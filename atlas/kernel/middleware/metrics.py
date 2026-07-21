from kernel.middleware.middleware import Middleware


class MetricsMiddleware(Middleware):

    def __init__(self):

        self.counter = 0

    def process(self, envelope):

        self.counter += 1

        return envelope