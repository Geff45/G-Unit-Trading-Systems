import time

from kernel.tasks.task_result import (
    TaskResult,
)


class LocalWorker:

    def execute(self, task):

        start = time.perf_counter()

        result = task.execute()

        elapsed = time.perf_counter() - start

        return TaskResult(

            success=result.success,

            message=result.message,

            data=result.data,

            execution_time=elapsed,
        )