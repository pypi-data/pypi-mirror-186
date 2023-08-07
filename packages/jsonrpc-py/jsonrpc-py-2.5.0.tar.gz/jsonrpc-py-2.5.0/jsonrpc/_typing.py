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

from collections.abc import Iterable, Iterator
from types import TracebackType
from typing import Any, Final, Protocol, TypeAlias, Union

__all__: Final[tuple[str, ...]] = (
    "Headers",
    "InputStream",
    "OptExcInfo",
    "Serializer",
    "StartResponse",
    "WSGIEnvironment",
)

Headers: TypeAlias = list[tuple[str, str]]
OptExcInfo: TypeAlias = Union[tuple[type[Exception], Exception, TracebackType | None], tuple[None, None, None]]
WSGIEnvironment: TypeAlias = dict[str, Any]


class StartResponse(Protocol):
    def __call__(self, status: str, headers: Headers, exc_info: OptExcInfo | None = ..., /) -> Any:
        ...


class InputStream(Iterable[bytes], Protocol):
    def read(self, size: int = ..., /) -> bytes:
        ...

    def readline(self, size: int = ..., /) -> bytes:
        ...

    def readlines(self, hint: int = ..., /) -> Iterator[bytes]:
        ...


class Serializer(Protocol):
    def serialize(self, obj: Any, /) -> bytes:
        ...

    def deserialize(self, obj: bytes, /) -> Any:
        ...
