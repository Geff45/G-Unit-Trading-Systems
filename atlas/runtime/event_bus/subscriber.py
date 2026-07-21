class Subscriber:

    def __init__(self, name):

        self.name = name

    def notify(self, event):

        return {
            "subscriber": self.name,
            "received": event.name
        }