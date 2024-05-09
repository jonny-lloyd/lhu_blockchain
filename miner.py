from hashlib import sha256


class Miner:
    """
    Miners are instantiated with an ID attribute, hardwarePower, current state (self._mining), block
    they are working on currently (self._block), their current nonce iteration for current block (self._nonce).

    The Miners are told to start inside of run.py everytime a new block is to be added to the chain, when the miner has
    found a block hash that meets the random dif threshold, the state of the Miner is then updated. This resets current
    data for the miner such as the current block inside that is being worked on by the miner (self._block) and the nonce iteration.
    """

    def __init__(self, id, hardwarePower):
        self._id = id
        self.hardwarePower = hardwarePower

        self._mining = True
        self._block = None
        self._nonce = 0

    def start_mine(self):
        self._mining = True  # determine whether to break out of mining each miner cycle

    def stop_mine(self):
        self._mining = False  # set mining to false then mining should stop and move onto next whole block
        self._block = None
        self._nonce = 0

    def handle_tick(self, block, threshold, winners):
        """
        def handle_tick(self, block, threshold, winners):

        handle_tick takes in the block which is to be worked on, as well as the difficulty threshold and an array that
        keeps track of winning miner IDs

        if the miner is ready to mine (self._mining == True), local data within the miner is updated and the miner enters
        the mine() function.

        A flag is which returns whether the mining attempt was successful, if its true then the miners ID is appended
        to the winner array and the worked block is returned to be appended to 'blockchain'

        :param block: block is a reference to current_block, which is the highest block on the chain and is to be
        concatenated and mined along with other info such as nonce, transactions, etc
        :param threshold: random mining difficulty of the block to be produced
        :param winners: list of winning miners, which may be appended to if the miner wins this tick
        :return: if a block is mined it is returned, else nothing will be returned
        """

        if self._mining == True:
            self._block = block  # set state of block to local block, so then _block can be used in PoW function
            self._nonce = self._nonce + 1  # updates nonce within the miner itself
            miningOutput, flag = self.mine(threshold)
            if flag == True:
                winners.append(self._id)
                self._block.setNonce(self._nonce)  # updates nonce on the block
                print("Worked block: ", self._block)
                return miningOutput
            else:
                return None
        else:
            return

    def setBlock(self, block):
        self._block = block

    def getHardwarePower(self):
        return self.hardwarePower

    def getId(self):
        return self._id

    def mine(self, threshold):
        """
        def mine(self, threshold):
        The passed in block has all information that constitutes a block (concatenated Txs hash + previous block + nonce)
        concatenated then hashed.

        This hash is then checked to see if it meets the pre-determined difficulty which is used to count the number of
        chars at the beginning of the post-work-hash (hashedBlock). For example if the difficulty threshold is 3,
        the first 3 chars are checked to see if they are all 0's, if so, the block has been successfully mined to meet
        the criteria.

        :param threshold: required block difficulty
        :return: if the leading 0s of a produced hash meets the threshold, a valid mined block has been mined a flag is
        raised and the mined block is returned, else there are two empty returns
        """

        transactions = self._block.getTxs()
        previousBlock = self._block.getPrevious()
        print("nonce: ", self._nonce)
        # print("txs: ", transactions)
        # print("local block in miner: ", self._block)
        # print("miner id: ", self._id)
        # print("prev: ", previousBlock)


        concat = str(transactions) + str(previousBlock)
        zeroStr = str('0' * threshold)
        # print("concat", concat)
        tempBlock = concat + str(self._nonce)
        print("concatenated hash + previous block + nonce: ", tempBlock)
        hashedBlock = str(sha256(tempBlock.encode('utf-8')).hexdigest())
        print("hashedBlock: ", hashedBlock)
        # print("zeroStr: ", zeroStr)

        if hashedBlock[0:threshold] == zeroStr:
            print("\nhash threshold of", zeroStr, "found")
            print("concat with nonce: ", tempBlock)
            print("post-hash using nonce: ", hashedBlock)
            flag = True
            return hashedBlock, flag
        else:
            return "", False  # return unsuccessful attempt
