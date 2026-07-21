from dataclasses import dataclass, field

from kernel.services.service_state import ServiceState


@dataclass
class ServiceDescriptor:

    service_id: str

    name: str

    version: str

    state: ServiceState = ServiceState.CREATED

    dependencies: list[str] = field(
        default_factory=list
    )

    plugins: list[str] = field(
        default_factory=list
    )