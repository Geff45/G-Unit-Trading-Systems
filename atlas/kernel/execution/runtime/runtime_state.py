from enum import Enum


class RuntimeState(Enum):

    INITIALIZING = "initializing"

    READY = "ready"

    RUNNING = "running"

    BUSY = "busy"

    PAUSED = "paused"

    STOPPING = "stopping"

    STOPPED = "stopped"

    FAILED = "failed"