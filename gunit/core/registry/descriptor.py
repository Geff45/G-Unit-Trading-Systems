"""
Service registration metadata.
"""

from dataclasses import dataclass
from typing import Any, Type

from gunit.core.container.lifetime import ServiceLifetime


@dataclass(slots=True)
class ServiceDescriptor:
    """
    Describes a registered service.
    """

    service_type: Type[Any]
    implementation_type: Type[Any]
    lifetime: ServiceLifetime

    instance: Any | None = None