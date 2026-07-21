"""
G-UNIT Platform Kernel

Event Models
"""


from dataclasses import dataclass, field

from datetime import datetime

from typing import Dict



@dataclass
class PlatformEvent:
    """
    Represents a system event.
    """


    name: str


    source: str


    data: Dict = field(
        default_factory=dict
    )


    timestamp: datetime = field(
        default_factory=datetime.utcnow
    )