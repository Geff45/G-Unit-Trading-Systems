class Publisher:

    def __init__(self):

        self.subscribers = []

    def subscribe(self, subscriber):

        self.subscribers.append(subscriber)

    def publish(self, event):

        results = []

        for subscriber in self.subscribers:

            results.append(
                subscriber.notify(event)
            )

        return results