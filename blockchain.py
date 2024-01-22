
class Blockchain:
    """
    Blockchain is used to create one instance 'blockchain' for every simulation/life-cycle of this program.

    The chain always starts with the Genesis block as every chain needs an initial link, which is inspired by Bitcoins
    initial Genesis block.
    """

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
            chain_strs.append(str(block))  # convert to actually readable format
        return chain_strs
