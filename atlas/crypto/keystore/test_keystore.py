from crypto.keystore.key_store import KeyStore

store = KeyStore()

store.generate("runtime")

store.generate("event_bus")

store.generate("broker")

print(store.list_keys())

print(store.exists("runtime"))

print(store.exists("scheduler"))