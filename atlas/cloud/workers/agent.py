"""
Atlas Cloud Worker Agent

Base class for every Atlas AI worker.

Examples:
    - Liquidity AI
    - Order Flow AI
    - Risk Engine
    - MT4 Execution Agent
    - Backtesting Worker
"""

from datetime import datetime


class WorkerAgent:

    def __init__(
        self,
        name,
        cpu=2,
        ram="4GB",
        gpu=None,
    ):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu

        self.status = "idle"
        self.current_task = None
        self.started = datetime.now()

    def register(self):
        self.status = "registered"

        return {
            "worker": self.name,
            "status": self.status,
        }

    def start(self):
        self.status = "running"

        return {
            "worker": self.name,
            "status": self.status,
        }

    def stop(self):
        self.status = "stopped"

        return {
            "worker": self.name,
            "status": self.status,
        }

    def assign_task(self, task):

        self.current_task = task
        self.status = "busy"

        return {
            "worker": self.name,
            "task": task,
            "status": self.status,
        }

    def complete_task(self):

        finished = self.current_task

        self.current_task = None
        self.status = "running"

        return {
            "worker": self.name,
            "task": finished,
            "status": "completed",
        }

    def info(self):

        return {
            "name": self.name,
            "cpu": self.cpu,
            "ram": self.ram,
            "gpu": self.gpu,
            "status": self.status,
        }