"""
Atlas engine states.
"""

from enum import Enum
from enum import auto


class AtlasState(Enum):
    """
    Atlas engine lifecycle.
    """

    CREATED = auto()

    CONFIGURING = auto()

    INITIALIZING = auto()

    STARTING = auto()

    RUNNING = auto()

    STOPPING = auto()

    STOPPED = auto()

    FAILED = auto()