from kernel.communication.packet_builder import PacketBuilder
from crypto.crypto_manager import CryptoManager


class SecureChannel:

    def __init__(self):

        self.builder = PacketBuilder()
        self.crypto = CryptoManager()

    def send(
        self,
        sender,
        receiver,
        message,
    ):

        return self.builder.build(
            sender,
            receiver,
            message,
        )

    def receive(
        self,
        packet,
    ):

        message = self.crypto.decrypt(
            packet.payload
        )

        if not self.crypto.verify_hash(
            message,
            packet.digest,
        ):
            raise ValueError(
                "Packet integrity failed."
            )

        if not self.crypto.verify_signature(
            message,
            packet.signature,
        ):
            raise ValueError(
                "Packet signature invalid."
            )

        return message