from dataclasses import dataclass

from kernel.runtime.runtime_state import RuntimeState


@dataclass
class RuntimeDescriptor:

    runtime_id: str

    name: str

    platform: str

    version: str

    max_workers: int

    state: RuntimeState = RuntimeState.INITIALIZING