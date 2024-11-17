blockchain = []


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

# Adds transaction to the blockchain
def add_transaction(transaction_amount, last_transaction=[1]):
    # If no last transaction exists (because the blockchain is new), add a default transaction
    if last_transaction == None:
        last_transaction = [1]
    # Add the new transaction to the end of the blockchain
    # New transactions consist of the last block in the chain saved in the new block with the new transaction amount
    blockchain.append([last_transaction, transaction_amount])


# Ask the user the transaction amount
def get_transaction_value():
    # Since we're working with money, we need a floating point number
    user_input = float(input('Your transaction amount please: '))
    return user_input


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
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
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
