"""
G-UNIT Platform Kernel

Health Report Models
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class HealthReport:
    """
    Overall platform health report.
    """

    platform_status: str

    services: List[str] = field(default_factory=list)

    warnings: List[str] = field(default_factory=list)

    errors: List[str] = field(default_factory=list)

    timestamp: datetime = field(default_factory=datetime.utcnow)

    @property
    def healthy(self) -> bool:
        return len(self.errors) == 0