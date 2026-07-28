"""
G-UNIT Platform Kernel

Service Container

Central dependency injection container.
"""

from __future__ import annotations

from typing import Any

from .service_descriptor import ServiceDescriptor


class ServiceContainer:
    """
    Dependency Injection container.

    Responsible for registering,
    resolving and managing services.
    """

    def __init__(self) -> None:
        self._descriptors: dict[str, ServiceDescriptor] = {}
        self._instances: dict[str, Any] = {}

    def register(
        self,
        descriptor: ServiceDescriptor,
    ) -> None:
        """
        Register a service descriptor.
        """

        identity = descriptor.name

        if identity in self._descriptors:
            raise ValueError(
                f"Service already registered: {identity}"
            )

        self._descriptors[identity] = descriptor

    def contains(
        self,
        name: str,
    ) -> bool:
        """
        Returns True if a service has been registered.
        """

        return name in self._descriptors

    def resolve(
        self,
        name: str,
    ) -> Any:
        """
        Resolve a service instance.
        """

        if name in self._instances:
            return self._instances[name]

        if name not in self._descriptors:
            raise LookupError(
                f"Service not found: {name}"
            )

        descriptor = self._descriptors[name]

        module = __import__(
            descriptor.module,
            fromlist=[descriptor.service_class],
        )

        service_class = getattr(
            module,
            descriptor.service_class,
        )

        instance = service_class()

        self._instances[name] = instance

        return instance

    def remove(
        self,
        name: str,
    ) -> None:
        """
        Remove a registered service.
        """

        self._descriptors.pop(
            name,
            None,
        )

        self._instances.pop(
            name,
            None,
        )

    def clear(self) -> None:
        """
        Remove all registered services.
        """

        self._descriptors.clear()
        self._instances.clear()

    def list_services(self) -> list[str]:
        """
        Return registered service names.
        """

        return list(self._descriptors.keys())

    @property
    def descriptors(self) -> dict[str, ServiceDescriptor]:
        """
        Registered service descriptors.
        """

        return self._descriptors

    @property
    def instances(self) -> dict[str, Any]:
        """
        Cached service instances.
        """

        return self._instances