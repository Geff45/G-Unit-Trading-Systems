from kernel.tasks.task import Task


class TaskRegistry:
    """
    Enterprise task registry.
    """

    def __init__(self):

        self._tasks = {}

    def register(self, task: Task):

        self._tasks[
            task.descriptor.task_id
        ] = task

    def get(self, task_id):

        return self._tasks.get(task_id)

    def exists(self, task_id):

        return task_id in self._tasks

    def all(self):

        return list(self._tasks.values())

    def count(self):

        return len(self._tasks)