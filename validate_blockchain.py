from block import BlockParams
from blockchain import BlockChain


class BlockChainTester():

    def __init__(self, blockchain):

        self.blockchain_ = blockchain

        self._create_validator_chain()


    def validate(self):

        def genesis_block_is_valid(chain):

            return chain.genesis_block.parameters == BlockParams.get_genesis_params()


        def validate_chain_sequence(true_chain, validator_chain, verbose = False):

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

        self.validator_chain_ = BlockChain(chain = [self.blockchain_.genesis_block])



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
        # print "Block #{} has been added to the blockchain!".format(blockchain.latest_block.index)
        # print "Hash: {}\n".format(blockchain.latest_block.hashcode) 


    validator = BlockChainTester(blockchain)

    validator.validate()