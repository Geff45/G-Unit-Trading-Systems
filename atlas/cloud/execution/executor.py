"""
Atlas Executor

Connects scheduler and workers.
"""


class Executor:


    def __init__(self, scheduler, worker):

        self.scheduler = scheduler

        self.worker = worker



    def execute(self):

        task = self.scheduler.next_task()


        if task is None:

            return {

                "status":"no_tasks"

            }


        return self.worker.run(task)