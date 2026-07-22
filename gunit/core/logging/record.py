"""
Immutable log record.
"""

from dataclasses import dataclass, field
from datetime import UTC
from datetime import datetime

from .levels import LogLevel


@dataclass(slots=True, frozen=True)
class LogRecord:

    level: LogLevel

    logger: str

    message: str

    timestamp: datetime = field(
    default_factory=lambda: datetime.now(UTC)
)

    module: str = ""

    function: str = ""

    line: int = 0

    thread: str = ""

    process: int = 0

    exception: str | None = None