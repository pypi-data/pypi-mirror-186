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

from collections.abc import MutableSequence
from pickle import dumps
from unittest.case import TestCase

from jsonrpc._errors import Error, ErrorEnum
from jsonrpc._serializer import JSONSerializer, PickleSerializer


class TestJSONSerializer(TestCase):
    def setUp(self) -> None:
        self.serializer: JSONSerializer = JSONSerializer()

    def test_serialize(self) -> None:
        self.assertIsInstance(self.serializer.serialize([1, 2, 3]), bytes)
        self.assertEqual(self.serializer.serialize(None), b"null")

        with self.assertRaises(Error) as context:
            self.serializer.serialize(object())

        self.assertEqual(context.exception.code, ErrorEnum.PARSE_ERROR)
        self.assertEqual(context.exception.message, "Failed to serialize object to JSON")

    def test_deserialize(self) -> None:
        self.assertIsInstance(sequence := self.serializer.deserialize(b"[1, 2, 3]"), MutableSequence)
        self.assertListEqual(sequence, [1, 2, 3])

        with self.assertRaises(Error) as context:
            self.serializer.deserialize(b"hello world")

        self.assertEqual(context.exception.code, ErrorEnum.PARSE_ERROR)
        self.assertEqual(context.exception.message, "Failed to deserialize object from JSON")


class TestPickleSerializer(TestCase):
    def setUp(self) -> None:
        self.serializer: PickleSerializer = PickleSerializer()

    def test_serialize(self) -> None:
        self.assertIsInstance(self.serializer.serialize([1, 2, 3]), bytes)
        self.assertEqual(self.serializer.serialize(None), dumps(None, self.serializer.PROTOCOL_VERSION))

        with self.assertRaises(Error) as context:
            import sys

            self.serializer.serialize(sys)

        self.assertEqual(context.exception.code, ErrorEnum.PARSE_ERROR)
        self.assertEqual(context.exception.message, "Failed to serialize object")

    def test_deserialize(self) -> None:
        serialized: bytes = dumps(expected := [1, 2, 3], self.serializer.PROTOCOL_VERSION)
        self.assertIsInstance(actual := self.serializer.deserialize(serialized), MutableSequence)
        self.assertListEqual(actual, expected)

        with self.assertRaises(Error) as context:
            self.serializer.deserialize(b"hello world")

        self.assertEqual(context.exception.code, ErrorEnum.PARSE_ERROR)
        self.assertEqual(context.exception.message, "Failed to deserialize object")
