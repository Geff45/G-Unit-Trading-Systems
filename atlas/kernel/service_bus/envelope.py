from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional
import uuid

from kernel.service_bus.message import Message


@dataclass(slots=True)
class Envelope:
    """
    Enterprise Atlas Service Bus Envelope.

    Every message travelling inside Atlas is wrapped
    inside an Envelope which contains routing,
    security and tracing information.
    """

    message: Message

    envelope_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    correlation_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    trace_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    sender: str = ""

    receiver: str = ""

    version: str = "ASB-1.0"

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    ttl: int = 60

    encrypted: bool = False

    compressed: bool = False

    signed: bool = False

    hash: Optional[str] = None

    signature: Optional[str] = None

    metadata: dict = field(default_factory=dict)