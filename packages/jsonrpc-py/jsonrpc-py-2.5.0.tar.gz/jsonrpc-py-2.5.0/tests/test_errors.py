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

from dataclasses import is_dataclass
from typing import Final
from unittest.case import TestCase

from jsonrpc._errors import Error, ErrorEnum
from jsonrpc._utilities import Undefined


class TestError(TestCase):
    def test_inheritance(self) -> None:
        error: Final[Error] = Error(code=ErrorEnum.INTERNAL_ERROR, message="Internal Error")
        self.assertTrue(is_dataclass(error))
        self.assertIsInstance(error, Exception)

    def test_hash(self) -> None:
        for actual, expected in (
            (
                hash(Error(code=ErrorEnum.PARSE_ERROR, message="Parse Error")),
                hash((ErrorEnum.PARSE_ERROR, "Parse Error", Undefined)),
            ),
            (
                hash(Error(code=ErrorEnum.INVALID_REQUEST, message="Invalid Request", data=[1, 2, 3])),
                hash((ErrorEnum.INVALID_REQUEST, "Invalid Request", (1, 2, 3))),
            ),
        ):
            with self.subTest(actual=actual, expected=expected):
                self.assertEqual(actual, expected)

    def test_str(self) -> None:
        error: Final[Error] = Error(code=ErrorEnum.METHOD_NOT_FOUND, message="Method Not Found")
        self.assertEqual(str(error), f"{error.message!s}\u0020\u0028{error.code:d}\u0029")

    def test_json(self) -> None:
        for actual, expected in (
            (
                Error(code=ErrorEnum.INVALID_PARAMETERS, message="Invalid Parameters").json,
                {"code": ErrorEnum.INVALID_PARAMETERS, "message": "Invalid Parameters"},
            ),
            (
                Error(code=ErrorEnum.INTERNAL_ERROR, message="Internal Error", data={"additional": "information"}).json,
                {"code": ErrorEnum.INTERNAL_ERROR, "message": "Internal Error", "data": {"additional": "information"}},
            ),
        ):
            with self.subTest(actual=actual, expected=expected):
                self.assertDictEqual(actual, expected)
