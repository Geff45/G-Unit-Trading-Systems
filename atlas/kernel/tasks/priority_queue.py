import heapq


class PriorityTaskQueue:
    """
    Enterprise priority queue.
    """

    def __init__(self):

        self._queue = []

    def push(self, priority, task):

        heapq.heappush(
            self._queue,
            (priority, task),
        )

    def pop(self):

        if not self._queue:

            return None

        return heapq.heappop(
            self._queue
        )[1]

    def empty(self):

        return len(self._queue) == 0

    def size(self):

        return len(self._queue)