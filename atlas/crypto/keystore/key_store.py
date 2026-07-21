from cryptography.fernet import Fernet


class KeyStore:

    _instance = None
    _keys = {}

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def generate(self, name):

        if name not in self._keys:
            self._keys[name] = Fernet.generate_key()

        return self._keys[name]

    def get(self, name):

        return self._keys.get(name)

    def exists(self, name):

        return name in self._keys

    def remove(self, name):

        if name in self._keys:
            del self._keys[name]

    def clear(self):

        self._keys.clear()

    def list_keys(self):

        return list(self._keys.keys())