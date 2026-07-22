"""
Base service definition.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class Service(ABC):
    """
    Base class for all services.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique service name.
        """

    @abstractmethod
    def start(self) -> None:
        """
        Start service.
        """

    @abstractmethod
    def stop(self) -> None:
        """
        Stop service.
        """

    @property
    @abstractmethod
    def running(self) -> bool:
        """
        True if service is active.
        """