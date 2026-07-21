from datetime import datetime


class Event:

    def __init__(self, name, payload=None):

        self.name = name
        self.payload = payload or {}
        self.timestamp = datetime.now()

    def to_dict(self):

        return {
            "name": self.name,
            "payload": self.payload,
            "timestamp": str(self.timestamp)
        }