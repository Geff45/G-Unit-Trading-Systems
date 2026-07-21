"""
Atlas Forge Service Container

Responsible for registering and managing
core Forge services.

Version: 1.0.0
"""

from typing import Any, Dict


class ServiceContainer:
    """
    Central dependency container for Atlas Forge.

    Services are registered by name and retrieved
    by other Forge components.
    """

    def __init__(self):
        self._services: Dict[str, Any] = {}

    def register(self, name: str, service: Any) -> None:
        """
        Register a service.

        Args:
            name: Unique service identifier.
            service: Service instance.
        """

        if name in self._services:
            raise ValueError(
                f"Service '{name}' is already registered."
            )

        self._services[name] = service


    def get(self, name: str) -> Any:
        """
        Retrieve a registered service.
        """

        if name not in self._services:
            raise KeyError(
                f"Service '{name}' was not found."
            )

        return self._services[name]


    def has(self, name: str) -> bool:
        """
        Check whether a service exists.
        """

        return name in self._services


    def remove(self, name: str) -> None:
        """
        Remove a service.
        """

        if name in self._services:
            del self._services[name]


    def clear(self) -> None:
        """
        Remove all registered services.
        """

        self._services.clear()


    def list_services(self) -> list[str]:
        """
        Return all registered services.
        """

        return list(self._services.keys())