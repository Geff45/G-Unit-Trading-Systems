from enum import Enum


class RuntimeState(Enum):

    INITIALIZING = "initializing"

    READY = "ready"

    BUSY = "busy"

    PAUSED = "paused"

    OFFLINE = "offline"

    FAILED = "failed"