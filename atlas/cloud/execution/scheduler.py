"""
Atlas Scheduler

Controls task scheduling.
"""


class Scheduler:


    def __init__(self, queue):

        self.queue = queue



    def submit(self, task):

        return self.queue.add(task)



    def next_task(self):

        return self.queue.get_next()