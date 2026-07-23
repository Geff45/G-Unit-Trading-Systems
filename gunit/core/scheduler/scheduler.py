"""
Task scheduler.
"""

from __future__ import annotations


class Scheduler:
    """
    Simple scheduler placeholder.
    """

    def __init__(self) -> None:
        self._started = False

    @property
    def started(self) -> bool:
        return self._started

    def start(self) -> None:
        self._started = True

    def stop(self) -> None:
        self._started = False