import random
from blockchain import *
from miner import *
from block import *


def do_run():
    blockchain = Blockchain()
    inner = False
    outer = True
    temp_count = 0
    loopCounter = -1

    miners_list = []
    for i in range(0, 4):  # id  #pwr
        miners_list.append(Miner(i + 1, i))  # miner id correlates to hardware power for now, where the lowest id will be number 1

    while outer:
        print("running outer")
        threshold = random.randint(1, 4)
        print("threshold: ", threshold)
        inner = True  # so inner can be turned off in the inner loop when block is mined, then re-turned on when outer loop restarts
        for miner in miners_list:
            miner.start_mine()

        while inner:  # this allows if statement to see if chain is appending to genesis or not, then creates a local block using previous block + txs bundle, loopCounter = -1 here
            mined_block = None

            print("running inner")
            if blockchain.getChainHeight() == 1:  # ensure this initialization correctly represents the intended previous block.
                local_block = Block(blockchain.chain[0])
                print("local ", local_block)
            else:
                local_block = Block(blockchain.chain[blockchain.getChainHeight() - 1])
                print("local", local_block)
                print(blockchain.chain)
            while mined_block is None:  # exit loop when is mined, can also parse miner number which is then printed but not in/related to blockchain
                loopCounter += 1
                if loopCounter > 3:
                    loopCounter = 0
                print(loopCounter)
                if loopCounter >= 0:
                    mined_block = miners_list[0].handle_tick(local_block, threshold)
                    print("miner hardware", miners_list[0].hardwarePower, "firing")
                if loopCounter >= 1:
                    mined_block = miners_list[1].handle_tick(local_block, threshold)
                    print("miner hardware", miners_list[1].hardwarePower, "firing")
                if loopCounter >= 2:
                    mined_block = miners_list[2].handle_tick(local_block, threshold)
                    print("miner hardware", miners_list[2].hardwarePower, "firing")
                if loopCounter >= 3:
                    mined_block = miners_list[3].handle_tick(local_block, threshold)
                    print("miner hardware", miners_list[3].hardwarePower, "firing")
                print(mined_block)
            del local_block
            print("breaking inner, stopping miners")
            for miner in miners_list:
                miner.stop_mine()
            break  # needs to be removed, turn off inner loop or remove as is redundant, when does this will simulate full node majority validation

        blockchain.addToChain(mined_block)
        print(blockchain.chain)
        print("breaking outer")
        del mined_block
        temp_count += 1  #
        if temp_count > 5:
            outer = False


if __name__ == '__main__':
    do_run()


#########################################################################
# need to do: cleanup -- still relying on breaks for loop exiting (remove inner loop? however this turns miners off and on) -- do run separate file -- really trim and cut down outputs -- return miner number, parallel miner id array, print when blockchain is printed? --
# loop doesnt use miner hardware level (can just give them the values already in loop) -- get rid of nonce tag in block as its always 0? or just update it just before block is added --
# miners can rearrange txs to make small miners able to compete(ask mark) --
# PROGRAM LOG
# took nonce hashing algo and txs generator from another file where i experimented with it until it was ok for this program -- generate 10 random hash strings to simulate a bundle of individually hashed txs presented for a miner to hash then place in a block--
# cut away most of the implementation of my mining logic (while loop) to be replaced with a tick based system, where each miner mines sequentially based on their hardware capabilities, then returns the nonce, easing the whole process --
# local_block = Block(blockchain.chain[0]) if genesis or not logic implementation -- blockchain appends and references last block even if genesis, however genesis still generates txs--
# got all of the set up out of the way before actually using the miner_tick yet -- miner_tick now has functionality, where it is parsed in information, distributed correctly (local block stored in miner when start_mine fires, as well as threshold is now passed to mine())--
# completed cleaned and finished txs class -- start and stop mine functions both work and are useful (stores local block, then clears local block and nonce when stopped)
# miner correctly hashes and produces pow -- implement multiple miners with loopCounter = -1 logic (remember when doing writeup to include that i built a loopCounter prototype beforehand which was then implemented with miners)
# if found: running = False  # simulated full node majority validation --
