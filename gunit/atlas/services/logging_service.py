"""
Atlas Logging Service.
"""

from __future__ import annotations

from gunit.core.logging.manager import LoggerManager


class LoggingService:
    """
    Provides a shared LoggerManager instance for Atlas.
    """

    def __init__(self) -> None:
        self._manager = LoggerManager()

    @property
    def manager(self) -> LoggerManager:
        return self._manager

    def get_logger(self, name: str):
        return self._manager.get_logger(name)