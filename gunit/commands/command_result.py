"""
Command result.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class CommandResult:
    """
    Result returned by command handlers.
    """

    success: bool

    message: str = ""

    value: Any = None