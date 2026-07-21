from crypto.signatures.ed25519 import Ed25519Signer

signer = Ed25519Signer()

message = "Atlas Decision Council"

signature = signer.sign(message)

print("Signature Length:")

print(len(signature))

print()

print("Valid:")

print(
    signer.verify(
        message,
        signature,
    )
)

print()

print("Tampered:")

print(
    signer.verify(
        "Modified Message",
        signature,
    )
)