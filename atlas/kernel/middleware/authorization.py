from kernel.middleware.middleware import Middleware


class AuthorizationMiddleware(Middleware):

    def process(self, envelope):

        # Placeholder for authorization.
        # Future policy engine will determine
        # whether the sender may publish to the topic.

        return envelope
