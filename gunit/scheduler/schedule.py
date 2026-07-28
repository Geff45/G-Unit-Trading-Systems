"""
Schedule definition.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Schedule:
    """
    Defines when a job should run.
    """

    interval: float

    repeat: bool = True

    delay: float = 0.0