import sqlite3 as sql

def addUserPass():
    username = input("Username to add: ")
    password = input("Password to add: ")
    access = int(input("Access level: "))
    
    with sql.connect("mF.db") as db:
        cursor = db.cursor()
        
        cursor.execute('''
                       INSERT INTO accounts(username,password,accessLevel) VALUES(?,?,?)
                       ''',
                       (username, password, access))
        db.commit()
        cursor.close()
    
    
def addStock():
    with sql.connect("mF.db") as edb:
        cursor = edb.cursor()
        
        cursor.execute('''
                       SELECT id FROM itemstock
                       ''')
        results = cursor.fetchall()
        
    print(results)
    
    name = input("Name: ")
    price = input("Price: £")
    category = input("Category: ")
    stock = input("Stock Number: ")
    
    with sql.connect("mF.db") as db:
        cursor = db.cursor()
        
        cursor.execute('''
                       INSERT INTO itemstock(name,price,category,stock) VALUES(?,?,?,?)
                       ''',
                       (name, price, category, stock))
        db.commit()
        cursor.close()
    
