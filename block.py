from transaction import *
from hashlib import sha256


class Block:
    def __init__(self, previous):
        self.previous = previous  # previous hash
        self.hash = 0

        self.nonce = 0
        self._transactions = 0
        concatTx = ""

        for i in range(10):
            concatTx = concatTx + str(Transaction())  # generate then hash 10 concatenated txs
        self._transactions = str(sha256(concatTx.encode('utf-8')).hexdigest())

    def setNonce(self, nonce):
        self.nonce = nonce

    def getTxs(self):
        return self._transactions

    def getPrevious(self):
        return self.previous

    def __str__(self):
        return f"Block(prevBlock={self.previous}, txs={self._transactions}, nonce={self.nonce})"
