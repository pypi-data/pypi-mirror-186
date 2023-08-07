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

from collections.abc import Callable, MutableMapping
from types import FunctionType, LambdaType
from typing import NoReturn, TypeVar
from unittest.case import TestCase

from jsonrpc._dispatcher import Dispatcher
from jsonrpc._errors import Error, ErrorEnum

_T = TypeVar("_T")


class TestDispatcher(TestCase):
    def setUp(self) -> None:
        self.dispatcher: Dispatcher = Dispatcher()

    def test_inheritance(self) -> None:
        self.assertIsInstance(self.dispatcher, MutableMapping)

    def test_register_not_function(self) -> None:
        with self.assertRaises(RuntimeError) as context:
            self.dispatcher.register(print)

        self.assertIn("isn't a user-defined function", str(context.exception))

    def test_register_already_defined(self) -> None:
        test_lambda: Callable[..., None] = lambda: None
        self.dispatcher.register(test_lambda, function_name="test_lambda")
        self.assertIn("test_lambda", self.dispatcher)
        self.assertIsInstance(self.dispatcher["test_lambda"], LambdaType)
        self.assertEqual(self.dispatcher["test_lambda"], test_lambda)

        with self.assertRaises(RuntimeError) as context:
            self.dispatcher.register(test_lambda, function_name="test_lambda")

        self.assertIn("is already defined", str(context.exception))

    def test_dispatch_non_existent_function(self) -> None:
        with self.assertRaises(Error) as context:
            self.dispatcher.dispatch("non_existent_function")

        self.assertEqual(context.exception.code, ErrorEnum.METHOD_NOT_FOUND)

    def test_dispatch_non_existent_parameter(self) -> None:
        test_lambda: Callable[[_T], _T] = lambda obj: obj
        self.dispatcher.register(test_lambda, function_name="test_lambda")
        self.assertIn("test_lambda", self.dispatcher)
        self.assertIsInstance(self.dispatcher["test_lambda"], LambdaType)
        self.assertEqual(self.dispatcher["test_lambda"], test_lambda)

        with self.assertRaises(Error) as context:
            self.dispatcher.dispatch("test_lambda", non_existent_parameter="non_existent_parameter")

        self.assertEqual(context.exception.code, ErrorEnum.INVALID_PARAMETERS)

    def test_dispatch_division(self) -> None:
        @self.dispatcher.register(function_name="my_div")
        def div(a: float, b: float) -> float:
            return a / b

        self.assertNotIn("div", self.dispatcher)
        self.assertIn("my_div", self.dispatcher)
        self.assertIsInstance(self.dispatcher["my_div"], FunctionType)
        self.assertEqual(self.dispatcher["my_div"], div)

        with self.assertRaises(Error) as context:
            self.dispatcher.dispatch("my_div", 10, 0)

        self.assertEqual(context.exception.code, ErrorEnum.INTERNAL_ERROR)
        self.assertIn("division by zero", context.exception.message)

    def test_dispatch_raising(self) -> None:
        @self.dispatcher.register
        def raising(*, code: int, message: str) -> NoReturn:
            raise Error(code=code, message=message)

        self.assertIn("raising", self.dispatcher)
        self.assertIsInstance(self.dispatcher["raising"], FunctionType)
        self.assertEqual(self.dispatcher["raising"], raising)

        with self.assertRaises(Error) as context:
            self.dispatcher.dispatch("raising", code=ErrorEnum.INTERNAL_ERROR, message="for testing purposes")

        self.assertEqual(context.exception.code, ErrorEnum.INTERNAL_ERROR)
        self.assertEqual(context.exception.message, "for testing purposes")
