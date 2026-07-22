"""
Service registry.
"""

from __future__ import annotations

from typing import Dict

from .service import Service


class ServiceRegistry:
    """
    Stores every system service.
    """

    def __init__(self) -> None:
        self._services: Dict[str, Service] = {}

    def register(self, service: Service) -> None:
        """
        Register a service.
        """
        self._services[service.name] = service

    def unregister(self, name: str) -> None:
        """
        Remove a service.
        """
        self._services.pop(name, None)

    def get(self, name: str) -> Service:
        """
        Retrieve a service.
        """
        return self._services[name]

    def exists(self, name: str) -> bool:
        """
        Check if service exists.
        """
        return name in self._services

    def all(self) -> dict[str, Service]:
        """
        Return all services.
        """
        return dict(self._services)

    def clear(self) -> None:
        """
        Remove all services.
        """
        self._services.clear()

    def __len__(self) -> int:
        return len(self._services)