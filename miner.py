from hashlib import sha256


class Miner:
    def __init__(self, id, hardwarePower):

        self._id = id
        self.hardwarePower = hardwarePower  # ?not to sure if this should be parsed in or determined later, however is a needed attribute

        self._mining = False
        self._block = None
        self._nonce = 0

    def start_mine(self, block,
                   threshhold):  # threshold to be determined randomly after every blockchain block appending
        self._block = block
        self._mining = True

    def stop_mine(self):
        self._mining = False
        self._block = None

    def handle_tick(self):

        self.mine(self._nonce)
        self._nonce = self._nonce + 1  # put this in mine function, after you know the hashed val is not valid for difficulty
        return self._block, self._id

    def getHardwarePower(self):
        return self.hardwarePower

    @staticmethod  # method that belongs to the class rather than to instances of the class
    def mine(threshold):  # ALSO TAKE HASHED TXS FROM BLOCK INSTANCE AS WELL AS MERKLE, THEN HASH UNTIL DIFFICULTY THRESHOLD MET
        flag = False
        x = -1

        ### need to combine all inputs: last hash and hashed txs bundle, then PoW that with nonce

        ###NEED TO GET RID OF WHILE AND MAKE IT RETURN NONCE AT A TIME, UPDATE START_MINE WHEN BLOCK IS PARSED, check if criteria is met, if so pass stop mine, miner number and mined
        ###block to append to chain

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

        # call func to add fully hashed block to chain. - from root

        # have to consider how this will fire, it needs to be able to build on last iteration count - as some miners will miss iterations per mine cycle -
        # maybe make an if that checks if the iteration count is 0? - maybe store iteration count + hash so will remember on the miners side

        # difficulty determined once per mine cycle (will be a loop inside a loop where outer is mine cycle -
        # outer is where dif is determined (and where blocks completed blocks could be appended) - and inner is until one cracks difficulty)
        # then append completed block to blockchain in outer loop

        # could have a counter in the inner loop that resets to 1 every 4 iterations (if there are 4 miners) then set </> thresholds comparing iteration counter
        # to miner hardware level, if lower then dont execute, else if == or higher then execute mine()
