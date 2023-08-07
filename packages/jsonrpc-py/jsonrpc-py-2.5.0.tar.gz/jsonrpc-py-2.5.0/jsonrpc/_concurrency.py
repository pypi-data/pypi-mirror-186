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
from concurrent.futures import Executor, Future, ThreadPoolExecutor
from contextvars import Context, ContextVar, copy_context
from functools import partial
from typing import Final, ParamSpec, TypeVar

__all__: Final[tuple[str, ...]] = (
    "get_executor",
    "run_in_executor",
    "set_executor",
)

_global_executor: Final[ContextVar[Executor]] = ContextVar("GlobalExecutor")

_P = ParamSpec("_P")
_T = TypeVar("_T")


def get_executor() -> Executor:
    try:
        return _global_executor.get()
    except LookupError:
        set_executor(fallback := ThreadPoolExecutor())
        return fallback


def set_executor(value: Executor, /) -> None:
    _global_executor.set(value)


def run_in_executor(user_function: Callable[_P, _T], /, *args: _P.args, **kwargs: _P.kwargs) -> Future[_T]:
    context: Final[Context] = copy_context()
    callback: partial[_T] = partial(context.run, user_function, *args, **kwargs)
    executor: Final[Executor] = get_executor()
    return executor.submit(callback)
