# The very first block in the blockchain. Used to init the blockchain. No important information is stored.
genesis_block = {'previous_hash': '', 'transactions': []}
blockchain = [genesis_block]
# Transactions need to be processed before adding them to the blockchain
open_transactions = []
owner = 'Ilias'

# Participants are saved in a set because we don't want any duplicates in our userbase
# The name will be replaced by a unique identifier
participants = {'Ilias'}


def hash_block(block):
    """'Hash' a block by concatonating the data with hyphens in between"""
    # TODO: Apply real hashing
    return '-'.join([str(block[key]) for key in block])

def get_balance(participant):
    print('part: ' + participant)
    # Check every block in the blockchain for the where the given participant is the sender and save them to a list
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]

    # Calculate the total amount sent by the given participant
    amount_sent = 0
    for tx in tx_sender:
        # Cannot add something if it doesn't exist
        if len(tx) > 0:
            amount_sent += tx[0]

    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]

    # Calculate the total amount sent by the given participant
    amount_received = 0
    for tx in tx_recipient:
        # Cannot add something if it doesn't exist
        if len(tx) > 0:
            amount_received += tx[0]

    return amount_sent - amount_received

def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# Adds transaction to the blockchain
def add_transaction(transaction):
    sender = transaction['sender']
    recipient = transaction['recipient']
    # Dictionary because each key-value pair needs to be unique
    open_transactions.append(
        {
            'sender': sender,
            'recipient': recipient,
            'amount': transaction['amount']
        }
    )
    # Because we use a set, duplicates will be ignored automatically
    participants.add(sender)
    participants.add(recipient)


def mine_block():
    # Get the last block in the chain to save as a hash in the new block
    last_block = blockchain[-1]
    # Hash the block using the predefined hashing function
    hashed_block = hash_block(last_block)
    # The new block saves the previous block as a hash
    block = {'previous_hash': hashed_block, 'transactions': open_transactions}
    # TODO: add validation to the transactions
    blockchain.append(block)

    return True


# The recipient and amount is important to know when making a transaction
def get_transaction_value_and_recipient():
    recipient = input('Enter the name of the recipient: ')
    amount = float(input('Enter the amount you want to send: '))
    return {'sender': owner, 'recipient': recipient, 'amount': amount}


# User keyboard input
def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


# Print all the blocks in the chain
def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)
    # Else is always executed after the loop is finished
    else:
        print('-' * 20)


# Verify if the blockchain isn't manipulated
def verify_chain():
    # Enumerate adds a counter to an iterable
    for (index, block) in enumerate(blockchain):
        # The first block doesn't have any other block to compare to so skip it
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            print('prev ' + block['previous_hash'])
            print('next ' + hash_block(blockchain[index - 1]))
            return False
    return True

waiting_for_input = True

while waiting_for_input:
    # Menu for the user to interact with the blockchain
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('h: Manipulate the chain')
    print('q: Quit')

    user_choice = get_user_choice()

    if user_choice == '1':
        transaction = get_transaction_value_and_recipient()
        add_transaction(transaction)
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            # Set the open transactions to an empty list because they're all processed
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'h':
        # Manipulate the blockchain to check its integrity
        if len(blockchain) >= 1:
            blockchain[0] = {'previous_hash': 'asdfasdf', 'transactions': [{'sender': 'chris', 'recipient': 'Max', 'amount': 30.9}]}
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
        verify_chain()
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break
    print(get_balance(owner))
else:
    print('User left!')

print('Done!')
