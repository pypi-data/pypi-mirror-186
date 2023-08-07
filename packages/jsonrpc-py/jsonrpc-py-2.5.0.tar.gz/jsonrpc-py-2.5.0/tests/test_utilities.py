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

from typing import Any, Literal
from unittest.case import TestCase

from jsonrpc._utilities import Undefined, UndefinedType, make_hashable


class TestHashable(TestCase):
    def test_equality(self) -> None:
        tests: tuple[tuple[Any, Any], ...] = (
            ([], ()),
            (["a", 1], ("a", 1)),
            ({}, ()),
            ({"a"}, ("a",)),
            (frozenset({"a"}), {"a"}),
            ({"a": 1, "b": 2}, (("a", 1), ("b", 2))),
            ({"b": 2, "a": 1}, (("a", 1), ("b", 2))),
            (("a", ["b", 1]), ("a", ("b", 1))),
            (("a", {"b": 1}), ("a", (("b", 1),))),
        )
        for actual, expected in tests:
            with self.subTest(actual=actual):
                self.assertEqual(make_hashable(actual), expected)

    def test_count_equality(self) -> None:
        tests: tuple[tuple[Any, Any], ...] = (
            ({"a": 1, "b": ["a", 1]}, (("a", 1), ("b", ("a", 1)))),
            ({"a": 1, "b": ("a", [1, 2])}, (("a", 1), ("b", ("a", (1, 2))))),
        )
        for actual, expected in tests:
            with self.subTest(actual=actual):
                self.assertCountEqual(make_hashable(actual), expected)

    def test_unhashable(self) -> None:
        class Unhashable:
            __hash__: Literal[None] = None

        with self.assertRaises(TypeError) as context:
            make_hashable(Unhashable())

        self.assertIn("unhashable type", str(context.exception))


class TestUndefined(TestCase):
    def test_hash(self) -> None:
        self.assertEqual(hash(Undefined), 0xDEADBEEF)

    def test_equality(self) -> None:
        self.assertEqual(Undefined, UndefinedType())
        self.assertNotEqual(Undefined, None)

    def test_is_truth(self) -> None:
        self.assertFalse(Undefined)
