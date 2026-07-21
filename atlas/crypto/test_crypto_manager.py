from crypto.crypto_manager import CryptoManager

crypto = CryptoManager()

message = "Atlas Kernel"

print("HASH")

digest = crypto.hash(message)

print(digest)

print()

print("VERIFY HASH")

print(
    crypto.verify_hash(
        message,
        digest,
    )
)

print()

print("ENCRYPT")

cipher = crypto.encrypt(message)

print(cipher)

print()

print("DECRYPT")

print(
    crypto.decrypt(
        cipher,
    )
)

print()

print("SIGN")

signature = crypto.sign(message)

print(len(signature))

print()

print("VERIFY SIGNATURE")

print(
    crypto.verify_signature(
        message,
        signature,
    )
)