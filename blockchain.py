
class Blockchain:
    def __init__(self):
        self._blockHeight = None
        self.chain = ["Genesis"]  # need to hash this - or just hash the raw data?

    def addToChain(self, block):
        self.chain.append(block)  # fully hashed block

    def getChainHeight(self):
        self._blockHeight = len(self.chain)  # updates then returns the blockHeight
        return self._blockHeight

    def getChain(self):
        chain_strs = []
        for block in self.chain:
            chain_strs.append(str(block))  # Convert to actually readable format
        return chain_strs
