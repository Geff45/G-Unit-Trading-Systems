from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
import uuid


@dataclass(slots=True)
class Message:
    """
    Atlas Enterprise Service Bus Message

    Represents the business payload travelling
    through the Atlas Service Bus.
    """

    topic: str

    payload: Any

    priority: int = 3

    message_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )