from blockchain import *
from miner import *
from block import *


def do_run():
    blockchain = Blockchain()
    threshold = 3  # this will fluctuate in an outer loop, inner loop will mine, outer loop will append mined block and generate new threshold
    running = True

    miners_list = []
    for i in range(0, 4):       #id  #pwr
        miners_list.append(Miner(i+1, i))  # miner id correlates to hardware power for now, where the lowest number will be number 1

    while running:  # this allows if statement to see if chain is appending to genesis or not, then creates a local block using previous block + txs bundle
        if blockchain.getChainHeight() == 1:
            local_block = Block(blockchain.chain[0])
        else:
            local_block = Block(blockchain.chain[blockchain.getChainHeight()-1])
            print(local_block)
            print(blockchain.chain)
            break
        print(blockchain.chain)
        print(local_block)
        blockchain.addToChain("block")

        # Create a new block, while running will run until local_block has something to put in it, then can push that to append to blockchain

        '''
        for miner in miners_list:
            (found, id) = miner.handle_tick()

            ## loopCounter = -1 loop here, parse in the id to identify which miner is being called
            # can still structure it like the (loopCounter = -1 loop) where print("miner hardware 0 firing") is a miner.tick, parsing in miner id and returning if solved + nonce
            # (id is already known)
            # threshold needs to be determined around here somewhere, to then parse to mine funct
            if found:
                running = False  # simulated full node majority validation
        '''


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
# cut away most of the implementation of my mining logic (while loop) to be replaced with a tick based system, where each miner mines sequentially based on their hardware capabilities, then returns the nonce, easing the whole process --
# local_block = Block(blockchain.chain[0]) if genesis or not logic implementation --
#
