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
from collections.abc import Iterable, MutableMapping, MutableSequence
from dataclasses import dataclass
from numbers import Number
from re import match as _regex_match
from typing import Any, Final, Union

from ._errors import Error, ErrorEnum
from ._utilities import Undefined, UndefinedType, make_hashable

__all__: Final[tuple[str, ...]] = (
    "BatchRequest",
    "Request",
)


@dataclass(kw_only=True, slots=True)
class Request:
    """
    Base JSON-RPC request object.
    """

    #: The :py:class:`str` object containing the name of the method.
    method: str
    #: The object of type :py:class:`list` or :py:class:`dict` that holds the parameter values
    #: to be used during the invocation of the method.
    #: May be omitted if provided method has no parameters for example.
    params: list[object] | dict[str, object] | UndefinedType = Undefined
    #: The :py:class:`str` object or any type of :py:class:`numbers.Number` object which represents an identifier
    #: of the request instance. May be omitted. If its value omitted, the request assumed to be a notification.
    request_id: str | float | UndefinedType = Undefined

    def __post_init__(self) -> None:
        self._validate_method()
        self._validate_params()
        self._validate_request_id()

    def __hash__(self) -> int:
        return hash((self.method, make_hashable(self.params), self.request_id))

    def _validate_method(self) -> None:
        if not isinstance(self.method, str) or _regex_match("\x5E\x72\x70\x63\x5C\x2E", self.method):
            raise Error(
                code=ErrorEnum.INVALID_REQUEST,
                message="Request method must be a string and should not have a 'rpc.' prefix",
            )

    def _validate_params(self) -> None:
        if not isinstance(self.params, MutableSequence | MutableMapping | UndefinedType):
            raise Error(
                code=ErrorEnum.INVALID_REQUEST,
                message=f"Request params must be a sequence or mapping, not a {type(self.params).__name__!r}",
            )

    def _validate_request_id(self) -> None:
        if not isinstance(self.request_id, str | Number | UndefinedType):
            raise Error(
                code=ErrorEnum.INVALID_REQUEST,
                message=f"Request id must be an optional string or number, not a {type(self.request_id).__name__!r}",
            )

    @property
    def args(self) -> tuple[object, ...]:
        """
        Returns the :py:class:`tuple` object containing positional arguments of the method.
        """
        return tuple(params) if isinstance(params := self.params, MutableSequence) else ()

    @property
    def kwargs(self) -> dict[str, object]:
        """
        Returns the :py:class:`dict` object containing keyword arguments of the method.
        """
        return params if isinstance(params := self.params, MutableMapping) else {}

    @property
    def is_notification(self) -> bool:
        """
        Returns :py:data:`True` if the identifier of the request is omitted, :py:data:`False` elsewise.
        """
        return isinstance(self.request_id, UndefinedType)

    @staticmethod
    def from_json(obj: dict[str, Any], /) -> Union["Request", Error]:
        """
        The static method for creating the :class:`jsonrpc.Request` object from :py:class:`dict` object.
        Unlike the :class:`jsonrpc.Request` constructor, doesn't raises any exceptions by validations,
        it returns the :class:`jsonrpc.Error` as is.

        Example usage::

            >>> Request.from_json({"jsonrpc": "2.0", "method": "foobar", "id": 1})
            Request(method="foobar", params=Undefined, request_id=1)
            >>> Request.from_json({"not_jsonrpc": True})
            Error(code=-32600, message="Invalid request object", data={"not_jsonrpc": True})
        """
        try:
            match obj:
                case {"jsonrpc": "2.0", "method": method, "params": params, "id": request_id}:
                    return Request(method=method, params=params, request_id=request_id)
                case {"jsonrpc": "2.0", "method": method, "params": params}:
                    return Request(method=method, params=params)
                case {"jsonrpc": "2.0", "method": method, "id": request_id}:
                    return Request(method=method, request_id=request_id)
                case {"jsonrpc": "2.0", "method": method}:
                    return Request(method=method)
                case _ as data:
                    raise Error(code=ErrorEnum.INVALID_REQUEST, message="Invalid request object", data=data)
        except Error as error:
            return error


class BatchRequest(UserList[Request | Error]):
    """
    The :py:class:`collections.UserList` subclass representing the collection
    of :class:`jsonrpc.Request` and :class:`jsonrpc.Error` objects.
    """

    __slots__: tuple[str, ...] = ()

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({self.data!r})"

    def __hash__(self) -> int:
        return hash(tuple(self.data))

    @staticmethod
    def from_json(iterable: Iterable[dict[str, Any]], /) -> "BatchRequest":
        """
        The static method for creating the :class:`jsonrpc.BatchRequest` object from :py:class:`collections.abc.Iterable`
        of :py:class:`dict` objects.
        Similar to :func:`jsonrpc.Request.from_json` function it doesn't raises any exceptions.

        Example usage::

            >>> BatchRequest.from_json([
            ...     {"jsonrpc": "2.0", "method": "foobar", "id": 1},
            ...     {"not_jsonrpc": True}
            ... ])
            BatchRequest([Request(\u2026), Error(\u2026)])
        """
        return BatchRequest(map(Request.from_json, iterable))
