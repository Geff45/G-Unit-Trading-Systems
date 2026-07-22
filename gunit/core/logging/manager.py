"""
Logger manager.
"""

from __future__ import annotations

from .formatter import StandardFormatter
from .handlers import ConsoleHandler
from .levels import LogLevel
from .logger import Logger


class LoggerManager:
    """
    Creates and caches loggers.
    """

    def __init__(self) -> None:
        self._loggers: dict[str, Logger] = {}

    def get_logger(self, name: str) -> Logger:
        if name not in self._loggers:
            logger = Logger(name, LogLevel.INFO)
            logger.add_handler(
                ConsoleHandler(StandardFormatter())
            )
            self._loggers[name] = logger

        return self._loggers[name]