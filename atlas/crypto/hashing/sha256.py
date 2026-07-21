import hashlib


class SHA256:

    @staticmethod
    def hash_text(text: str) -> str:
        return hashlib.sha256(
            text.encode("utf-8")
        ).hexdigest()

    @staticmethod
    def verify(text: str, digest: str) -> bool:
        return (
            SHA256.hash_text(text)
            == digest
        )