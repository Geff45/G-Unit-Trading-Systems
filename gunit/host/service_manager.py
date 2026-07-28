"""
Hosted service manager.
"""

from __future__ import annotations

from .hosted_service import HostedService


class HostedServiceManager:
    """
    Starts and stops hosted services.
    """

    def __init__(self) -> None:
        self._services: list[HostedService] = []

    @property
    def services(self) -> list[HostedService]:
        return self._services

    def add(
        self,
        service: HostedService,
    ) -> None:
        """
        Registers a hosted service.
        """

        if service not in self._services:
            self._services.append(service)

    def remove(
        self,
        service: HostedService,
    ) -> None:
        """
        Removes a hosted service.
        """

        if service in self._services:
            self._services.remove(service)

    def clear(self) -> None:
        """
        Removes all hosted services.
        """

        self._services.clear()

    def start_all(self) -> None:
        """
        Starts every hosted service.
        """

        for service in self._services:
            service.start()

    def stop_all(self) -> None:
        """
        Stops every hosted service.
        """

        for service in reversed(self._services):
            service.stop()