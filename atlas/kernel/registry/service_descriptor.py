from dataclasses import dataclass, field
from typing import List

from kernel.registry.service_state import ServiceState


@dataclass(slots=True)
class ServiceDescriptor:
    service_id: str
    name: str
    version: str

    state: ServiceState = ServiceState.CREATED

    dependencies: List[str] = field(default_factory=list)

    owner: str = "Atlas"

    trusted: bool = True

    heartbeat_ms: int = 1000