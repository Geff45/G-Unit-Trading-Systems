"""
Scheduled job.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from .schedule import Schedule


@dataclass(slots=True)
class ScheduledJob:
    """
    Represents a scheduled task.
    """

    name: str

    action: Callable[[], None]

    schedule: Schedule

    enabled: bool = True