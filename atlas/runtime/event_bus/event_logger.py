class EventLogger:

    def __init__(self):

        self.logs = []

    def log(self, event):

        self.logs.append(event.to_dict())

    def history(self):

        return self.logs