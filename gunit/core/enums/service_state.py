from enum import Enum


class ServiceState(str, Enum):
    CREATED = "created"
    INITIALIZED = "initialized"
    CONFIGURED = "configured"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"
    FAILED = "failed"