from enum import Enum


class CapabilityState(Enum):
    """
    Enterprise capability lifecycle.
    """

    CREATED = "created"

    INITIALIZED = "initialized"

    ACTIVE = "active"

    PAUSED = "paused"

    DISABLED = "disabled"

    FAILED = "failed"

    SHUTDOWN = "shutdown"