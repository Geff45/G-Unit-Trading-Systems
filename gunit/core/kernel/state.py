"""
G-UNIT Kernel state definitions.
"""

from enum import Enum


class KernelState(str, Enum):
    """
    Current state of the kernel.
    """

    CREATED = "created"
    INITIALIZING = "initializing"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"
    FAILED = "failed"