from hashlib import sha256


class Miner:
    def __init__(self, id, hardwarePower):
        self._id = id
        self.hardwarePower = hardwarePower  # ?not to sure if this should be parsed in or determined later, however is a needed attribute

        self._mining = True
        self._block = None
        self._nonce = 0

    def start_mine(self):  # threshold to be determined randomly after every blockchain block appending
        self._mining = True  # ?why is this here? so can determine whether to break out of mining each miner cycle?

    def stop_mine(self):
        self._mining = False  # need to find use of this, maybe in set mining to false then use that to see if mining should stop and move onto next whole block
        self._block = None
        self._nonce = 0

    def handle_tick(self, block, threshold):  # PASS IN LOCAL BLOCK, THEN PASS LOCAL BLOCK TO MINE FUNCT, WHICH WILL BE HASHED WITH MINERS STORED NONCE
        # pass in local block and difficulty, hash combing miners nonce attribute, return. logic determines if it meets diff criteria here, if so then stop_mine and return completed block,
        # else end handle_tick and wait for next miner to mine
        # print("entering miner tick")
        if self._mining == True:
            # print("self._mining == True, this if for miner ", self._id)
            self._block = block  # set state of block to local block, so then _block can be used when passed into PoW function
            self._nonce = self._nonce + 1  # updates nonce within the miner itself -- put this in mine function, after you know the hashed val is not valid for difficulty
            self.start_mine()
            miningOutput, flag = self.mine(threshold)
            # print("inside tick flag", flag)
            # print("inside tick mining output", miningOutput)
            if flag == True:
                print("in tick flag true return mining output")
                return miningOutput  # self._id -- !!set self._block to fully mined block when completed, remember to do something with parsed miner id
            else:
                # print("in tick else return none")
                return None
        else:
            # print("in tick else return")
            return

    def setBlock(self, block):
        self._block = block

    def getHardwarePower(self):
        return self.hardwarePower

    def mine(self, threshold):  # ALSO TAKE HASHED TXS FROM BLOCK INSTANCE AS WELL AS MERKLE, THEN HASH UNTIL DIFFICULTY THRESHOLD MET
        flag = False

        # print("entering mine")
        transactions = self._block.getTxs()
        previousBlock = self._block.getPrevious()
        # print("txs: ", transactions)
        # print("local block in miner: ", self._block)
        # print("miner id: ", self._id)
        # print("nonce: ", self._nonce)
        # print("prev: ", previousBlock)

        concat = str(transactions) + str(previousBlock)
        # print("concat", concat)

        zeroStr = str('0' * threshold)

        tempCoin = concat + str(self._nonce)
        # print("concat + nonce: ", tempCoin)
        hashedCoin = str(sha256(tempCoin.encode('utf-8')).hexdigest())
        # print("hashedCoin: ", hashedCoin)
        # print("threshold: ", threshold)
        # print("zerostr: ", zeroStr)

        if hashedCoin[0:threshold] == zeroStr:
            print("\nthreshold met")
            print(tempCoin)
            print(hashedCoin)
            flag = True
            return hashedCoin, flag
        else:
            return "", False  # return unsuccessful attempt
