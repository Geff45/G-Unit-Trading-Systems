from kernel.execution.workers.local_worker import (
    LocalWorker,
)


class WorkerPool:

    def __init__(self, size=4):

        self.size = size

        self.workers = [

            LocalWorker()

            for _ in range(size)
        ]

        self.index = 0

    def next_worker(self):

        worker = self.workers[self.index]

        self.index = (

            self.index + 1

        ) % self.size

        return worker