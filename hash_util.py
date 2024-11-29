import hashlib
import json


def hash_string_256(string):
    return hashlib.sha256(string).hexdigest()


def hash_block(block):
    # Converts a block object to a dictionary
    # It's important to create the copy since we want to have the current state of the block. The original block can
    # change and therefore the output hash won't match up with the original
    hashable_block = block.__dict__.copy()
    hashable_block['transactions'] = [tx.to_ordered_dict() for tx in hashable_block['transactions']]
    # Hash the block by converting the block into a JSON object because the expected argument is a string.
    # We're hashing the block because we want to have a "signature" of the previous block. This signature can be used to
    # determine whether the previous block has been tampered with because the hashing algorithm should always be
    # able to reproduce the same hash when the exact values are given.
    return hash_string_256(json.dumps(hashable_block, sort_keys=True).encode())
