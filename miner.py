from hashlib import sha256


class Miner:
    def __init__(self, id, hardwarePower):
        self._id = id
        self.hardwarePower = hardwarePower  # ?not to sure if this should be parsed in or determined later, however is a needed attribute

        self._mining = True
        self._block = None
        self._nonce = 0

    def start_mine(self):
        self._mining = True  # determine whether to break out of mining each miner cycle?

    def stop_mine(self):
        self._mining = False  # set mining to false then mining should stop and move onto next whole block
        self._block = None
        self._nonce = 0

    def handle_tick(self, block, threshold, winners):  # PASS IN LOCAL BLOCK, THEN PASS LOCAL BLOCK TO MINE FUNCT, WHICH WILL BE HASHED WITH MINERS STORED NONCE, then stop_mine and return completed block, else end handle_tick and wait for next miner to mine
        # print("entering miner tick")
        if self._mining == True:
            self._block = block  # set state of block to local block, so then _block can be used when passed into PoW function
            self._nonce = self._nonce + 1  # updates nonce within the miner itself -- in mine function, after you know the hashed val is not valid for difficulty
            self.start_mine()
            miningOutput, flag = self.mine(threshold)
            if flag == True:
                winners.append(self._id)
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
            print("pre-nonce hash: ", tempBlock)
            print("post-nonce hash: ", hashedBlock)
            flag = True
            return hashedBlock, flag
        else:
            return "", False  # return unsuccessful attempt
