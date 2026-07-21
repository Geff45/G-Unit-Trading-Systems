from dataclasses import dataclass
from typing import Any

from kernel.runtime.lifetime import ServiceLifetime


@dataclass(slots=True)
class ServiceRegistration:

    interface: type

    implementation: type

    lifetime: ServiceLifetime

    instance: Any = None