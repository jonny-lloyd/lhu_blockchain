from random import randint
from hashlib import sha256


class Transaction:  # generates and returns 1 tx at a time, which gets hash bundled and stored in Block
    """
    Generates single Transaction objects when called. This is called in Block class where these txs are bundled to form
    a pre-mined block.

    Between 1 and 10,000 chance of being the same tx, in the persuit of generating completely different and unique
    blockchains for every simulation.
    """

    def __init__(self):
        self._transaction = self._generateTransaction()

    @staticmethod
    def _generateTransaction():
        value = str(randint(0, 10000))  # 1 in 10,000 chance of being the same hash, which represents a transaction
        hashedVal = str(sha256(value.encode('utf-8')).hexdigest())
        return hashedVal
