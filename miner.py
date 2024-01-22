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
        self.hardwarePower = hardwarePower  # ?not to sure if this should be parsed in or determined later, however is a needed attribute

        self._mining = True
        self._block = None
        self._nonce = 0

    def start_mine(self):
        self._mining = True  # determine whether to break out of mining each miner cycle

    def stop_mine(self):
        self._mining = False  # set mining to false then mining should stop and move onto next whole block
        self._block = None
        self._nonce = 0

    def handle_tick(self, block, threshold, winners):  # PASS IN LOCAL BLOCK, THEN PASS LOCAL BLOCK TO MINE FUNCT, WHICH WILL BE HASHED WITH MINERS STORED NONCE, then stop_mine and return completed block, else end handle_tick and wait for next miner to mine
        """
        handle_tick takes in the block which is to be worked on, as well as the difficulty threshold and an array that
        keeps track of winning miner IDs

        if the miner is ready to mine (self._mining == True), local data within the miner is updated and the miner enters
        the mine() function.

        A flag is which returns whether the mining attempt was successful, if its true then the miners ID is appended
        to the winner array and the worked block is returned to be appended to 'blockchain'
        """

        # print("entering miner tick")
        if self._mining == True:
            self._block = block  # set state of block to local block, so then _block can be used when passed into PoW function
            self._nonce = self._nonce + 1  # updates nonce within the miner itself -- in mine function, after you know the hashed val is not valid for difficulty
            self.start_mine()
            miningOutput, flag = self.mine(threshold)
            if flag == True:
                winners.append(self._id)
                self._block.setNonce(self._nonce)  # updates nonce on the block
                print("Worked block: ", self._block)
                return miningOutput  # self._id -- !!set self._block to fully mined block when completed, remember to do something with parsed miner id.
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
        The passed in block has all information that constitutes a block (concatenated Txs hash + previous block + nonce)
        concatenated then hashed.

        This hash is then checked to see if it meets the pre-determined difficulty which is used to count the number of
        chars at the beginning of the post-work-hash (hashedBlock). For example if the difficulty threshold is 3,
        the first 3 chars are checked to see if they are all 0's, if so, the block has been successfully mined to meet
        the criteria.
        """

        flag = False

        # print("entering mine")
        transactions = self._block.getTxs()
        previousBlock = self._block.getPrevious()
        # print("txs: ", transactions)
        # print("local block in miner: ", self._block)
        # print("miner id: ", self._id)
        print("nonce: ", self._nonce)
        # print("prev: ", previousBlock)

        concat = str(transactions) + str(previousBlock)
        # print("concat", concat)

        zeroStr = str('0' * threshold)

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
