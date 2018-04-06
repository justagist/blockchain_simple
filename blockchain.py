import time
from block import Block, BlockParams


class BlockChain():
    '''
        The Blockchain Class which links new blocks with previous block.
    '''

    def __init__(self):
        self._full_chain = self._initialise_blockchain() # ----- The entire block chain is stored in full_chain

    def get_latest_block(self):
        return self._full_chain[-1]

    def generate_next_block(self, data):
        index = len(self._full_chain)
        previous_hash = self.get_latest_block().hash
        timestamp = int(time.time())

        params = BlockParams(index, previous_hash, timestamp, data)
        new_block = Block(params)
        self._full_chain.append(new_block)

    def _initialise_blockchain(self):
        return [Block.genesis_block()]

    def receive_new_block(self, new_block):
        previous_block = self.get_latest_block()

        if not new_block.has_valid_index(previous_block):
            print('invalid index')
            return
        if not new_block.has_valid_previous_hash(previous_block):
            print('invalid previous hash')
            return
        if not new_block.has_valid_hash():
            print('invalid hash')
            return

        self._full_chain.append(new_block)


#################
### TEST CODE ###
#################
if __name__ == '__main__':
    

    # -----  Create the blockchain and add the genesis block
    blockchain = BlockChain()

    num_of_blocks_to_add = 20

    # ----- Add blocks to the chain
    for i in range(0, num_of_blocks_to_add):

        data = "Hey! I'm block " + str(blockchain.get_latest_block().index + 1)
        print data

        blockchain.generate_next_block(data)

        # ----- Tell everyone about it!
        print "Block #{} has been added to the blockchain!".format(blockchain.get_latest_block().index)
        print "Hash: {}\n".format(blockchain.get_latest_block().hash) 