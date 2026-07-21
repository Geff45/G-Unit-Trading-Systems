from kernel.middleware.middleware import Middleware


class LoggingMiddleware(Middleware):

    def process(self, envelope):

        print(
            f"[BUS] "
            f"{envelope.sender} "
            f"-> "
            f"{envelope.message.topic}"
        )

        return envelope