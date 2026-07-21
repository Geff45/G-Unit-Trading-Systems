from kernel.middleware.middleware import Middleware


class AuthenticationMiddleware(Middleware):

    def process(self, envelope):

        # Placeholder for authentication.
        # Later this will validate node identities,
        # service certificates, or API tokens.

        return envelope