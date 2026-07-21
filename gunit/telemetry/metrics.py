"""
G-UNIT Platform Kernel

Telemetry Metrics
"""


from dataclasses import dataclass, field

from datetime import datetime

from typing import Dict



@dataclass
class Metric:

    """
    Represents a telemetry measurement.
    """


    name: str


    value: float


    source: str


    metadata: Dict = field(
        default_factory=dict
    )


    timestamp: datetime = field(
        default_factory=datetime.utcnow
    )