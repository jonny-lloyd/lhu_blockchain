from run import *

if __name__ == '__main__':
    do_run()









#########################################################################
# need to do:
# miners can rearrange txs to make small miners able to compete(ask mark), thinking something trivial like 1/10 chance they’ll rearrange the block when it is received, or maybe that’ll increase the lower the hardware capabilities of the miners 1/5, 1/3, etc.
# create sim mempool for txs? help make miners make different blocks, more random making it easier for worse hardware nodes--

# PROGRAM LOG:
# took nonce hashing algo and txs generator from another file where i experimented with it until it was ok for this program -- generate 10 random hash strings to simulate a bundle of individually hashed txs presented for a miner to hash then place in a block--
# cut away most of the implementation of my mining logic (while loop) to be replaced with a tick based system, where each miner mines sequentially based on their hardware capabilities, then returns the nonce, easing the whole process --
# local_block = Block(blockchain.chain[0]) if genesis or not logic implementation -- blockchain appends and references last block even if genesis, however genesis still generates txs--
# got all of the set up out of the way before actually using the miner_tick yet -- miner_tick now has functionality, where it is parsed in information, distributed correctly (local block stored in miner when start_mine fires, as well as threshold is now passed to mine())--
# completed cleaned and finished txs class -- start and stop mine functions both work and are useful (stores local block, then clears local block and nonce when stopped)
# miner correctly hashes and produces pow -- implement multiple miners with loopCounter = -1 logic (remember when doing writeup to include that i built a loopCounter prototype beforehand which was then implemented with miners)
# if found: running = False  # simulated full node majority validation -- loopCounter now uses the miners hardware level -- still relying on breaks for loop exiting - removed inner loop --
# loopCounter NEEDS TO BE RESET TO 0 WHEN VALID BLOCK FOUND (if within every loopCounter condition, if yes then set to -1?) -- return miner number, parallel miner id array, print when blockchain is printed? say in diss that 1 was winning constantly after many simulations so not good enough representation of IRL even tho hardware taken into account--
# finally updates nonce tag before block is added, also prints entirety of worked block --
#
