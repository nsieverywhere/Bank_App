import sqlite3
import uuid


# Create customer table if not exists
def create_customer_table():
    conn = connect_customer_db()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS customers (id TEXT PRIMARY KEY, name TEXT, age INTEGER, gender TEXT, address TEXT, phone_number TEXT, account_number INTEGER)')
    conn.commit()
    conn.close()

# create a bank table if not exists


def create_bank_table():
    conn = connect_bank_db()
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS bank (account_number INTEGER PRIMARY KEY, balance INTEGER)')
    conn.commit()
    conn.close()


# Connect to the customer database
def connect_customer_db():
    return sqlite3.connect('./db/database.db')

# connects to bank db


def connect_bank_db():
    return sqlite3.connect('./db/bank.db')


# check if customer exists
def check_customer_exist(name, phone_number):
    create_customer_table()
    create_bank_table()
    try:
        conn = connect_customer_db()
        cur = conn.cursor()
        cur.execute(
            'SELECT * FROM customers WHERE name = ? and phone_number = ?', (name, phone_number))
        result = cur.fetchone()
        if result:
            return True
        else:
            return False
    except sqlite3.Error as e:
        print("Error occurred while checking customer:", e)


# Save customer to the database
def save_customer(name, age, gender, address, phone_number, account_number, balance=0):
    checkingcx = check_customer_exist(name, phone_number)
    if not checkingcx:
        try:
            conn = connect_customer_db()
            conn2 = connect_bank_db()
            cur = conn.cursor()
            cur2 = conn2.cursor()
            customer_id = str(uuid.uuid4())
            cur.execute('INSERT INTO customers (id, name, age, gender, address, phone_number, account_number) VALUES (?, ?, ?, ?, ?, ?, ?)',
                        (customer_id, name, age, gender, address, phone_number, account_number))
            cur2.execute(
                'INSERT INTO bank (account_number, balance) VALUES (?, ?)', (account_number, balance))
            print("Customer details saved, and bank account created")
            conn.commit()
            conn2.commit()
            conn.close()
            conn2.close()
        except sqlite3.Error as e:
            print("Error occurred while saving customer:", e)
    else:
        print("Customer already exists")


#############################################
# bank db


# check if bank account exists

class banking:
    def check_bank_exist(account_number):
        try:
            conn = connect_bank_db()
            cur = conn.cursor()
            cur.execute('SELECT * FROM bank WHERE account_number = ?',
                        (account_number,))
            existing_account = cur.fetchone()
            if existing_account:
                return True
            else:
                return False
        except sqlite3.Error as e:
            print("Error occurred while checking customer:", e)

    def deposit(amount, account_number):
        conn = connect_bank_db()
        cur = conn.cursor()
        cur.execute(
            'UPDATE bank SET balance = balance + ? WHERE account_number = ?',
            (amount, account_number)
        )
        conn.commit()
        conn.close()

    def check_balance(account_number):
        conn = connect_bank_db()
        cur = conn.cursor()
        cur.execute('SELECT balance FROM bank WHERE account_number = ?',
                    (account_number,))
        balance = cur.fetchone()
        return balance
        conn.commit()
        conn.close()

    def withdraw(amount, account_number):
        conn = connect_bank_db()
        cur = conn.cursor()
        cur.execute(
            'UPDATE bank SET balance = balance - ? WHERE account_number = ?',
            (amount, account_number)
        )
        conn.commit()
        conn.close()
