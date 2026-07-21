from kernel.middleware.middleware import Middleware


class EncryptionMiddleware(Middleware):

    def process(self, envelope):

        # This will later integrate with the
        # CryptoManager for automatic encryption
        # of inter-node messages.

        return envelope