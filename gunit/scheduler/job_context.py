"""
Scheduler job context.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class JobContext:
    """
    Context passed to scheduler jobs.
    """

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    cancelled: bool = False