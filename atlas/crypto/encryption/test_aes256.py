from crypto.encryption.aes256 import AES256

crypto = AES256()

message = "Atlas Secure Runtime"

cipher = crypto.encrypt(message)

print("Encrypted")
print(cipher)

print()

plain = crypto.decrypt(cipher)

print("Decrypted")

print(plain)