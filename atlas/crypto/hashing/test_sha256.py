from crypto.hashing.sha256 import SHA256

message = "Atlas Kernel"

digest = SHA256.hash_text(message)

print("Hash:")
print(digest)

print()

print(
    SHA256.verify(
        message,
        digest,
    )
)

print(
    SHA256.verify(
        "Modified",
        digest,
    )
)