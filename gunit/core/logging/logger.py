"""
Core logger implementation.
"""

from __future__ import annotations

from .handlers import ConsoleHandler
from .levels import LogLevel
from .protocol import LogHandler
from .record import LogRecord


class Logger:
    """
    Enterprise logger.
    """

    def __init__(
        self,
        name: str,
        level: LogLevel = LogLevel.INFO,
    ) -> None:
        self.name = name
        self.level = level
        self._handlers: list[LogHandler] = []

    def add_handler(self, handler: LogHandler) -> None:
        if handler not in self._handlers:
            self._handlers.append(handler)

    def remove_handler(self, handler: LogHandler) -> None:
        if handler in self._handlers:
            self._handlers.remove(handler)

    def set_level(self, level: LogLevel) -> None:
        self.level = level

    def log(self, level: LogLevel, message: str) -> None:
        if level < self.level:
            return

        record = LogRecord(
            level=level,
            logger=self.name,
            message=message,
        )

        for handler in self._handlers:
            handler.emit(record)

    def trace(self, message: str) -> None:
        self.log(LogLevel.TRACE, message)

    def debug(self, message: str) -> None:
        self.log(LogLevel.DEBUG, message)

    def info(self, message: str) -> None:
        self.log(LogLevel.INFO, message)

    def warning(self, message: str) -> None:
        self.log(LogLevel.WARNING, message)

    def error(self, message: str) -> None:
        self.log(LogLevel.ERROR, message)

    def critical(self, message: str) -> None:
        self.log(LogLevel.CRITICAL, message)