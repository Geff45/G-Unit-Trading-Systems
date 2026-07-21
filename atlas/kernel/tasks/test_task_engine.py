from kernel.tasks.task import Task

from kernel.tasks.task_descriptor import (
    TaskDescriptor,
)

from kernel.tasks.task_result import (
    TaskResult,
)

from kernel.tasks.task_scheduler import (
    TaskScheduler,
)


class DownloadCalendarTask(Task):

    def execute(self):

        print("Downloading Calendar...")

        return TaskResult(
            True,
            "Calendar Updated",
        )


scheduler = TaskScheduler()

task = DownloadCalendarTask(

    TaskDescriptor(

        task_id="calendar",

        name="Download Calendar",

        workflow="Research",

        capability="Economic Calendar",

        priority=1,
    )

)

scheduler.submit(task)

scheduler.run()