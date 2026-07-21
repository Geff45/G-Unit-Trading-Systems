"""
Service lifetime definitions.

Controls how long a registered service instance exists.
"""

from enum import Enum


class ServiceLifetime(str, Enum):
    """
    Defines service creation behaviour.
    """

    SINGLETON = "singleton"
    TRANSIENT = "transient"
    SCOPED = "scoped"