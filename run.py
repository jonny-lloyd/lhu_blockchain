import random
from blockchain import *
from miner import *
from block import *


def do_run():
    """
    do_run is where this simulation of PoW mining starts and is orchestrated.

    Firstly, 'Blockchain' is instantiated into 'blockchain', a list of Miner instances with different hardware capabilities is generated,
    as well as the initialisation of the variables winningMiner, mainLoop, and loopCounter.

    Then, the mining simulation starts within mainLoop.

    After the right block hash has been found, all miners are turned off and the mined block is appended to 'blockchain'.
    """

    blockchain = Blockchain()  # instantiation of blockchain
    winningMiner = ["Null"]  # list of winning miners for every block
    mainLoop = True
    temp_count = 0  # chain length counter
    loopCounter = -1

    miners_list = []
    for i in range(0, 4):        #id   #pwr
        miners_list.append(Miner(i + 1, i))

    while mainLoop:
        """
        Difficulty threshold (number of 0's at the beginning of each mined block) is set randomly for every block mined to 
        simulate fluctuating mining difficulty on a real blockchain, such as Bitcoin. Then, Miners are set to start_mine mode.
        
        After this, the blockchain height is checked, if the height is 1, then the miners use the genesis block in 
        the creation of the local block before it is mined, if the genesis isn't to be used, then the highest block
        on the chain is used instead. This is because the 'previous block' is required to construct a block object.
        """

        mined_block = None
        threshold = random.randint(1, 4)
        print("threshold: ", threshold)
        for miner in miners_list:
            miner.start_mine()

        if blockchain.getChainHeight() == 1:
            local_block = Block(blockchain.chain[0])  # creation of the new block passing in local_block
            print("local ", local_block)
        else:
            local_block = Block(blockchain.chain[blockchain.getChainHeight() - 1])
            print("local", local_block)
            print(blockchain.chain)

        while mined_block is None:
            """
            A loop counter will repeatedly count up to 3 incrementing by 1 every loop iteration, then reset to 0 if loopCounter > 3.
            if hardwarePower == loopCounter, then that miner will execute 1 nonce incremental mining cycle, or 'tick'. This
            results in the higher 'mining power'/hardware Miners firing/guessing more frequently than lower hardware Miners.
            
            The mining result is then checked, if the result is Null then it is discarded, if is not null then a block
            that meets the difficulty threshold has been met by a miner and they have returned the results.
            """

            loopCounter += 1
            if loopCounter > 3:
                loopCounter = 0
            print("\n\nLOOP COUNTER: ", loopCounter)
            if loopCounter >= miners_list[0].hardwarePower:
                print("miner ", miners_list[0].getId(), "firing")
                mined_block = miners_list[0].handle_tick(local_block, threshold, winningMiner)
                if mined_block is not None:  # stop miners from mining after block is found,
                    loopCounter = -1  # stops other miners from still guessing even though block hash has been found

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
        temp_count += 1
        if temp_count > 6:  # determines how many blocks long the chain is, doesnt take genesis into account, so 8
            mainLoop = False

    print("Winning miners", winningMiner)
