"""
Command execution context.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class CommandContext:
    """
    Context passed during command execution.
    """

    user: str | None = None

    correlation_id: str | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict
    )