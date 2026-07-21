"""
Atlas Forge Service Manager

Controls the lifecycle of all registered services.

Version: 2.0.0
"""

from __future__ import annotations

from typing import List

from ..interfaces import IService
from ..registry import ServiceRegistry


class ServiceManager:
    """
    Manages the lifecycle of all Forge services.
    """

    def __init__(self) -> None:

        self._registry = ServiceRegistry()

        self._startup_order: List[str] = []

    @property
    def registry(self) -> ServiceRegistry:
        return self._registry

    def register(self, service: IService) -> None:
        """
        Register a new service.
        """

        self._registry.register(service)

        self._startup_order.append(
            service.service_name
        )

    def unregister(self, service_name: str) -> None:
        """
        Remove a registered service.
        """

        self._registry.unregister(service_name)

        if service_name in self._startup_order:
            self._startup_order.remove(service_name)

    def initialize_all(self) -> None:
        """
        Initialize every registered service.
        """

        for name in self._startup_order:

            service = self._registry.get(name)

            service.initialize()

    def start_all(self) -> None:
        """
        Start every registered service.
        """

        for name in self._startup_order:

            service = self._registry.get(name)

            service.start()

    def stop_all(self) -> None:
        """
        Stop services in reverse order.
        """

        for name in reversed(self._startup_order):

            service = self._registry.get(name)

            service.stop()

    def shutdown_all(self) -> None:
        """
        Shutdown services in reverse order.
        """

        for name in reversed(self._startup_order):

            service = self._registry.get(name)

            service.shutdown()

    def get(self, service_name: str) -> IService:

        return self._registry.get(service_name)

    def exists(self, service_name: str) -> bool:

        return self._registry.exists(service_name)

    def list_services(self) -> List[str]:

        return self._registry.list_services()

    def count(self) -> int:

        return self._registry.count()