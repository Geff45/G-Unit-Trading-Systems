from kernel.middleware.middleware import Middleware


class CompressionMiddleware(Middleware):

    def process(self, envelope):

        # Compression will be enabled for
        # large payloads or remote transport.

        return envelope