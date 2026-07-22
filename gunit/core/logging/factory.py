"""
Logger factory.
"""

from __future__ import annotations

from .manager import LoggerManager


class LoggerFactory:
    _manager: LoggerManager | None = None

    @classmethod
    def manager(cls) -> LoggerManager:
        if cls._manager is None:
            cls._manager = LoggerManager()

        return cls._manager

    @classmethod
    def get_logger(cls, name: str):
        return cls.manager().get_logger(name)