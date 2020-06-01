# To implement the block chain I have used LinkedList.
#
# A new block is added to the head of List, which makes the
# insertion O(1).
#
# To make the hash unique regardless of the data being entered
# I have hashed the data along with current timestamp.

import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        # timestamp is added to hash in order to make it unique
        hash_str = f"{self.data}{self.timestamp}".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return f"Timestamp:{self.timestamp}\nDate:{self.data}\nSHA256:{self.hash}\nPrev_Hash:{self.previous_hash}"


class BlockChain:

    def __init__(self):
        self.head = None

    def add_block(self, data):
        previous_hash = self.head.hash if self.head else "0"
        block = Block(datetime.utcnow(), data, previous_hash)
        block.next = self.head
        self.head = block

    def print_chain(self):
        temp = self.head

        while temp:
            print(temp, "\n")
            temp = temp.next


# Prints 3 blocks
print("Test 1")
print("------")
blockchain = BlockChain()
blockchain.add_block('123')
blockchain.add_block('345')
blockchain.add_block('567')
blockchain.print_chain()

# Prints no blocks
print("Test 2")
print("------")
blockchain = BlockChain()
blockchain.print_chain()

# Prints 1 block
print("Test 3")
print("------")
blockchain = BlockChain()
blockchain.add_block("123")
blockchain.print_chain()
