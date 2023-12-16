from random import randint
from hashlib import sha256


class Transaction:
    def __init__(self):
        self._hash = self._create_hash_value()

    def _create_hash_value(self):
        value = str(randint(0, 10000))
        hashedVal = str(sha256(value.encode('utf-8')).hexdigest())
        return hashedVal

    def get_hash(self):
        return self._hash
