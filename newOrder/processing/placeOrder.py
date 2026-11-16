import datetime
import tkinter as tk
import sql_call as call
from newOrder import orderScreen
from newOrder.processing import back as bBack

def back(frame):
    bBack.back(frame)   #Exit out of the frame
    
def placeOrder(accountID, window, total, vat, subtotal, newOrder_frame, orderArray):
    print("placeorder", total)
    listItems = []
            
    def finishPlacingOrder():
        date = datetime.datetime.now()
        date = str(date.strftime("%d") + "/" + date.strftime("%m") + "/" + date.strftime("%Y")) #Formats the date into DD/YY/YYYY
        state = "Waiting"   #Default state
        c = call.sq()
        cursor = c.cursor()
        
        #Subtract 1 from stock number for each item in the order array
        for i in orderArray:
            cursor.execute("""
                           UPDATE itemstock SET stock = stock-1 WHERE ID = ?
                           """,
                           (i,)) 
            c.commit()
        
        #Writing order to database
        orderString = str(orderArray)   #Convert array to string
        cursor.execute('''
                        INSERT INTO orders(accountID,menuItems,date,priceTotal,state)  VALUES(?,?,?,?,?)
                        ''',
                        (accountID,orderString,date,total,state,))
        c.commit()
        cursor.close()
        
        confirmOrder.place_forget()
        newOrder_frame.place_forget()
        orderScreen.newOrder(accountID, window) #Refreshes order screen to default
        
    
    confirmOrder  = tk.Frame(newOrder_frame,
                                highlightbackground = "gray",
                                highlightthickness = "1",
                                height = 300,
                                width = 400)
    confirmOrder.place(x = 162,
                       y = 86)
    
    completeOrderButton = tk.Button(confirmOrder,
                                    text = "Confirm",
                                    font = ('Arial', 15),
                                    width = 13,
                                    command = finishPlacingOrder)
    completeOrderButton.place(x = 165,
                                y = 250)
    
    backButton = tk.Button(confirmOrder,
                            text = "Back",
                            font = ('Arial', 15),
                            width = 13,
                            command = lambda: back(confirmOrder))
    backButton.place(x = 5,
                        y = 250)
    
    finalTotal = tk.Label(confirmOrder,
                        text = f"Total: £{total:.2f}",
                        font = ('Arial', 10))
    finalTotal.place(x = 5,
                        y = 225)
    
    finalSubtotal = tk.Label(confirmOrder,
                            text = f"Subtotal: £{subtotal:.2f}",
                            font = ('Arial', 10))
    finalSubtotal.place(x = 5,
                        y = 205)
    
    finalVAT = tk.Label(confirmOrder,
                        text = f"VAT: £{vat:.2f}",
                        font = ('Arial', 10))
    finalVAT.place(x = 5,
                    y = 185)
    
    itemsList = tk.Listbox(confirmOrder,
                            height = 10,
                            width = 50)
    itemsList.place(x = 5,
                    y = 5)
    
    
    c = call.sq()
    cursor = c.cursor()
    for i in orderArray:
        cursor.execute('''
                        SELECT name,price FROM itemstock WHERE id = ?
                        ''',
                        (i,))
        itemTuple = cursor.fetchall()
        name = itemTuple[0][0]
        price = itemTuple[0][1]
        listItems.append([name, price])
        itemsList.insert(tk.END, f"{name}, £{price:.2f}")   #Displays all items in the order for final frame
        #print(listItems)