from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .lifetime import ServiceLifetime


@dataclass(slots=True)
class ServiceDescriptor:
    """
    Describes a registered dependency-injection service.
    """

    service_type: type[Any]
    implementation_type: type[Any]
    lifetime: ServiceLifetime

    instance: Any | None = None
