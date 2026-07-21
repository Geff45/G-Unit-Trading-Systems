from kernel.service_bus.envelope import Envelope


class MiddlewarePipeline:
    """
    Enterprise middleware execution pipeline.
    """

    def __init__(self):

        self._middleware = []

    def add(self, middleware):

        self._middleware.append(
            middleware
        )

    def process(
        self,
        envelope: Envelope,
    ) -> Envelope:

        for middleware in self._middleware:

            envelope = middleware.process(
                envelope
            )

        return envelope