from enum import Enum


class PluginState(Enum):
    CREATED = "created"
    LOADED = "loaded"
    INITIALIZED = "initialized"
    STARTED = "started"
    STOPPED = "stopped"
    FAILED = "failed"