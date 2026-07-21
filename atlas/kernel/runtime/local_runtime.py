from kernel.runtime.runtime import Runtime

from kernel.runtime.runtime_state import RuntimeState


class LocalRuntime(Runtime):

    def initialize(self):

        self.descriptor.state = RuntimeState.READY

        print()

        print("Local Runtime Ready")

    def execute(self, task):

        print()

        print(

            f"Executing {task.descriptor.name}"

        )

        return task.execute()