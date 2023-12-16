from transaction import *
from hashlib import sha256


class Block:
    def __init__(self, previous):
        # This is the hash of the previous (mined) Block - maybe logic for genesis, but doesnt matter if its a hash
        self.previous = previous  # previous hash
        # This 'will be' the hash of this Block it is the hash of the nonce and the hash values
        # of each of the 10 nested transactions
        self.hash = 0

        self.nonce = 0
        self._transactions = 0
        concatTrans = ""

        for i in range(10):
            concatTrans = concatTrans + str(Transaction())  # generate then hash 10 concatenated txs
        self._transactions = str(sha256(concatTrans.encode('utf-8')).hexdigest())

    # Generate the hash self._hash = afunctionyouwrite() - concat then hash generates hashes

    def __str__(self):
        return f"Block(prevBlock={self.previous}, txs={self._transactions}, nonce={self.nonce})"
