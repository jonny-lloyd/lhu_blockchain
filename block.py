from transaction import *
from hashlib import sha256


class Block:
    """
    Blocks are instantiated by passing in the hash of the previous mined block. self.nonce is defined which is to then
    be incremented inside handle_tick. self.transactions is defined then 10 generated transactions are generated using
    the transaction.py class, these 10 txs are then concatenated and hashed, forming a pre-mined block of txs.
    """

    def __init__(self, previous):
        self.previous = previous  # previous hash
        self.nonce = 0
        self._transactions = 0
        concatTx = ""

        for i in range(10):
            concatTx = concatTx + str(Transaction())  # generate then concatenate 10 txs, then hash -> block of 10 hash
        self._transactions = str(sha256(concatTx.encode('utf-8')).hexdigest())

    def setNonce(self, nonce):
        self.nonce = nonce

    def getTxs(self):
        return self._transactions

    def getPrevious(self):
        return self.previous

    def __str__(self):
        # allow human-readable block representation
        return f"Block(prevBlock={self.previous}, txs={self._transactions}, nonce={self.nonce})"
