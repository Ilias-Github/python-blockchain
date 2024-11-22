import hashlib
import json


def hash_string_256(string):
    return hashlib.sha256(string).hexdigest()


def hash_block(block):
    # Hash the block by converting the block into a JSON object because the expected argument is a string.
    # We're hashing the block because we want to have a "signature" of the previous block. This signature can be used to
    # determine whether the previous block has been tampered with because the hashing algorithm should always be
    # able to reproduce the same hash when the exact values are given.
    return hash_string_256(json.dumps(block, sort_keys=True).encode())
