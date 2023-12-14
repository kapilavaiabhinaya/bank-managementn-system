# application.py

import sqlite3
from bottle import Bottle, route, run, template, request
import database  # Assuming this contains database related functions

# Connect to SQLite database
connection = sqlite3.connect("bank_management_db.db")

# Call set_up_database to create tables and insert sample data
database.set_up_database()

app = Bottle()

# Create a table named 'users_table'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users_table (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        date_of_birth DATE,
        address TEXT,
        contact_number TEXT,
        email TEXT
    )
''')

# Create a table named 'accounts_table'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts_table (
        account_number TEXT PRIMARY KEY,
        user_id INTEGER,
        account_type TEXT,
        balance DECIMAL(10, 2),
        FOREIGN KEY (user_id) REFERENCES users_table(user_id)
    )
''')

# Create a table named 'transactions_table'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions_table (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_number TEXT,
        transaction_type TEXT,
        amount DECIMAL(10, 2),
        transaction_date DATETIME,
        description TEXT,
        FOREIGN KEY (account_number) REFERENCES accounts_table(account_number)
    )
''')

# Save (commit) the changes
connection.commit()

@app.route('/')
def index():
    # Fetch data from 'users_table', 'accounts_table', and 'transactions_table' tables using a JOIN
    cursor.execute('''
        SELECT users_table.user_id, users_table.first_name, users_table.last_name,
               accounts_table.account_number, accounts_table.account_type, accounts_table.balance,
               transactions_table.transaction_type, transactions_table.amount,
               transactions_table.transaction_date, transactions_table.description
        FROM users_table
        LEFT JOIN accounts_table ON users_table.user_id = accounts_table.user_id
        LEFT JOIN transactions_table ON accounts_table.account_number = transactions_table.account_number
    ''')
    data = cursor.fetchall()

    return template('index', data=data)

# Add routes for adding, updating, and deleting users, accounts, and transactions

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
