"""
Atlas Forge Console Logger

Version: 1.0.0
"""

from .log_record import LogRecord


class ConsoleLogger:

    def write(self, record: LogRecord) -> None:

        print(
            f"[{record.timestamp:%Y-%m-%d %H:%M:%S}] "
            f"[{record.level.value}] "
            f"[{record.source}] "
            f"{record.message}"
        )