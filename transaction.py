from random import randint
from hashlib import sha256


class Transaction:  # generates and returns 1 tx at a time, which gets bundled, hashed and stored in Block
    def __init__(self):
        self._transaction = self._generateTransaction()

    @staticmethod
    def _generateTransaction():
        value = str(randint(0, 10000))
        hashedVal = str(sha256(value.encode('utf-8')).hexdigest())
        return hashedVal
