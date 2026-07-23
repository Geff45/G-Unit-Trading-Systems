"""
Atlas scheduler service.
"""

from __future__ import annotations

from gunit.core.scheduler.scheduler import Scheduler


class SchedulerService:
    """
    Atlas wrapper around Scheduler.
    """

    def __init__(self) -> None:
        self._scheduler = Scheduler()

    @property
    def scheduler(self) -> Scheduler:
        return self._scheduler