import random
from blockchain import *
from miner import *
from block import *


def do_run():
    blockchain = Blockchain()
    inner = False
    outer = True
    temp_count = 0

    miners_list = []
    for i in range(0, 4):  # id  #pwr
        miners_list.append(
            Miner(i + 1, i))  # miner id correlates to hardware power for now, where the lowest id will be number 1

    while outer:
        print("running outer")
        threshold = random.randint(1, 4)
        inner = True  # so inner can be turned off in the inner loop when block is mined, then re-turned on when outer loop restarts

        while inner:  # this allows if statement to see if chain is appending to genesis or not, then creates a local block using previous block + txs bundle, loopCounter = -1 here
            mined_block = None

            print("running inner")
            if blockchain.getChainHeight() == 1:  # ensure this initialization correctly represents the intended previous block.
                local_block = Block(blockchain.chain[0])  # ?generates txs for genesis which is not good, can just leave txs part as a 0, however doesnt impact workings of blockchain
                print("local ", local_block)
            else:
                local_block = Block(blockchain.chain[blockchain.getChainHeight() - 1])
                print("local", local_block)
                print(blockchain.chain)

            mined_block = miners_list[0].handle_tick(local_block, threshold)
            del local_block
            break

        blockchain.addToChain(mined_block)
        print(blockchain.chain)
        print("breaking outer")

        temp_count += 1  #
        if temp_count > 5:
            outer = False


if __name__ == '__main__':
    do_run()

'''
    for miner in miners_list:
        miner.setBlock(localBlock)   this needs to happen once for all miners every time a new local block is set (could just be pinned to 'if blockchain.getChainHeight() == 1' logic?)
        (found, id) = miner.handle_tick()
'''

'''
    ## loopCounter = -1 loop here, parse in the id to identify which miner is being called
    # can still structure it like the (loopCounter = -1 loop) where print("miner hardware 0 firing") is a miner.tick, parsing in miner id and returning if solved + nonce
    # (id is already known)
    # threshold needs to be determined around here somewhere, to then parse to mine funct
    if found:
        running = False  # simulated full node majority validation
'''

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

#########################################################################
# TXS GENERATOR CONSIDERATIONS: If you want each transaction to be unique, you need to create a new instance of the Transaction class inside your mining loop instead of incrementing a counter.
# This way, each transaction will have a different hash value. Right now, it seems the transactions are using the same previously generated values and not generating new ones inside the loop.


# need to do: miner correctly hashes and produces pow -- implement multiple miners with loopCounter = -1 logic
# PROGRAM LOG
# took nonce hashing algo and txs generator from another file where i experimented with it until it was ok for this program -- generate 10 random hash strings to simulate a bundle of individually hashed txs presented for a miner to hash then place in a block--
# cut away most of the implementation of my mining logic (while loop) to be replaced with a tick based system, where each miner mines sequentially based on their hardware capabilities, then returns the nonce, easing the whole process --
# local_block = Block(blockchain.chain[0]) if genesis or not logic implementation -- blockchain appends and references last block even if genesis, however genesis still generates txs--
# got all of the set up out of the way before actually using the miner_tick yet -- miner_tick now has functionality, where it is parsed in information, distributed correctly (local block stored in miner when start_mine fires, as well as threshold is now passed to mine())--
# completed cleaned and finished txs class -- start and stop mine functions both work and are useful (stores local block, then clears local block and nonce when stopped)
#