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

import json as _json
import pickle as _pickle
from io import BytesIO, StringIO
from sys import getdefaultencoding
from typing import Any, ClassVar, Final

from ._errors import Error, ErrorEnum

__all__: Final[tuple[str, ...]] = (
    "JSONSerializer",
    "PickleSerializer",
)


class JSONSerializer:
    """
    Simple class for JSON serialization and deserialization.
    """

    __slots__: tuple[str, ...] = ()

    #: Returns the name of the current default string encoding.
    #: Default value retrieves from the :py:func:`sys.getdefaultencoding`.
    DEFAULT_ENCODING: ClassVar[str] = getdefaultencoding()

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}()"

    def serialize(self, obj: Any, /) -> bytes:
        """
        Returns the JSON representation of a value.

        :param obj: An any type of object that must be JSON serializable.
        :raises jsonrpc.Error: If any exception has occurred due the serialization or/and encoding to :py:class:`bytes`.
        :returns: The :py:class:`bytes` object containing the serialized Python data structure.
        """
        try:
            with StringIO() as raw_buffer:
                _json.dump(obj, raw_buffer, ensure_ascii=False, separators=(",", ":"))
                return raw_buffer.getvalue().encode(self.DEFAULT_ENCODING)
        except Exception as exc:
            raise Error(code=ErrorEnum.PARSE_ERROR, message="Failed to serialize object to JSON") from exc

    def deserialize(self, obj: bytes, /) -> Any:
        """
        Returns the value encoded in JSON in appropriate Python type.

        :param obj: The :py:class:`bytes` object containing the serialized JSON document.
        :raises jsonrpc.Error: If any exception has occurred due the deserialization or/and decoding from :py:class:`bytes`.
        :returns: An any type of object containing the deserialized Python data structure.
        """
        try:
            with BytesIO(obj) as raw_buffer:
                return _json.load(raw_buffer)
        except Exception as exc:
            raise Error(code=ErrorEnum.PARSE_ERROR, message="Failed to deserialize object from JSON") from exc


class PickleSerializer:
    """
    Simple class for the "Pickling" and "Unpickling" Python objects.
    """

    __slots__: tuple[str, ...] = ()

    #: Pickle protocol version used for the serialization.
    #: Defaults to :py:data:`pickle.HIGHEST_PROTOCOL`.
    PROTOCOL_VERSION: ClassVar[int] = _pickle.HIGHEST_PROTOCOL

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}()"

    def serialize(self, obj: Any, /) -> bytes:
        """
        Returns the pickled representation of a value.

        :param obj: An any type of object that must be serializable.
        :raises jsonrpc.Error: If exception has occurred due the pickling.
        :returns: The :py:class:`bytes` object containing the pickled object.
        """
        try:
            with BytesIO() as raw_buffer:
                _pickle.dump(obj, raw_buffer, self.PROTOCOL_VERSION)
                return raw_buffer.getvalue()
        except Exception as exc:
            raise Error(code=ErrorEnum.PARSE_ERROR, message="Failed to serialize object") from exc

    def deserialize(self, obj: bytes, /) -> Any:
        """
        Returns the unpickled representation of a value.

        :param obj: The :py:class:`bytes` object containing the pickled object.
        :raises jsonrpc.Error: If exception has occurred due the unpickling.
        :returns: An any type of object containing the deserialized Python data structure.
        """
        try:
            with BytesIO(obj) as raw_buffer:
                return _pickle.load(raw_buffer)
        except Exception as exc:
            raise Error(code=ErrorEnum.PARSE_ERROR, message="Failed to deserialize object") from exc
