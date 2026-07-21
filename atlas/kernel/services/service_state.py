from enum import Enum


class ServiceState(Enum):

    CREATED = "created"

    LOADING = "loading"

    RUNNING = "running"

    PAUSED = "paused"

    STOPPING = "stopping"

    STOPPED = "stopped"

    FAILED = "failed"