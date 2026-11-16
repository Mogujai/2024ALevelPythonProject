import sql_call as sql
from stock import viewStock

def addNumber(name, number: int, window):
    c = sql.sq()
    cursor = c.cursor()
    cursor.execute("""
                   SELECT stock FROM itemstock WHERE name = ?
                   """,
                   (name,))
    number += int(cursor.fetchone()[0])
    
    cursor.execute("""
                   UPDATE itemstock SET stock = ? WHERE name = ?
                   """,
                   (number, name,))
    c.commit()
    cursor.close()
    
    viewStock.viewStock(window)
    
def addNewStock(category, name, price: float, stock: int, window):
    c = sql.sq()
    cursor = c.cursor()
    cursor.execute("""
                   INSERT INTO itemstock(name,price,category,stock) VALUES(?,?,?,?)
                   """,
                   (name, price, category, stock,))
    c.commit()
    cursor.close()
    
    viewStock.viewStock(window)