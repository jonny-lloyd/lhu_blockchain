import random
from blockchain import *
from miner import *
from block import *


def do_run():
    blockchain = Blockchain()
    mainLoop = True
    temp_count = 0
    loopCounter = -1

    miners_list = []
    for i in range(0, 4):  # id  #pwr
        miners_list.append(Miner(i + 1, i))  # miner id correlates to hardware power for now, where the lowest id will be number 1

    while mainLoop:
        mined_block = None

        print("running mainLoop")
        threshold = random.randint(1, 4)
        print("threshold: ", threshold)
        for miner in miners_list:
            miner.start_mine()

        if blockchain.getChainHeight() == 1:  # ensure this initialization correctly represents the intended previous block.
            local_block = Block(blockchain.chain[0])
            print("local ", local_block)
        else:
            local_block = Block(blockchain.chain[blockchain.getChainHeight() - 1])
            print("local", local_block)
            print(blockchain.chain)

        print("running inner")
        while mined_block is None:  # hard coded hardware levels
            loopCounter += 1
            if loopCounter > 3:
                loopCounter = 0
            print("\n\nLOOP COUNTER: ", loopCounter)
            if loopCounter >= miners_list[0].hardwarePower:
                print("miner hardware", miners_list[0].hardwarePower, "firing")
                mined_block = miners_list[0].handle_tick(local_block, threshold)

            if loopCounter >= miners_list[1].hardwarePower:
                print("miner hardware", miners_list[1].hardwarePower, "firing")
                mined_block = miners_list[1].handle_tick(local_block, threshold)

            if loopCounter >= miners_list[2].hardwarePower:
                mined_block = miners_list[2].handle_tick(local_block, threshold)
                print("miner hardware", miners_list[2].hardwarePower, "firing")

            if loopCounter >= miners_list[3].hardwarePower:
                mined_block = miners_list[3].handle_tick(local_block, threshold)
                print("miner hardware", miners_list[3].hardwarePower, "firing")

        del local_block
        print("breaking inner, stopping miners")
        for miner in miners_list:
            miner.stop_mine()

        blockchain.addToChain(mined_block)
        print(blockchain.chain)
        print("breaking mainLoop")
        del mined_block
        temp_count += 1  #
        if temp_count > 5:
            mainLoop = False


if __name__ == '__main__':
    do_run()


#########################################################################
# need to do:  -- do run separate file  -- return miner number, parallel miner id array, print when blockchain is printed? --
# loop doesnt use miner hardware level (can just give them the values already in loop) -- get rid of nonce tag in block as its always 0? or just update it just before block is added --
# miners can rearrange txs to make small miners able to compete(ask mark) --
# PROGRAM LOG
# took nonce hashing algo and txs generator from another file where i experimented with it until it was ok for this program -- generate 10 random hash strings to simulate a bundle of individually hashed txs presented for a miner to hash then place in a block--
# cut away most of the implementation of my mining logic (while loop) to be replaced with a tick based system, where each miner mines sequentially based on their hardware capabilities, then returns the nonce, easing the whole process --
# local_block = Block(blockchain.chain[0]) if genesis or not logic implementation -- blockchain appends and references last block even if genesis, however genesis still generates txs--
# got all of the set up out of the way before actually using the miner_tick yet -- miner_tick now has functionality, where it is parsed in information, distributed correctly (local block stored in miner when start_mine fires, as well as threshold is now passed to mine())--
# completed cleaned and finished txs class -- start and stop mine functions both work and are useful (stores local block, then clears local block and nonce when stopped)
# miner correctly hashes and produces pow -- implement multiple miners with loopCounter = -1 logic (remember when doing writeup to include that i built a loopCounter prototype beforehand which was then implemented with miners)
# if found: running = False  # simulated full node majority validation -- loopCounter now uses the miners hardware level -- still relying on breaks for loop exiting - removed inner loop --
#
#
#
#

