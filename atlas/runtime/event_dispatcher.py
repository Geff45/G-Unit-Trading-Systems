class EventDispatcher:

    def __init__(self):
        self.events = []

    def dispatch(self, event):

        self.events.append(event)

        return {
            "status": "dispatched",
            "event": event
        }

    def history(self):
        return self.events