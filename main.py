from blockchain import *
from miner import *
from transaction import *


class Block:
    def __init__(self, previous, nonce):
        # This is the hash of the previous (mined) Blcok - maybe logic for genesis, but doesnt matter if its a hash
        self.previous = previous  # previous hash
        # This 'will be' the hash of this Block it is the hash of the nonce and the hash values
        # of each of the 10 nested transactions
        self.hash = 0

        self.nonce = nonce
        self._transactions = []
        for i in range(10):
            self._transactions.append(Transaction())

        # Generate the hash self._hash = afunctionyouwrite() - concat then hash generates hashes

    def __str__(self):
        return f"Block(merkle={self.previous}, txs={self._transactions}, nonce={self.nonce})"


def do_run():
    running = True
    local_block = None

    miners_list = []

    for i in range(0, 4):
        miners_list.append(Miner(i, 20))

    while running:
        # Create a new block
        for miner in miners_list:
            (found, id) = miner.handle_tick()


if __name__ == '__main__':
    do_run()

'''
chainHash = hashGenerator(1)
blockchain = Blockchain()  # keep outside of loop
block1 = Block(123, chainHash, 1)
blockchain.addToChain(block1)
print(blockchain.getChain())

chainHash = hashGenerator(2)
block2 = Block(345, chainHash, 7)
blockchain.addToChain(block2)
print(blockchain.getChain())
print("---------------\n")

miner1 = Miner(1, 1)
miner1.mine(1)

##
loopCounter = -1
for x in range(10):
    loopCounter += 1
    if loopCounter > 2:
        loopCounter = 0
    print(loopCounter)
    if loopCounter >= 0:
        print("miner hardware 0 firing")
    if loopCounter >= 1:
        print("miner hardware 1 firing")
    if loopCounter >= 2:
        print("miner hardware 2 firing")
'''

'''
def hashGenerator(enteredSeed):
    seed(enteredSeed)
    fullHash = ""
    completeHash = ""
    for x in range(
            10):  # generate 10 random hash strings to simulate a bundle of individually hashed txs presented for a miner to hash then place in a block
        value = str(randint(0, 1000))
        hashedVal = str(sha256(value.encode('utf-8')).hexdigest())
        fullHash = hashedVal + fullHash
        completeHash = (sha256(fullHash.encode('utf-8')).hexdigest())
    print("full", fullHash)
    print("complete", completeHash)
    return completeHash
'''

##  struggling with the idea of firing mine once, saving the state, going through the loop,
##  then loading that state and continuing from saved state for each miner


#########################################################################
# need to do: implement commented (ln 65+) looping structure: which is both the mining logic and implementation, and looping structure- seperate classes into seperate
# files that feed into do_run() main file-
# PROGRAM LOG
# took nonce hashing algo and txs generator from another file where i experimented with it until it was ok for this program -- generate 10 random hash strings to simulate a bundle of individually hashed txs presented for a miner to hash then place in a block--
# cut away most of the implementation of my mining logic (while loop) to be replaced with a tick based system, where each miner mines sequentially based on their hardware capabilities, then returns the nonce, easing the whole process
#
#
