"""
Logging protocol definitions.
"""

from abc import ABC, abstractmethod

from .record import LogRecord


class LogHandler(ABC):

    @abstractmethod
    def emit(self, record: LogRecord) -> None:
        ...


class LogFormatter(ABC):

    @abstractmethod
    def format(self, record: LogRecord) -> str:
        ...