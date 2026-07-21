from task_queue import TaskQueue
from scheduler import Scheduler
from worker import Worker
from executor import Executor
from result_store import ResultStore



queue = TaskQueue()


scheduler = Scheduler(queue)


worker = Worker()


executor = Executor(
    scheduler,
    worker
)


store = ResultStore()



print(
    scheduler.submit(
        "Build G-Unit Trading System"
    )
)


result = executor.execute()


print(
    store.save(result)
)


print(
    store.all()
)