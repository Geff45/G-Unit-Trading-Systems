from crypto.crypto_manager import CryptoManager
from kernel.communication.packet import SecurePacket


class PacketBuilder:

    def __init__(self):

        self.crypto = CryptoManager()

    def build(
        self,
        sender,
        receiver,
        message,
    ):

        digest = self.crypto.hash(message)

        signature = self.crypto.sign(message)

        encrypted = self.crypto.encrypt(message)

        return SecurePacket.create(
            sender=sender,
            receiver=receiver,
            payload=encrypted,
            digest=digest,
            signature=signature,
            encrypted=True,
        )