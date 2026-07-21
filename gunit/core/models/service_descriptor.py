from dataclasses import dataclass

from platform.core.models.version import Version


@dataclass(frozen=True, slots=True)
class ServiceDescriptor:
    service_id: str
    service_name: str
    version: Version
    description: str = ""