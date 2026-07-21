from dataclasses import dataclass, field
from datetime import datetime, UTC

from kernel.logging.log_level import LogLevel


@dataclass(slots=True)
class LogEntry:

    level: LogLevel

    source: str

    message: str

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )