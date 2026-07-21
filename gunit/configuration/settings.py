"""
G-UNIT Platform Kernel

Configuration Settings Models
"""


from dataclasses import dataclass, field
from typing import Dict



@dataclass
class PlatformSettings:
    """
    Global platform configuration.
    """

    name: str = "G-UNIT"

    version: str = "1.0"

    environment: str = "development"

    debug: bool = True

    metadata: Dict = field(
        default_factory=dict
    )