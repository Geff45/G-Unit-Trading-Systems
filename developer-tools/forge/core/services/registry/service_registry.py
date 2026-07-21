"""
Atlas Forge Service Registry

Stores and manages registered services.

Version: 1.0.0
"""

from __future__ import annotations

from typing import Dict, List

from ..interfaces import IService


class ServiceRegistry:
    """
    Registry for all Forge services.
    """

    def __init__(self) -> None:
        self._services: Dict[str, IService] = {}

    def register(self, service: IService) -> None:
        """
        Register a service.
        """
        name = service.service_name

        if name in self._services:
            raise ValueError(
                f"Service '{name}' is already registered."
            )

        service.on_register()
        self._services[name] = service

    def unregister(self, service_name: str) -> None:
        """
        Remove a registered service.
        """
        self._services.pop(service_name, None)

    def get(self, service_name: str) -> IService:
        """
        Retrieve a registered service.
        """
        try:
            return self._services[service_name]
        except KeyError as exc:
            raise KeyError(
                f"Unknown service: '{service_name}'"
            ) from exc

    def exists(self, service_name: str) -> bool:
        """
        Check whether a service exists.
        """
        return service_name in self._services

    def list_services(self) -> List[str]:
        """
        Return all registered service names.
        """
        return sorted(self._services.keys())

    def count(self) -> int:
        """
        Return the number of registered services.
        """
        return len(self._services)

    def clear(self) -> None:
        """
        Remove all services.
        """
        self._services.clear()