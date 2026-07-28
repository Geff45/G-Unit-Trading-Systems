from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class CommandResult:
    """
    Represents the result of a Forge command.
    """

    success: bool = True
    message: str = ""
    data: Any = None

    @classmethod
    def ok(cls, message: str = "", data: Any = None):
        return cls(
            success=True,
            message=message,
            data=data,
        )

    @classmethod
    def fail(cls, message: str):
        return cls(
            success=False,
            message=message,
        )