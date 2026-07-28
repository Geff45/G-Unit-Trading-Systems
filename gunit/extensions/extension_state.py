from enum import Enum


class ExtensionState(Enum):
    CREATED = "created"
    REGISTERED = "registered"
    INITIALIZED = "initialized"
    ENABLED = "enabled"
    DISABLED = "disabled"
    FAILED = "failed"


__all__ = ["ExtensionState"]
