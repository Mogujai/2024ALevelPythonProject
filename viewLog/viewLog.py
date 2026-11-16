import tkinter as tk
import sql_call as sql

def viewLog(window):
    viewLog_frame = tk.Frame(window,
                             highlightbackground = "gray",
                             highlightthickness = 1,
                             height = 474,
                             width = 724)
    viewLog_frame.place(x = 126,
                        y = 2)
    
    #Refreshing the frame every time the button is clicked
    for widget in viewLog_frame.winfo_children():
        widget.destroy()
    
    logList = tk.Listbox(viewLog_frame,
                         height = 28,
                         width = 110)
    logList.place(x = 6,
                  y = 6)
    
    c = sql.sq()
    cursor = c.cursor()
    cursor.execute("""
                   SELECT orderID,accountID,menuItems,date,priceTotal,state FROM orders
                   """)
    results = cursor.fetchall()
     
    for i in results:
        string = f"OrderID: {i[0]}, AccountID: {i[1]}, ItemsID: {i[2]}, Date: {i[3]}, Price: £{float(i[4]):.2f}, State: {i[5]}"
        logList.insert(tk.END, string)  #Inserting all related data into the log

    
    
    