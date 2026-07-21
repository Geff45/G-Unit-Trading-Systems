from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Evidence:

    source: str

    category: str

    instrument: str

    direction: float

    confidence: float

    weight: float

    timestamp: datetime

    metadata: dict