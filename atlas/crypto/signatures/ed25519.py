from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
)


class Ed25519Signer:

    _instance = None

    _private_key = None

    _public_key = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._private_key = Ed25519PrivateKey.generate()

            cls._public_key = cls._private_key.public_key()

        return cls._instance

    def sign(self, message: str) -> bytes:

        return self._private_key.sign(
            message.encode("utf-8")
        )

    def verify(
        self,
        message: str,
        signature: bytes,
    ) -> bool:

        try:

            self._public_key.verify(
                signature,
                message.encode("utf-8"),
            )

            return True

        except Exception:

            return False