"""
Service registry.

Stores available services in the platform.
"""

from typing import Any, Type

from gunit.core.registry.descriptor import ServiceDescriptor
from gunit.core.container.lifetime import ServiceLifetime


class ServiceRegistry:
    """
    Central storage for service registrations.
    """

    def __init__(self) -> None:
        self._services: dict[Type[Any], ServiceDescriptor] = {}

    def register(
        self,
        service_type: Type[Any],
        implementation_type: Type[Any],
        lifetime: ServiceLifetime,
    ) -> None:
        """
        Register a service.
        """

        descriptor = ServiceDescriptor(
            service_type=service_type,
            implementation_type=implementation_type,
            lifetime=lifetime,
        )

        self._services[service_type] = descriptor

    def get(
        self,
        service_type: Type[Any],
    ) -> ServiceDescriptor:

        return self._services[service_type]

    def contains(
        self,
        service_type: Type[Any],
    ) -> bool:

        return service_type in self._services