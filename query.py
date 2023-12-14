import sqlite3

connection = sqlite3.connect("bank_management_db.db")
cursor = connection.cursor()

# Fetch data from the 'users_table' table
cursor.execute("SELECT user_id, first_name, last_name, date_of_birth, address, contact_number, email FROM users_table")
user_rows = list(cursor.fetchall())

# Fetch data from the 'accounts_table' table
cursor.execute("SELECT account_number, user_id, account_type, balance FROM accounts_table")
account_rows = list(cursor.fetchall())

# Fetch data from the 'transactions_table' table
cursor.execute("SELECT transaction_id, account_number, transaction_type, amount, transaction_date, description FROM transactions_table")
transaction_rows = list(cursor.fetchall())

print("Users:")
print(user_rows)

print("\nAccounts:")
print(account_rows)

print("\nTransactions:")
print(transaction_rows)

# Combine the data into a single list of dictionaries
user_data = [{'user_id': row[0], 'first_name': row[1], 'last_name': row[2], 'date_of_birth': row[3],
              'address': row[4], 'contact_number': row[5], 'email': row[6]} for row in user_rows]

account_data = [{'account_number': row[0], 'user_id': row[1], 'account_type': row[2], 'balance': row[3]} for row in account_rows]

transaction_data = [{'transaction_id': row[0], 'account_number': row[1], 'transaction_type': row[2],
                     'amount': row[3], 'transaction_date': row[4], 'description': row[5]} for row in transaction_rows]

print("\nCombined Data:")
combined_data = []

for user in user_data:
    related_accounts = [account for account in account_data if account['user_id'] == user['user_id']]
    user_copy = user.copy()
    user_copy['accounts'] = related_accounts
    combined_data.append(user_copy)

for account in account_data:
    related_transactions = [transaction for transaction in transaction_data if
                            transaction['account_number'] == account['account_number']]
    account_copy = account.copy()
    account_copy['transactions'] = related_transactions
    combined_data.append(account_copy)

print(combined_data)
