"""
Hosted service contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class HostedService(ABC):
    """
    Base class for services managed by the Host.
    """

    @abstractmethod
    def start(self) -> None:
        """
        Starts the service.
        """

    @abstractmethod
    def stop(self) -> None:
        """
        Stops the service.
        """