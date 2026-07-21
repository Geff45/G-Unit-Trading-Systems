from dataclasses import dataclass, field

from kernel.capabilities.capability_state import CapabilityState


@dataclass
class CapabilityDescriptor:
    """
    Metadata describing an Atlas capability.
    """

    capability_id: str

    name: str

    version: str

    plugin: str

    description: str

    state: CapabilityState = CapabilityState.CREATED

    tasks: list[str] = field(default_factory=list)

    dependencies: list[str] = field(default_factory=list)