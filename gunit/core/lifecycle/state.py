"""
Lifecycle states.
"""

from enum import Enum
from enum import auto


class LifecycleState(Enum):
    """
    Atlas lifecycle states.
    """

    CREATED = auto()

    INITIALIZING = auto()

    RUNNING = auto()

    STOPPING = auto()

    STOPPED = auto()

    FAILED = auto()