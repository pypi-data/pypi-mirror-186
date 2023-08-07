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

from collections import UserList
from dataclasses import dataclass
from numbers import Number
from types import NoneType
from typing import Any, Final

from ._errors import Error
from ._utilities import Undefined, UndefinedType, make_hashable

__all__: Final[tuple[str, ...]] = (
    "BatchResponse",
    "Response",
)


@dataclass(kw_only=True, slots=True)
class Response:
    """
    Base JSON-RPC response object.
    """

    #: An any type of object that contains a result of successful processing
    #: the :class:`jsonrpc.Request` object. This attribute must not be set if there an error has occurred.
    body: Any = Undefined
    #: The :class:`jsonrpc.Error` object representing an erroneous processing
    #: the :class:`jsonrpc.Request` object. This attribute must not be set if no one error has occurred.
    error: Error | UndefinedType = Undefined
    #: The same attribute as :attr:`jsonrpc.Request.request_id`
    #: except that its value might be equal to :py:data:`None` in erroneous responses.
    response_id: str | float | UndefinedType | None = Undefined

    def __post_init__(self) -> None:
        self._validate_body_and_error()
        self._validate_response_id()

    def __hash__(self) -> int:
        return hash((make_hashable(self.body), self.error, self.response_id))

    def _validate_body_and_error(self) -> None:
        if isinstance(self.body, UndefinedType) == isinstance(self.error, UndefinedType):
            raise TypeError("Either 'body' or 'error' attribute must be set")

    def _validate_response_id(self) -> None:
        if not isinstance(self.response_id, str | Number | UndefinedType | NoneType):
            raise TypeError(f"Response id must be an optional string or number, not a {type(self.response_id).__name__!r}")

    @property
    def json(self) -> dict[str, Any]:
        """
        Returns the :py:class:`dict` object needed for the serialization.

        Example successful response::

            >>> response: Response = Response(body="foobar", response_id=65535)
            >>> response.json
            {"jsonrpc": "2.0", "result": "foobar", "id": 65535}

        Example erroneous response::

            >>> error: Error = Error(code=ErrorEnum.INTERNAL_ERROR, message="Unexpected error")
            >>> response: Response = Response(error=error, response_id="6ba7b810")
            >>> response.json
            {"jsonrpc": "2.0", "error": {"code": -32603, "message": "Unexpected error"}, "id": "6ba7b810"}
        """
        obj: dict[str, Any] = {"jsonrpc": "2.0"}

        if isinstance(error := self.error, UndefinedType):
            obj |= {"result": self.body}
        else:
            obj |= {"error": error.json}
        if not isinstance(response_id := self.response_id, UndefinedType):
            obj |= {"id": response_id}

        return obj


class BatchResponse(UserList[Response]):
    """
    The :py:class:`collections.UserList` subclass representing the collection
    of :class:`jsonrpc.Response` objects.
    """

    __slots__: tuple[str, ...] = ()

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({self.data!r})"

    def __hash__(self) -> int:
        return hash(tuple(self.data))

    @property
    def json(self) -> list[dict[str, Any]]:
        """
        Returns the :py:class:`list` of :py:class:`dict` objects needed for the serialization.

        Example output::

            >>> response: BatchResponse = BatchResponse([
            ...     Response(body="foobar", response_id=1024),
            ...     Response(
            ...         error=Error(code=ErrorEnum.INTERNAL_ERROR, message="Unexpected error"),
            ...         response_id="6ba7b810"
            ...     )
            ... ])
            >>> response.json
            [
                {"jsonrpc": "2.0", "result": "foobar", "id": 1024},
                {"jsonrpc": "2.0", "error": {"code": -32603, "message": "Unexpected error"}, "id": "6ba7b810"}
            ]
        """
        return list(map(lambda response: response.json, self))
