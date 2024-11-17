blockchain = []
# Transactions need to be processed before adding them to the blockchain
open_transactions = []
owner = 'Ilias'


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# Adds transaction to the blockchain
def add_transaction(transaction):
    # Dictionary because each key-value pair needs to be unique
    open_transactions.append(
        {
            'sender': transaction['sender'],
            'recipient': transaction['recipient'],
            'amount': transaction['amount']
        }
    )

def mine_block():
    pass

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
    is_valid = True

    for block_index in range(len(blockchain)):
        # Skip checking the first block because it's no use to check the first block when there are no previous blocks
        if block_index == 0:
            continue
        # Check if the first element of a block is equal to the previous block
        # The first element is always the entire previous block
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False

    return is_valid


waiting_for_input = True

while waiting_for_input:
    # Menu for the user to interact with the blockchain
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')

    user_choice = get_user_choice()

    if user_choice == '1':
        transaction = get_transaction_value_and_recipient()
        add_transaction(transaction)
        print(open_transactions)
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        # Manipulate the blockchain to check its integrity
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break
else:
    print('User left!')


print('Done!')
