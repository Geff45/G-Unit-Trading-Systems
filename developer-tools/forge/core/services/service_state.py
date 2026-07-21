"""
Atlas Forge Service State

Version: 1.0.0
"""

from enum import Enum, auto


class ServiceState(Enum):

    NEW = auto()

    REGISTERED = auto()

    INITIALIZING = auto()

    RUNNING = auto()

    STOPPING = auto()

    STOPPED = auto()

    FAILED = auto()