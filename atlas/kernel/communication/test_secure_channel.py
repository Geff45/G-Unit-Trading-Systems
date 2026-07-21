from kernel.communication.secure_channel import SecureChannel

channel = SecureChannel()

packet = channel.send(
    sender="trend_engine",
    receiver="risk_engine",
    message="BUY EURUSD"
)

print("Packet Created")

print(packet.packet_id)

print()

print("Receiving...")

message = channel.receive(packet)

print(message)