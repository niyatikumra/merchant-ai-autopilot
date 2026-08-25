transactions = []


def save_transaction(transaction):
    transactions.append(transaction)
    return transaction


def get_all_transactions():
    return transactions