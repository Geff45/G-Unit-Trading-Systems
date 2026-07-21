from kernel.tasks.priority_queue import (
    PriorityTaskQueue,
)

from kernel.tasks.worker_manager import (
    WorkerManager,
)


class TaskScheduler:
    """
    Enterprise Task Scheduler.
    """

    def __init__(self):

        self.queue = PriorityTaskQueue()

        self.workers = WorkerManager()

    def submit(self, task):

        self.queue.push(
            task.descriptor.priority,
            task,
        )

    def run(self):

        while not self.queue.empty():

            task = self.queue.pop()

            result = self.workers.execute(
                task
            )

            print(
                f"[TASK] {task.descriptor.name}"
            )

            print(
                f"Status : {result.success}"
            )

            print(
                f"Message: {result.message}"
            )

            print(
                f"Time   : {result.execution_time:.4f}s"
            )

            print()