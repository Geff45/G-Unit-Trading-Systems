from dataclasses import dataclass, field
from datetime import datetime, UTC


@dataclass(slots=True)
class Metric:

    name: str

    value: float

    unit: str

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )