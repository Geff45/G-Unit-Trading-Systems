from datetime import timedelta

from kernel.scheduler.clock import AtlasClock
from kernel.scheduler.task import ScheduledTask


class AtlasScheduler:

    def __init__(self):

        self.clock = AtlasClock()

        self.tasks = []

    def add_task(

        self,

        name,

        seconds,

        callback,

    ):

        self.tasks.append(

            ScheduledTask(

                name=name,

                interval=timedelta(seconds=seconds),

                callback=callback,

            )

        )

    def run_once(self):

        print("Scheduler:", self.clock.now())

        for task in self.tasks:

            if task.enabled:

                task.callback()