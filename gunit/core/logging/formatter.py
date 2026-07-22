"""
Enterprise log formatters.
"""

from __future__ import annotations

import json

from .protocol import LogFormatter
from .record import LogRecord


class StandardFormatter(LogFormatter):
    """
    Human-readable formatter.
    """

    def format(self, record: LogRecord) -> str:

        return (
            f"{record.timestamp.isoformat()} "
            f"[{record.level.label}] "
            f"[{record.logger}] "
            f"{record.message}"
        )


class JsonFormatter(LogFormatter):
    """
    Structured formatter.
    """

    def format(self, record: LogRecord) -> str:

        return json.dumps(
            {
                "timestamp": record.timestamp.isoformat(),
                "level": record.level.label,
                "logger": record.logger,
                "message": record.message,
                "module": record.module,
                "function": record.function,
                "line": record.line,
            }
        )