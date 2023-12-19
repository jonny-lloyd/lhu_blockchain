from hashlib import sha256


class Miner:
    def __init__(self, id, hardwarePower):
        self._id = id
        self.hardwarePower = hardwarePower  # ?not to sure if this should be parsed in or determined later, however is a needed attribute

        self._mining = False
        self._block = None
        self._nonce = 0

    def start_mine(self, block):  # threshold to be determined randomly after every blockchain block appending
        self._block = block  # set state of block to local block, so then _block can be used when passed into PoW function
        self._mining = True  # ?why is this here? so can determine whether to break out of mining each miner cycle?

    def stop_mine(self):
        self._mining = False  # need to find use of this, maybe in set mining to false then use that to see if mining should stop and move onto next whole block
        self._block = None
        self._nonce = 0

    def handle_tick(self, block, threshold):  # PASS IN LOCAL BLOCK, THEN PASS LOCAL BLOCK TO MINE FUNCT, WHICH WILL BE HASHED WITH MINERS STORED NONCE
        # pass in local block and difficulty, hash combing miners nonce attribute, return. logic determines if it meets diff criteria here, if so then stop_mine and return completed block,
        # else end handle_tick and wait for next miner to mine
        self._nonce = self._nonce + 1  # updates nonce within the miner itself -- put this in mine function, after you know the hashed val is not valid for difficulty
        self.start_mine(block)
        self.mine(threshold)
        return self._block, self._id  # set self._block to fully mined block when completed

    def setBlock(self, block):
        self._block = block

    def getHardwarePower(self):
        return self.hardwarePower

    def mine(self, threshold):  # ALSO TAKE HASHED TXS FROM BLOCK INSTANCE AS WELL AS MERKLE, THEN HASH UNTIL DIFFICULTY THRESHOLD MET
        flag = False
        x = -1
        print("entering miner")
        transactions = self._block.getTxs()
        print(transactions)
        print(self._block)

        self.stop_mine()
        print(self._nonce)

        ### set up complete, time to read all greened out text as well as comments to make sure im not forgetting anuthing before combining
        # and mining passed in information

        ###NEED TO GET RID OF WHILE AND MAKE IT RETURN NONCE AT A TIME, UPDATE START_MINE WHEN BLOCK IS PARSED, check if criteria is met, if so pass stop mine, miner number and mined
        ###block to append to chain

        '''
        while not flag:  # while flag is not true
            x += 1
            tempNonce = "coin" + str(x)
            # print(tempNonce)
            hashedCoin = str(sha256(tempNonce.encode('utf-8')).hexdigest())
            # print(hashedCoin)
            zeroStr = '0' * threshold

            if hashedCoin[0:threshold] == zeroStr:
                print("\nthreshold met")
                flag = True
                print(tempNonce)
                print(hashedCoin)
        '''
