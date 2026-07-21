from __future__ import annotations

from dataclasses import dataclass
from typing import Generic
from typing import Optional
from typing import TypeVar

from common.results.error import AtlasError

T = TypeVar("T")


@dataclass(slots=True)
class Result(Generic[T]):

    success: bool

    value: Optional[T] = None

    error: Optional[AtlasError] = None

    @staticmethod
    def ok(value=None):

        return Result(
            success=True,
            value=value
        )

    @staticmethod
    def fail(error: AtlasError):

        return Result(
            success=False,
            error=error
        )