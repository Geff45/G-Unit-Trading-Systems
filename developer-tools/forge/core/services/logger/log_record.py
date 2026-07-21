"""
Atlas Forge Log Record

Version: 1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from .log_level import LogLevel


@dataclass(slots=True)
class LogRecord:

    level: LogLevel

    source: str

    message: str

    timestamp: datetime = field(default_factory=datetime.utcnow)

    exception: str | None = None