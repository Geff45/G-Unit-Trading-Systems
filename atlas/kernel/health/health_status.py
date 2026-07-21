from enum import Enum


class HealthStatus(Enum):

    HEALTHY = "healthy"

    WARNING = "warning"

    CRITICAL = "critical"

    OFFLINE = "offline"