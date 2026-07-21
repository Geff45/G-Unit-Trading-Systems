"""
Atlas Base Worker
"""

from core.base.component import BaseComponent


class BaseWorker(BaseComponent):

    def __init__(self, name):

        super().__init__(name)

        self.current_task = None

    def assign(self, task):

        self.current_task = task

        return {
            "worker": self.name,
            "task": task
        }