import random
from blockchain import *
from miner import *
from block import *


def do_run():
    blockchain = Blockchain()
    winningMiner = ["Null"]  # pass into tick

    mainLoop = True
    temp_count = 0
    loopCounter = -1

    miners_list = []
    for i in range(0, 4):  # id  #pwr
        miners_list.append(Miner(i + 1, i))  #

    while mainLoop:
        mined_block = None
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

        while mined_block is None:
            loopCounter += 1
            if loopCounter > 3:
                loopCounter = 0
            print("\n\nLOOP COUNTER: ", loopCounter)
            if loopCounter >= miners_list[0].hardwarePower:
                print("miner ", miners_list[0].getId(), "firing")
                mined_block = miners_list[0].handle_tick(local_block, threshold, winningMiner)
                if mined_block is not None:  # stop miners from mining after block is found,
                    loopCounter = -1

            if loopCounter >= miners_list[1].hardwarePower:
                print("miner ", miners_list[1].getId(), "firing")
                mined_block = miners_list[1].handle_tick(local_block, threshold, winningMiner)
                if mined_block is not None:
                    loopCounter = -1

            if loopCounter >= miners_list[2].hardwarePower:
                print("miner ", miners_list[2].getId(), "firing")
                mined_block = miners_list[2].handle_tick(local_block, threshold, winningMiner)
                if mined_block is not None:
                    loopCounter = -1

            if loopCounter >= miners_list[3].hardwarePower:
                print("miner ", miners_list[3].getId(), "firing")
                mined_block = miners_list[3].handle_tick(local_block, threshold, winningMiner)
                if mined_block is not None:
                    loopCounter = -1

        del local_block
        print("stopping miners")
        for miner in miners_list:
            miner.stop_mine()

        blockchain.addToChain(mined_block)
        print("\n")
        print(blockchain.chain)
        del mined_block
        temp_count += 1  #
        if temp_count > 2:  # determines how many blocks long the chain is
            mainLoop = False

    print("Winning miners", winningMiner)
