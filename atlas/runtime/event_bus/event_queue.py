class EventQueue:

    def __init__(self):

        self.queue = []

    def push(self, event):

        self.queue.append(event)

        return {
            "status": "queued",
            "event": event.name
        }

    def pop(self):

        if self.queue:
            return self.queue.pop(0)

        return None

    def size(self):

        return len(self.queue)