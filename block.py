import datetime as date
import hashlib

# ====== Params for the Genesis block ========
genesis_params = {
'GENESIS_INDEX':0,
'GENESIS_PREVIOUS_HASH':'0',
'GENESIS_TIMESTAMP':1495851743,
'GENESIS_DATA':'There was no one before me!'
}
# ============================================

class BlockParams():
    '''
        Parameters for each block: 
            1. Index of the block (prev + 1)
            2. Hash of the previous block in chain
            3. Timestamp
            4. The data to be stored in block
    '''
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data

    def __str__(self):
        '''
            Redifine str function for BlockParams objects
    
        '''
        return str(self.index) + self.previous_hash + str(self.timestamp) + self.data

    def __eq__(self, other):
        '''
            Redifine equality function for BlockParams objects
            
        '''
        return self.index == other.index and self.previous_hash == other.previous_hash and self.timestamp == other.timestamp and self.data == other.data

    @classmethod
    def get_genesis_params(cls):
        # ----- The hardcoded parameters for the genesis block
        return cls(genesis_params['GENESIS_INDEX'], genesis_params['GENESIS_PREVIOUS_HASH'], genesis_params['GENESIS_TIMESTAMP'], genesis_params['GENESIS_DATA'])


class Block:
    '''
        Blocks forming the block chain initialised with a BlockParams object
    '''

    def __init__(self, params):
        self.index = params.index
        self.previous_hash = params.previous_hash
        self.timestamp = params.timestamp
        self.data = params.data
        self.hash = self.hashcode

    @property
    def parameters(self):
        return BlockParams(
            self.index,
            self.previous_hash,
            self.timestamp,
            self.data
        )

    @classmethod
    def genesis_block(cls):
        params = BlockParams.get_genesis_params()
        return cls(params)

    @property
    def hashcode(self):
        return hashlib.sha256(str(self.parameters).encode()).hexdigest()


    def has_valid_index(self, previous_block):
        return self.index == previous_block.index + 1

    def has_valid_previous_hash(self, previous_block):
        return self.previous_hash == previous_block.hash

    def has_valid_hash(self):
        return self.hashcode == self.hash