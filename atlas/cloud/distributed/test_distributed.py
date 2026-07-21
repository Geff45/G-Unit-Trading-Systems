from job_queue import JobQueue
from job_manager import JobManager
from load_balancer import LoadBalancer



queue = JobQueue()

manager = JobManager()

balance = LoadBalancer()



print(
    queue.add(
        "Train Liquidity AI Model"
    )
)


worker = balance.select_worker(
    [
        "worker-001",
        "worker-002"
    ]
)


print(
    manager.submit(
        "Liquidity AI Training",
        worker
    )
)


print(
    queue.next()
)


print(
    manager.complete(
        "Liquidity AI Training"
    )
)


print(
    manager.all()
)