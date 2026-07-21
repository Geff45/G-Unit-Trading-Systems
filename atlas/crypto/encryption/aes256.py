import base64
import os

from cryptography.fernet import Fernet


class AES256:

    def __init__(self, key=None):

        self.key = key or Fernet.generate_key()

        self.cipher = Fernet(self.key)

    def encrypt(self, text: str) -> str:

        encrypted = self.cipher.encrypt(
            text.encode()
        )

        return encrypted.decode()

    def decrypt(self, token: str) -> str:

        decrypted = self.cipher.decrypt(
            token.encode()
        )

        return decrypted.decode()

    def export_key(self):

        return self.key.decode()