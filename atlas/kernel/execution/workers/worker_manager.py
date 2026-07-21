from kernel.execution.workers.worker_pool import (
    WorkerPool,
)


class WorkerManager:

    def __init__(self):

        self.pool = WorkerPool()

    def execute(self, task):

        worker = self.pool.next_worker()

        return worker.execute(task)