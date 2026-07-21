from kernel.runtime.local_runtime import (
    LocalRuntime,
)

from kernel.runtime.runtime_descriptor import (
    RuntimeDescriptor,
)

from kernel.runtime.runtime_manager import (
    RuntimeManager,
)

from kernel.tasks.task import Task

from kernel.tasks.task_descriptor import (
    TaskDescriptor,
)

from kernel.tasks.task_result import (
    TaskResult,
)


class CalendarTask(Task):

    def execute(self):

        print("Downloading Calendar...")

        return TaskResult(

            True,

            "Calendar Updated"

        )


manager = RuntimeManager()

runtime = LocalRuntime(

    RuntimeDescriptor(

        runtime_id="local",

        name="Local Runtime",

        platform="Windows",

        version="1.0",

        max_workers=8,

    )

)

manager.register(runtime)

task = CalendarTask(

    TaskDescriptor(

        task_id="calendar",

        name="Calendar Download",

        workflow="Research",

        capability="Calendar",

    )

)

result = manager.execute(

    "local",

    task,

)

print()

print("Success :", result.success)

print("Message :", result.message)