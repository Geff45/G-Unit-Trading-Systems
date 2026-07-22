"""
Enterprise log handlers.
"""

from __future__ import annotations

from pathlib import Path
from threading import Lock

from .protocol import LogFormatter
from .protocol import LogHandler
from .record import LogRecord


class ConsoleHandler(LogHandler):

    def __init__(self, formatter: LogFormatter):

        self.formatter = formatter

    def emit(self, record: LogRecord) -> None:

        print(self.formatter.format(record))


class FileHandler(LogHandler):

    def __init__(self, path: str | Path, formatter: LogFormatter):

        self.path = Path(path)

        self.path.parent.mkdir(parents=True, exist_ok=True)

        self.formatter = formatter

        self._lock = Lock()

    def emit(self, record: LogRecord) -> None:

        text = self.formatter.format(record)

        with self._lock:

            with self.path.open(
                "a",
                encoding="utf-8",
            ) as file:

                file.write(text)

                file.write("\n")