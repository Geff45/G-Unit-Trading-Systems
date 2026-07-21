from kernel.middleware.middleware import Middleware


class ValidationMiddleware(Middleware):
    """
    Validates message envelopes before
    they enter the Service Bus.
    """

    def process(self, envelope):

        if envelope is None:
            raise ValueError(
                "Envelope cannot be None."
            )

        if envelope.message is None:
            raise ValueError(
                "Message missing."
            )

        if not envelope.message.topic:
            raise ValueError(
                "Topic missing."
            )

        return envelope