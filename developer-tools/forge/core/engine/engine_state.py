"""
Atlas Forge Engine State

Defines the lifecycle states of the Atlas Engine.

Version: 1.0.0
"""

from enum import Enum, auto


class EngineState(Enum):
    CREATED = auto()
    INITIALIZING = auto()
    RUNNING = auto()
    STOPPING = auto()
    STOPPED = auto()
    FAILED = auto()