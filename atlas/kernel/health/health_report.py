from dataclasses import dataclass
from datetime import datetime, UTC

from kernel.health.health_status import HealthStatus


@dataclass(slots=True)
class HealthReport:

    service_id: str

    status: HealthStatus

    message: str

    timestamp: datetime = datetime.now(UTC)