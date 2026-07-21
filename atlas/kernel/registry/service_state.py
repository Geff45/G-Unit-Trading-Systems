from enum import Enum


class ServiceState(Enum):
    CREATED = "created"
    REGISTERED = "registered"
    INITIALIZED = "initialized"
    STARTED = "started"
    RUNNING = "running"
    PAUSED = "paused"
    STOPPED = "stopped"
    FAILED = "failed"
    DESTROYED = "destroyed"