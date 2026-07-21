from kernel.middleware.middleware import Middleware


class TracingMiddleware(Middleware):

    def process(self, envelope):

        envelope.metadata[
            "trace"
        ] = envelope.trace_id

        return envelope