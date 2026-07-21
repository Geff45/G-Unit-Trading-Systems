import time

from kernel.tasks.task_result import (
    TaskResult,
)


class LocalWorker:
    """
    Executes a task on the local machine.
    """

    def execute(self, task):

        start = time.perf_counter()

        result = task.execute()

        end = time.perf_counter()

        return TaskResult(
            success=result.success,
            message=result.message,
            data=result.data,
            execution_time=end - start,
        )