import sql_call as sql
import tkinter as tk
from viewOrder.processing import refresh


def buttonUpdateRight(id, waiting, in_progress, completed):    
    
    #Updating states via buttons
    c = sql.sq()
    cursor = c.cursor()
    cursor.execute("""
                   SELECT orderID,state FROM orders WHERE orderID = ?
                   """,
                   (id,))
    data = cursor.fetchall()
    #print(data) TEST
    
    #Setting new states
    if data[0][-1] == "Waiting":
        newState = "In Progress"
    elif data[0][-1] == "In Progress":
        newState = "Completed"
    elif data[0][-1] == "Completed":
        newState = "Collected"
        
    cursor.execute("""
                   UPDATE orders SET state = ? WHERE orderID = ?
                   """,
                   (newState, id,))
    c.commit()
    cursor.close()
    refresh.refresh(waiting, in_progress, completed)
    
def buttonUpdateLeft(id, waiting, in_progress, completed):
    c = sql.sq()
    cursor = c.cursor()
    cursor.execute("""
                   SELECT orderID,state FROM orders WHERE orderID = ?
                   """,
                   (id,))
    data = cursor.fetchall()
    
    #Setting new states
    if data[0][-1] == "In Progress":
        newState = "Waiting"
    elif data[0][-1] == "Completed":
        newState = "In Progress"
        
    cursor.execute("""
                   UPDATE orders SET state = ? WHERE orderID = ?
                   """,
                   (newState, id,))
    c.commit()
    cursor.close()
    refresh.refresh(waiting, in_progress, completed)
    
    