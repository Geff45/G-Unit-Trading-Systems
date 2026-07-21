"""
Atlas Worker Manager

Registers and manages WorkerAgent instances.
"""

from agent import WorkerAgent


class WorkerManager:
    def __init__(self):
        self._workers = {}

    def register(self, worker: WorkerAgent):
        self._workers[worker.name] = worker
        return {
            "status": "registered",
            "worker": worker.name,
        }

    def get(self, name):
        return self._workers.get(name)

    def list(self):
        return list(self._workers.keys())

    def remove(self, name):
        if name in self._workers:
            del self._workers[name]
            return {
                "status": "removed",
                "worker": name,
            }

        return {
            "status": "not_found",
            "worker": name,
        }

    def count(self):
        return len(self._workers)