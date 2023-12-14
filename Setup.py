# setup.py

from setuptools import setup

setup(
    name='your_app_name',
    version='1.0',
    packages=['your_app_name'],
    install_requires=[
        'bottle',
        'sqlite3',
    ],
    entry_points={
        'console_scripts': [
            'your_app_name = your_app_name.application:main',
        ],
    },
)
import sqlite3

connection = sqlite3.connect("bank_management_db.db")

cursor = connection.cursor()

try:
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS accounts")
    cursor.execute("DROP TABLE IF EXISTS transactions")
except Exception as e:
    print(f"Error dropping tables: {e}")

# Create the 'users' table
try:
    cursor.execute("CREATE TABLE users (user_id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, date_of_birth DATE, address TEXT, contact_number TEXT, email TEXT)")
except Exception as e:
    print(f"Error creating 'users' table: {e}")

# Create the 'accounts' table
try:
    cursor.execute("CREATE TABLE accounts (account_number INTEGER PRIMARY KEY, user_id INTEGER, account_type TEXT, balance DECIMAL(10, 2), FOREIGN KEY (user_id) REFERENCES users(user_id))")
except Exception as e:
    print(f"Error creating 'accounts' table: {e}")

# Create the 'transactions' table
try:
    cursor.execute("CREATE TABLE transactions (transaction_id INTEGER PRIMARY KEY, account_number INTEGER, transaction_type TEXT, amount DECIMAL(10, 2), transaction_date DATETIME, description TEXT, FOREIGN KEY (account_number) REFERENCES accounts(account_number))")
except Exception as e:
    print(f"Error creating 'transactions' table: {e}")

# Insert sample data into 'users' table
users_data = [
    ('John', 'Doe', '1990-01-01', '123 Main St', '555-1234', 'john@example.com'),
    ('Jane', 'Smith', '1985-05-15', '456 Oak St', '555-5678', 'jane@example.com'),
    # Add more users as needed
]

for user_data in users_data:
    try:
        cursor.execute("INSERT INTO users (first_name, last_name, date_of_birth, address, contact_number, email) VALUES (?, ?, ?, ?, ?, ?)", user_data)
    except Exception as e:
        print(f"Error inserting data into 'users' table: {e}")

# Insert sample data into 'accounts' table
accounts_data = [
    (1, 'Savings', 1000.00),
    (2, 'Checking', 500.50),
    # Add more accounts as needed
]

for account_data in accounts_data:
    try:
        cursor.execute("INSERT INTO accounts (user_id, account_type, balance) VALUES (?, ?, ?)", account_data)
    except Exception as e:
        print(f"Error inserting data into 'accounts' table: {e}")

# Insert sample data into 'transactions' table
transactions_data = [
    (1, 'Deposit', 500.00, '2023-01-15', 'Initial deposit'),
    (2, 'Withdrawal', 50.25, '2023-01-20', 'Grocery shopping'),
    # Add more transactions as needed
]

for transaction_data in transactions_data:
    try:
        cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount, transaction_date, description) VALUES (?, ?, ?, ?, ?)", transaction_data)
    except Exception as e:
        print(f"Error inserting data into 'transactions' table: {e}")

connection.commit()
connection.close()
print("done.")
