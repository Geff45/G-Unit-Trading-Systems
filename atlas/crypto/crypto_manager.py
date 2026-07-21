from crypto.hashing.sha256 import SHA256
from crypto.encryption.aes256 import AES256
from crypto.signatures.ed25519 import Ed25519Signer
from crypto.keystore.key_store import KeyStore


class CryptoManager:

    def __init__(self):

        # Shared enterprise KeyStore
        self.keys = KeyStore()

        # Generate the Atlas runtime key only once
        if not self.keys.exists("atlas"):
            self.keys.generate("atlas")

        # Load the shared encryption key
        self.encryptor = AES256(
            self.keys.get("atlas")
        )

        # Shared signer
        self.signer = Ed25519Signer()

    # ==================================================
    # HASHING
    # ==================================================

    def hash(self, text: str):

        return SHA256.hash_text(text)

    def verify_hash(self, text: str, digest: str):

        return SHA256.verify(text, digest)

    # ==================================================
    # ENCRYPTION
    # ==================================================

    def encrypt(self, text: str):

        return self.encryptor.encrypt(text)

    def decrypt(self, token: str):

        return self.encryptor.decrypt(token)

    # ==================================================
    # DIGITAL SIGNATURES
    # ==================================================

    def sign(self, message: str):

        return self.signer.sign(message)

    def verify_signature(
        self,
        message: str,
        signature: bytes,
    ):

        return self.signer.verify(
            message,
            signature,
        )

    # ==================================================
    # KEY MANAGEMENT
    # ==================================================

    def list_keys(self):

        return self.keys.list_keys()

    def key_exists(self, name: str):

        return self.keys.exists(name)

    def generate_key(self, name: str):

        return self.keys.generate(name)

    def get_key(self, name: str):

        return self.keys.get(name)

    def remove_key(self, name: str):

        self.keys.remove(name)