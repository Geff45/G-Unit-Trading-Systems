from dataclasses import dataclass

from kernel.execution.controller_state import (
    ControllerState,
)


@dataclass
class ControllerDescriptor:

    controller_id: str

    name: str

    version: str

    state: ControllerState = ControllerState.CREATED