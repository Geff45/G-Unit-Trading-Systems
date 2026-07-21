from agent import WorkerAgent
from worker_manager import WorkerManager

manager = WorkerManager()

worker = WorkerAgent(
    name="AI-Agent-001",
    cpu=16,
    ram="64GB",
    gpu="RTX4090",
)

print(manager.register(worker))

print(worker.start())

print(worker.assign_task("Liquidity Analysis"))

print(worker.complete_task())

print(manager.list())

print(manager.count())

print(manager.remove("AI-Agent-001"))

print(manager.list())