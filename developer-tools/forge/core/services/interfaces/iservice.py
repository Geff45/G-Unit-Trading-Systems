"""
Atlas Forge Service Interface

Defines the contract that every Atlas Forge service
must implement.

Version: 1.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from ..service_state import ServiceState


class IService(ABC):
    """
    Interface for all Atlas Forge services.
    """

    @property
    @abstractmethod
    def service_name(self) -> str:
        """Return the unique service name."""
        raise NotImplementedError

    @property
    @abstractmethod
    def version(self) -> str:
        """Return the service version."""
        raise NotImplementedError

    @property
    @abstractmethod
    def state(self) -> ServiceState:
        """Return the current service state."""
        raise NotImplementedError

    @abstractmethod
    def on_register(self) -> None:
        """Called when the service is registered."""
        raise NotImplementedError

    @abstractmethod
    def initialize(self) -> None:
        """Initialize the service."""
        raise NotImplementedError

    @abstractmethod
    def start(self) -> None:
        """Start the service."""
        raise NotImplementedError

    @abstractmethod
    def stop(self) -> None:
        """Stop the service."""
        raise NotImplementedError

    @abstractmethod
    def shutdown(self) -> None:
        """Shutdown the service."""
        raise NotImplementedError

    @abstractmethod
    def health_check(self) -> bool:
        """Return True if the service is healthy."""
        raise NotImplementedError