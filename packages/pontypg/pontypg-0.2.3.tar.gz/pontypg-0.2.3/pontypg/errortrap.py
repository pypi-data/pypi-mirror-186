import functools
from typing import Awaitable, Callable, TypeVar
from typing_extensions import ParamSpec

import asyncpg.exceptions  # type: ignore
from ponty import ValidationError


P = ParamSpec("P")
R = TypeVar("R")


def error_trap(f: Callable[P, Awaitable[R]]) -> Callable[P, Awaitable[R]]:
    @functools.wraps(f)
    async def wrapper(*a: P.args, **kw: P.kwargs) -> R:
        try:
            return await f(*a, **kw)

        except (
            asyncpg.exceptions.CheckViolationError,
            asyncpg.exceptions.ForeignKeyViolationError,
            asyncpg.exceptions.NotNullViolationError,
            asyncpg.exceptions.UniqueViolationError,
        ) as e:
            raise ValidationError(text=e.detail)

    return wrapper
