"""
G-UNIT Dependency Injection Container.
"""

from typing import Any, Type

from gunit.core.container.lifetime import ServiceLifetime
from gunit.core.registry.service_registry import ServiceRegistry


class ServiceContainer:
    """
    Creates and manages platform services.
    """

    def __init__(self) -> None:
        self._registry = ServiceRegistry()

    def register(
        self,
        service_type: Type[Any],
        implementation_type: Type[Any],
        lifetime: ServiceLifetime = ServiceLifetime.TRANSIENT,
    ) -> None:

        self._registry.register(
            service_type,
            implementation_type,
            lifetime,
        )

    def resolve(
        self,
        service_type: Type[Any],
    ) -> Any:

        descriptor = self._registry.get(service_type)

        if descriptor.lifetime == ServiceLifetime.SINGLETON:

            if descriptor.instance is None:
                descriptor.instance = (
                    descriptor.implementation_type()
                )

            return descriptor.instance

        return descriptor.implementation_type()