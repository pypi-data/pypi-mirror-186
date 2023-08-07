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

from collections.abc import Iterator
from concurrent.futures import Executor, Future, ThreadPoolExecutor
from contextlib import contextmanager
from typing import Final
from unittest.case import TestCase
from unittest.mock import Mock

from jsonrpc._concurrency import get_executor, run_in_executor, set_executor

from .fixtures.dummy_executor import DummyExecutor


class TestConcurrency(TestCase):
    @contextmanager
    def dummy_executor(self) -> Iterator[DummyExecutor]:
        executor: Final[Executor] = get_executor()
        set_executor(dummy_executor := DummyExecutor())

        try:
            yield dummy_executor
        finally:
            set_executor(executor)

    def test_get_set_executor(self) -> None:
        fallback_executor: Final[ThreadPoolExecutor] = get_executor()
        self.assertIsInstance(fallback_executor, ThreadPoolExecutor)

        set_executor(dummy_executor := DummyExecutor())
        self.assertIsInstance(dummy_executor, DummyExecutor)

    def test_run_in_executor(self) -> None:
        with self.dummy_executor():
            mock: Final[Mock] = Mock(return_value=None)
            future: Future[None] = run_in_executor(mock, 1, 2, 3, key="value")
            self.assertIsInstance(future, Future)
            self.assertTrue(future.done())
            self.assertIsNone(future.result())
            mock.assert_called_with(1, 2, 3, key="value")
