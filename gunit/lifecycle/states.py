"""
G-UNIT Platform Kernel

Lifecycle States
"""

from enum import Enum



class ServiceState(Enum):
    """
    Service lifecycle states.
    """


    CREATED = "created"

    INITIALIZED = "initialized"

    STARTING = "starting"

    RUNNING = "running"

    STOPPING = "stopping"

    STOPPED = "stopped"

    FAILED = "failed"