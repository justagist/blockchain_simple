from block import BlockParams
from blockchain import BlockChain


class BlockChainTester():
    '''
        A simple class to test the validity of a blockchain

    '''
    def __init__(self, blockchain):

        self.blockchain_ = blockchain

        self._create_validator_chain()


    def validate(self):
        '''
            This function checks the validity of the blockchain

        '''
        def genesis_block_is_valid(chain):
            '''
                This function checks if the genesis block is as defined in block.py

            '''
            return chain.genesis_block.parameters == BlockParams.get_genesis_params()


        def validate_chain_sequence(true_chain, validator_chain, verbose = False):
            '''
                This function checks if the blocks in true_chain are valid by checking their index, hash, and hash of previous block

            '''

            for idx in range(1, true_chain.chain_length):

                valid, status = validator_chain.receive_new_block(true_chain.full_chain[idx])

                if verbose:
                    print "Block %d : Validity"%idx, status

                if not valid:
                    return False

            return True



        print "Genesis valid\n" if genesis_block_is_valid(self.validator_chain_) else "Invalid Genesis\n"

        print "Chain valid" if validate_chain_sequence(self.blockchain_, self.validator_chain_, verbose = True) else "Blockchain invalid"


    def _create_validator_chain(self):
        '''
            Create a chain with the same genesis block. Blocks from the test chain will be added to this chain by verifying the validity of the chain.

        '''

        self.validator_chain_ = BlockChain(chain = [self.blockchain_.genesis_block])



#################
### TEST CODE ###
#################
if __name__ == '__main__':
    

    # -----  Create the blockchain and add the genesis block
    blockchain = BlockChain()

    num_of_blocks_to_add = 20

    # ----- Gernerate a block chain by adding blocks to the chain
    for i in range(0, num_of_blocks_to_add):

        data = "Hey! I'm block " + str(blockchain.latest_block.index + 1)
        blockchain.generate_next_block(data)

    # ----- validate the blockchain
    BlockChainTester(blockchain).validate()
