from agent import WorkerAgent

worker = WorkerAgent(
    name="AI-Agent-001",
    cpu=16,
    ram="64GB",
    gpu="RTX4090"
)

print(worker.register())
print(worker.start())
print(worker.assign_task("Liquidity Analysis"))
print(worker.complete_task())
print(worker.info())