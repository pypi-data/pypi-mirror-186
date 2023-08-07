# Pure zero-dependency JSON-RPC 2.0 implementation.
# Copyright © 2022-2023 Andrew Malchuk. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from collections import UserDict
from collections.abc import Iterable, Iterator, MutableSequence
from concurrent.futures import Future, as_completed
from functools import partial, singledispatchmethod
from http import HTTPStatus
from io import DEFAULT_BUFFER_SIZE, BytesIO
from sys import exc_info
from traceback import print_exception
from typing import Any, ClassVar, Final, TypeAlias

from ._concurrency import run_in_executor
from ._dispatcher import Dispatcher
from ._errors import Error
from ._request import BatchRequest, Request
from ._response import BatchResponse, Response
from ._serializer import JSONSerializer
from ._typing import Headers, InputStream, OptExcInfo, Serializer, StartResponse, WSGIEnvironment

__all__: Final[tuple[str, ...]] = ("WSGIHandler",)

_AnyRequest: TypeAlias = Request | Error | BatchRequest
_AnyResponse: TypeAlias = Response | BatchResponse | None


class _RequestHandlerMixIn:
    __slots__: tuple[str, ...] = ()

    @singledispatchmethod
    def _handle_deserialized_object(self, obj: _AnyRequest, *, dispatcher: Dispatcher) -> _AnyResponse:
        raise NotImplementedError(f"Unsupported type {type(obj).__name__!r}")  # pragma: no cover

    @_handle_deserialized_object.register
    def _(self, request: Request, *, dispatcher: Dispatcher) -> Response | None:
        future: Future[Any] = run_in_executor(dispatcher.dispatch, request.method, *request.args, **request.kwargs)
        if request.is_notification:
            return None
        try:
            result: Final[Any] = future.result()
            return Response(body=result, response_id=request.request_id)
        except Error as error:
            return Response(error=error, response_id=request.request_id)

    @_handle_deserialized_object.register
    def _(self, error: Error, /, **kwargs: Any) -> Response:
        return Response(error=error, response_id=None)

    @_handle_deserialized_object.register
    def _(self, batch_request: BatchRequest, *, dispatcher: Dispatcher) -> BatchResponse:
        futures: frozenset[Future[_AnyResponse]] = frozenset(
            as_completed(run_in_executor(self._handle_deserialized_object, obj, dispatcher=dispatcher) for obj in batch_request)
        )
        return BatchResponse(response for future in futures if isinstance(response := future.result(), Response))


class _SerializableMixIn(_RequestHandlerMixIn):
    __slots__: tuple[str, ...] = ()

    def _process_raw_object(self, body: bytes, *, dispatcher: Dispatcher, serializer: Serializer) -> bytes:
        try:
            obj: Any = serializer.deserialize(body)
        except Error as error:
            deserialization_error: Response = Response(error=error, response_id=None)
            return serializer.serialize(deserialization_error.json)

        is_batch_request: Final[bool] = isinstance(obj, MutableSequence) and len(obj) >= 1
        request: Final[_AnyRequest] = BatchRequest.from_json(obj) if is_batch_request else Request.from_json(obj)

        if not (response := self._handle_deserialized_object(request, dispatcher=dispatcher)):
            return b""

        try:
            return serializer.serialize(response.json)
        except Error as error:
            serialization_error: Response = Response(error=error, response_id=None)
            return serializer.serialize(serialization_error.json)


class WSGIHandler(UserDict[str, Any], _SerializableMixIn):
    """
    Base class representing the ``WSGI`` entry point.
    Its subclassing the :py:class:`collections.UserDict` object
    for providing the user-defined data storage.

    For example::

        >>> app = WSGIHandler()
        >>> app["my_private_key"] = "foobar"
        >>> app["my_private_key"]
        "foobar"
    """

    __slots__: tuple[str, ...] = ()

    #: The default content type of the responses.
    default_content_type: ClassVar[str] = "application/json"

    #: The list of HTTP request methods which are allowed to use.
    allowed_http_methods: ClassVar[Iterable[str]] = ("POST", "PUT")

    #: Class variable representing the :class:`jsonrpc.Dispatcher` object
    #: used by this class for routing user-defined functions by default.
    dispatcher: ClassVar[Dispatcher] = Dispatcher()

    #: Class variable representing the :class:`jsonrpc.JSONSerializer` object
    #: used by this class for data serialization by default.
    serializer: ClassVar[Serializer] = JSONSerializer()

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({self.data!r})"

    def __call__(self, environ: WSGIEnvironment, start_response: StartResponse, /) -> Iterator[bytes]:
        # Prevents the "start_response" argument duplicate invocation:
        wsgi_response: partial[Iterator[bytes]] = partial(self._get_response, start_response)

        if environ["REQUEST_METHOD"] not in self.allowed_http_methods:
            # Specified request method is invalid:
            return wsgi_response(status=HTTPStatus.METHOD_NOT_ALLOWED)

        try:
            if not (body := self._read_request_body(environ)):
                # Trying to check the request body is empty.
                # If that's true then it returns HTTP 400 "Bad Request".
                return wsgi_response(status=HTTPStatus.BAD_REQUEST)

            if not (response_body := self._process_raw_object(body, dispatcher=self.dispatcher, serializer=self.serializer)):
                # Trying to check the response is empty.
                # If that's true then it returns empty response body.
                return wsgi_response(status=HTTPStatus.NO_CONTENT)

            # We're on a roll, baby. Send the response as is.
            return wsgi_response(response_body=response_body)

        except Exception as exc:
            # Houston, we have a problem O_o
            # In unexpected situations it raises the exception to WSGI server.
            print_exception(exc, file=environ["wsgi.errors"])
            return wsgi_response(status=HTTPStatus.INTERNAL_SERVER_ERROR, exc_info=exc_info())

    def _read_request_body(self, environ: WSGIEnvironment, /) -> bytes:
        try:
            content_length: int = int(environ["CONTENT_LENGTH"])
        except (KeyError, ValueError):
            return b""

        stream: Final[InputStream] = environ["wsgi.input"]

        with BytesIO() as raw_buffer:
            # Ensure to disallow reading the stream more bytes
            # than specified by "Content-Length" header:
            while content_length > 0:
                if not (chunk := stream.read(min(content_length, DEFAULT_BUFFER_SIZE))):
                    raise EOFError(f"Client disconnected, {content_length:d} more bytes were expected")

                # Appends the chunk of request body to the buffer
                # and decreases the request size:
                content_length -= raw_buffer.write(chunk)

            return raw_buffer.getvalue()

    def _get_response(
        self,
        start_response: StartResponse,
        *,
        status: HTTPStatus = HTTPStatus.OK,
        response_body: bytes | None = None,
        exc_info: OptExcInfo | None = None,
    ) -> Iterator[bytes]:
        content_length: Final[int] = len(response_body := b"" if response_body is None else response_body)
        headers: Final[Headers] = [
            ("Content-Length", f"{content_length:d}"),
            ("Content-Type", self.default_content_type),
        ]

        if status == HTTPStatus.METHOD_NOT_ALLOWED:
            # Fill the allowed request methods if the specified method is invalid:
            headers.append(("Allow", "\u002c\u0020".join(self.allowed_http_methods)))
            headers.sort()

        start_response(f"{status.value:d}\u0020{status.phrase!s}", headers, exc_info)
        yield response_body
