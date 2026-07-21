from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any
import uuid


@dataclass(slots=True)
class Event:
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    event_type: str = ""
    source: str = ""
    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))
    payload: Any = None