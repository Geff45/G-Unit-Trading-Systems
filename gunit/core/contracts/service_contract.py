"""
Enterprise Service Contract

Every kernel service in G-UNIT implements this contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class ServiceContract(ABC):
    """Base contract implemented by every platform service."""

    @property
    @abstractmethod
    def service_id(self) -> str:
        """Return the unique service identifier."""

    @property
    @abstractmethod
    def service_name(self) -> str:
        """Return the display name."""

    @property
    @abstractmethod
    def version(self) -> str:
        """Return semantic version."""

    @abstractmethod
    def initialize(self) -> None:
        """Initialize the service."""

    @abstractmethod
    def configure(self) -> None:
        """Configure the service."""

    @abstractmethod
    def start(self) -> None:
        """Start the service."""

    @abstractmethod
    def stop(self) -> None:
        """Stop the service."""

    @abstractmethod
    def shutdown(self) -> None:
        """Shutdown the service."""