from enum import Enum


class LifecycleState(Enum):
    """
    Represents lifecycle states of G-Unit components.
    """

    CREATED = "created"

    INITIALIZING = "initializing"

    READY = "ready"

    RUNNING = "running"

    STOPPING = "stopping"

    STOPPED = "stopped"

    FAILED = "failed"