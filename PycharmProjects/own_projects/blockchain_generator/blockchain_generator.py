import random
import time


class Blockchain:

    def __init__(self, number_of_block, own_hash, last_block_hash):
        self.number_of_block = number_of_block
        self.own_hash = own_hash
        self.last_block_hash = last_block_hash

    def __repr__(self):
        return f"Blok nr: {self.number_of_block}\nlast # : {self.last_block_hash}\n# \t   : {self.own_hash}\n{self.visual_end_of_block} "

    visual_end_of_block = "_" * 25


used_hashs = []


def did_i_used_this_hash(hash):
    if hash in used_hashs:
        return True
    else:
        used_hashs.append(hash)


def start_generating_blockchain():
    last_block_hash = str(0).zfill(16)
    block_number = 1
    while True:
        pre_own_hash = str(random.randint(1, 9_999_999_999_999_999))
        own_hash = pre_own_hash.zfill(16)
        time.sleep(2.5)

        if did_i_used_this_hash(own_hash):
            continue

        block = Blockchain(block_number, own_hash, last_block_hash)
        print(block)
        print()
        last_block_hash = own_hash
        block_number += 1


if __name__ == '__main__':
    start_generating_blockchain()
