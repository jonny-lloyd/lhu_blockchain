

class Blockchain:
    def __init__(self):
        self.blockHeight = 0
        self.chain = ["Genesis"]  # need to hash this - or just hash the raw data?
        #  self.merkle = merkle

    def addToChain(self, block):
        self.chain.append(block)  # fully hashed block

    def getChainHeight(self):
        self.blockHeight = len(self.chain)  # updates then returns the blockHeight
        return self.blockHeight

    # def getChainHeight(self):
    #    return self.blockHeight

    def getChain(self):
        chain_strs = []
        for block in self.chain:
            chain_strs.append(str(block))  # Convert to actually readable format
        return chain_strs

    # get last block hash
    #   use get chain to only get hash of last block, len-1 or something