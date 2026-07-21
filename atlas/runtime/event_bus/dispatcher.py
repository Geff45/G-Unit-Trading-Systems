from publisher import Publisher
from event_queue import EventQueue
from event_logger import EventLogger


class Dispatcher:

    def __init__(self):

        self.publisher = Publisher()
        self.queue = EventQueue()
        self.logger = EventLogger()

    def register(self, subscriber):

        self.publisher.subscribe(subscriber)

    def dispatch(self, event):

        self.queue.push(event)

        self.logger.log(event)

        return self.publisher.publish(event)