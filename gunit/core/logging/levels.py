"""
Logging levels.
"""

from enum import IntEnum


class LogLevel(IntEnum):
    TRACE = 5
    DEBUG = 10
    INFO = 20
    SUCCESS = 25
    WARNING = 30
    ERROR = 40
    CRITICAL = 50

    @property
    def label(self) -> str:
        return self.name

    @classmethod
    def from_string(cls, value: str) -> "LogLevel":
        value = value.upper()

        try:
            return cls[value]
        except KeyError:
            raise ValueError(f"Unknown log level: {value}")