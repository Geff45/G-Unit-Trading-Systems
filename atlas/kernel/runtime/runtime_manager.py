from kernel.runtime.runtime_registry import (
    RuntimeRegistry,
)


class RuntimeManager:

    def __init__(self):

        self.registry = RuntimeRegistry()

    def register(self, runtime):

        runtime.initialize()

        self.registry.register(runtime)

    def execute(

        self,

        runtime_id,

        task,

    ):

        runtime = self.registry.get(runtime_id)

        return runtime.execute(task)