from __future__ import annotations

from typing import Any, Callable

from .descriptor import ServiceDescriptor
from .lifetime import ServiceLifetime
from .provider import ServiceProvider


class ServiceCollection:
    """
    Collects service registrations before building a provider.
    """

    def __init__(self) -> None:
        self._descriptors: dict[type, ServiceDescriptor] = {}

    def add(
        self,
        service_type: type,
        implementation_type: type,
        lifetime: ServiceLifetime = ServiceLifetime.TRANSIENT,
    ) -> "ServiceCollection":
        """
        Register a service implementation type.
        """

        self._descriptors[service_type] = ServiceDescriptor(
            service_type=service_type,
            implementation_type=implementation_type,
            lifetime=lifetime,
        )

        return self

    def add_factory(
        self,
        service_type: type,
        factory: Callable[..., Any],
        lifetime: ServiceLifetime = ServiceLifetime.TRANSIENT,
    ) -> "ServiceCollection":
        """
        Register a service factory.

        The factory is stored as the implementation callable and is
        invoked by ServiceProvider during resolution.
        """

        self._descriptors[service_type] = ServiceDescriptor(
            service_type=service_type,
            implementation_type=factory,
            lifetime=lifetime,
        )

        return self

    def contains(self, service_type: type) -> bool:
        """
        Return True when a service is registered.
        """

        return service_type in self._descriptors

    def get_descriptor(
        self,
        service_type: type,
    ) -> ServiceDescriptor:
        """
        Return registration metadata for a service.
        """

        return self._descriptors[service_type]

    def build_provider(self) -> ServiceProvider:
        """
        Build a provider from the current registrations.
        """

        return ServiceProvider(
            self._descriptors
        )
