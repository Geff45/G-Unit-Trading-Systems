"""
Atlas Task Queue

Stores execution jobs.
"""


class TaskQueue:


    def __init__(self):

        self.tasks = []



    def add(self, task):

        self.tasks.append(task)

        return {
            "status":"queued",
            "task":task
        }



    def get_next(self):

        if self.tasks:

            return self.tasks.pop(0)

        return None



    def size(self):

        return len(self.tasks)