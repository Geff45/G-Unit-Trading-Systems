"""
Atlas AI Operating System
=========================

Module:
    Lifecycle State

Purpose:
    Defines every valid lifecycle state that an Atlas
    service can occupy.

Author:
    Atlas Development Team

Version:
    1.0.0
"""

from enum import Enum, auto


class LifecycleState(Enum):
    """
    Official lifecycle states for every Atlas component.
    """

    CREATED = auto()

    INITIALIZING = auto()

    INITIALIZED = auto()

    CONFIGURING = auto()

    READY = auto()

    STARTING = auto()

    RUNNING = auto()

    PAUSING = auto()

    PAUSED = auto()

    RESUMING = auto()

    STOPPING = auto()

    STOPPED = auto()

    FAILED = auto()

    SHUTTING_DOWN = auto()

    SHUTDOWN = auto()

    UNKNOWN = auto()