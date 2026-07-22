"""
Runtime lifecycle states.
"""

from __future__ import annotations

from enum import Enum
from enum import auto


class RuntimeState(Enum):
    """
    Represents the current runtime lifecycle state.
    """

    CREATED = auto()

    INITIALIZING = auto()

    STARTING = auto()

    RUNNING = auto()

    STOPPING = auto()

    STOPPED = auto()

    FAILED = auto()