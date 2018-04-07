import time
from block import Block, BlockParams


class BlockChain():
    '''
        The Blockchain Class which links new blocks with previous block.
    '''

    def __init__(self, chain = None):

        if chain is None:
            self._initialise_blockchain() # ----- The entire block chain is stored in full_chain

        else:
            self._full_chain = chain

    @property
    def latest_block(self):
        return self._full_chain[-1]

    def generate_next_block(self, data):
        index = len(self._full_chain)
        previous_hash = self.latest_block.hash
        timestamp = int(time.time())

        params = BlockParams(index, previous_hash, timestamp, data)
        new_block = Block(params)
        self._full_chain.append(new_block)

    def _initialise_blockchain(self):
        self._full_chain = [Block.genesis_block()]

    def receive_new_block(self, new_block):
        previous_block = self.latest_block

        if not new_block.has_valid_index(previous_block):
            return False, 'invalid index'
        if not new_block.has_valid_previous_hash(previous_block):
            return False, 'invalid previous hash'
        if not new_block.has_valid_hash():
            return False, 'invalid hash'

        self._full_chain.append(new_block)

        return True, 'block valid'

    @property
    def full_chain(self):
        return self._full_chain

    @property
    def chain_length(self):
        return len(self.full_chain)

    @property
    def genesis_block(self):
        return self.full_chain[0]


#################
### TEST CODE ###
#################
if __name__ == '__main__':
    

    # -----  Create the blockchain and add the genesis block
    blockchain = BlockChain()

    num_of_blocks_to_add = 20

    # ----- Add blocks to the chain
    for i in range(0, num_of_blocks_to_add):

        data = "Hey! I'm block " + str(blockchain.latest_block.index + 1)
        # print data

        blockchain.generate_next_block(data)

        # ----- Tell everyone about it!
        print "Block #{} has been added to the blockchain!".format(blockchain.latest_block.index)
        print "Hash: {}\n".format(blockchain.latest_block.hashcode) 