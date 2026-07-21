from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class HealthReport:

    service: str

    healthy: bool

    version: str

    started_at: datetime | None = None

    warnings: int = 0

    errors: int = 0