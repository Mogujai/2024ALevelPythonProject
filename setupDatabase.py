import sqlite3 as sql

def setup():
    conn = sql.connect('mF.db')
    cursor = conn.cursor()
    
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS accounts (
                       accountID INTEGER PRIMARY KEY AUTOINCREMENT,
                       username TEXT,
                       password TEXT,
                       accessLevel INTEGER
                   );
                   ''')
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS accountsDetails (
                       accountID INTEGER,
                       firstName TEXT,
                       surName TEXT,
                       email TEXT,
                       phoneNumber TEXT,
                       address TEXT,
                       FOREIGN KEY (accountID) REFERENCES accounts (accountID)
                   );
                   ''')
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS orders(
                       orderID INTEGER PRIMARY KEY AUTOINCREMENT,
                       accountID INTEGER,
                       menuItems,
                       date,
                       priceTotal REAL,
                       state
                    );
                   ''')
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS itemstock (
                       ID INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       price REAL,
                       category TEXT,
                       stock INTEGER
                   );
                   ''')
    conn.commit()
    conn.close()
    
setup()
