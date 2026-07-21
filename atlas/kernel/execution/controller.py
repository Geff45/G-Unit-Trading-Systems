from kernel.execution.controller_state import (
    ControllerState,
)

from kernel.execution.manager.runtime_manager import (
    RuntimeManager,
)

from kernel.execution.workers.worker_manager import (
    WorkerManager,
)


class ExecutionController:
    """
    Enterprise execution subsystem.

    Owns every execution component.
    """

    def __init__(self, descriptor):

        self.descriptor = descriptor

        self.runtime_manager = RuntimeManager()

        self.worker_manager = WorkerManager()

    def initialize(self):

        self.descriptor.state = (
            ControllerState.READY
        )

        print()

        print("Execution Controller Ready")

    def start(self):

        self.descriptor.state = (
            ControllerState.RUNNING
        )

        print("Execution Started")

    def stop(self):

        self.descriptor.state = (
            ControllerState.STOPPED
        )

        print("Execution Stopped")