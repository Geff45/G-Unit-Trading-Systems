"""
Module state.
"""

from enum import Enum


class ModuleState(Enum):
    CREATED = "created"
    LOADED = "loaded"
    STARTED = "started"
    STOPPED = "stopped"