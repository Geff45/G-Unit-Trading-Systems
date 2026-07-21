from kernel.tasks.local_worker import (
    LocalWorker,
)


class WorkerManager:
    """
    Routes tasks to execution workers.
    """

    def __init__(self):

        self.local = LocalWorker()

    def execute(self, task):

        return self.local.execute(task)