# import pygame
from hashlib import sha256
from random import seed, randint


class Blockchain:
    def __init__(self):
        self.blockHeight = 0
        self.chain = ["Genesis"]  # need to hash this - or just hash the raw data?
        #  self.merkle = merkle

    def addToChain(self, block):
        self.chain.append(block)  # fully hashed block

    def getChainHeight(self):
        self.blockHeight = len(self.chain)  # updates then returns the blockHeight
        return self.blockHeight

    # def getChainHeight(self):
    #    return self.blockHeight

    def getChain(self):
        chain_strs = []
        for block in self.chain:
            chain_strs.append(str(block))  # Convert to actually readable format
        return chain_strs

    # get last block hash
    #   use get chain to only get hash of last block, len-1 or something


class Block:
    def __init__(self, merkle, txs, nonce):
        self.merkle = merkle  # previous hash
        self.transactions = txs  # hash of txs
        self.nonce = nonce

    def __str__(self):
        return f"Block(merkle={self.merkle}, txs={self.transactions}, nonce={self.nonce})"


class Miner:
    def __init__(self, number, hardwarePower):
        self.number = number
        self.hardwarePower = hardwarePower  # ?not to sure if this should be parsed in or determined later, however is a needed attribute

    def getHardwarePower(self):
        return self.hardwarePower

    @staticmethod  # method that belongs to the class rather than to instances of the class
    def mine(difficulty):  # ALSO TAKE HASHED TXS FROM BLOCK INSTANCE AS WELL AS MERKLE, THEN HASH UNTIL DIFFICULTY THRESHOLD MET
        flag = False
        x = -1

        while not flag:  # while flag is not true
            x += 1
            tempNonce = "coin" + str(x)
            #print(tempNonce)
            hashedCoin = str(sha256(tempNonce.encode('utf-8')).hexdigest())
            #print(hashedCoin)
            zeroStr = '0' * difficulty

            if hashedCoin[0:difficulty] == zeroStr:
                print("\nthreshold met")
                flag = True
                print(tempNonce)
                print(hashedCoin)

        # call func to add fully hashed block to chain.

        # have to consider how this will fire, it needs to be able to build on last iteration count - as some miners will miss iterations per mine cycle -
        # maybe make an if that checks if the iteration count is 0? - maybe store iteration count + hash so will remember on the miners side

        # difficulty determined once per mine cycle (will be a loop inside a loop where outer is mine cycle -
        # outer is where dif is determined (and where blocks completed blocks could be appended) - and inner is until one cracks difficulty)
        # then append completed block to blockchain in outer loop

        # could have a counter in the inner loop that resets to 1 every 4 iterations (if there are 4 miners) then set </> thresholds comparing iteration counter
        # to miner hardware level, if lower then dont execute, else if == or higher then execute mine()


def hashGenerator(enteredSeed):
    seed(enteredSeed)
    fullHash = ""
    completeHash = ""
    for x in range(10):  # generate 10 random hash strings to simulate a bundle of individually hashed txs presented for a miner to hash then place in a block
        value = str(randint(0, 1000))
        hashedVal = str(sha256(value.encode('utf-8')).hexdigest())
        fullHash = hashedVal + fullHash
        completeHash = (sha256(fullHash.encode('utf-8')).hexdigest())
    print("full", fullHash)
    print("complete", completeHash)
    return completeHash


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
##  struggling with the idea of firing mine once, saving the state, going through the loop,
##  then loading that state and continuing from saved state for each miner


#########################################################################
# need to do: implement commented (ln 65+) looping structure: which is both the mining logic and implementation, and looping structure
#
# PROGRAM LOG
# took nonce hashing algo and txs generator from another file where i experimented with it until it was ok for this program -- generate 10 random hash strings to simulate a bundle of individually hashed txs presented for a miner to hash then place in a block--
#
#
#
