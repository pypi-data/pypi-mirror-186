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

from collections.abc import Callable
from concurrent.futures import Executor, Future
from typing import Final, ParamSpec, TypeVar

_P = ParamSpec("_P")
_T = TypeVar("_T")


class DummyExecutor(Executor):
    __slots__: tuple[str, ...] = ()

    def submit(self, user_function: Callable[_P, _T], /, *args: _P.args, **kwargs: _P.kwargs) -> Future[_T]:
        future: Future[_T] = Future()
        future.set_running_or_notify_cancel()

        try:
            result: Final[_T] = user_function(*args, **kwargs)
        except BaseException as exception:
            future.set_exception(exception)
        else:
            future.set_result(result)

        return future
