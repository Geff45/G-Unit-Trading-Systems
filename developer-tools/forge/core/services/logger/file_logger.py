"""
Atlas Forge File Logger

Version: 1.0.0
"""

from pathlib import Path

from .log_record import LogRecord


class FileLogger:

    def __init__(self, logfile: Path):

        self._logfile = logfile

    def write(self, record: LogRecord) -> None:

        with self._logfile.open(
            "a",
            encoding="utf-8"
        ) as f:

            f.write(
                f"[{record.timestamp:%Y-%m-%d %H:%M:%S}] "
                f"[{record.level.value}] "
                f"[{record.source}] "
                f"{record.message}\n"
            )