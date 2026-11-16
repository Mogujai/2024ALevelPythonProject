import tkinter as tk
import sql_call as sql
from stock.processing import addstock


def viewStock(window):
    
    c = sql.sq()
    cursor = c.cursor()
    cursor.execute("""
                   SELECT name,stock FROM itemstock
                   """)
    results = cursor.fetchall()
    #print(results)
    
    viewStock_frame = tk.Frame(window,
                               highlightbackground = "gray",
                               highlightthickness = 1,
                               height = 474,
                               width = 724)
    viewStock_frame.place(x = 126,
                          y = 2)
    
    #Refreshing the frame
    for widget in viewStock_frame.winfo_children():
        widget.destroy()
    
    stock_Listbox = tk.Listbox(viewStock_frame,
                               height = 24,
                               width = 110)
    stock_Listbox.place(x = 6,
                        y = 6)
    
    addStock = tk.Button(viewStock_frame,
                         text = "Add Stock",
                         height = 4,
                         width = 15,
                         command = lambda: addstock.addstock(window, results)) #Passing results
    addStock.place(x = 6,
                   y = 400)
    
    for i in results:
        string = f"Item: {i[0]}, Stock: {i[1]}"
        stock_Listbox.insert(tk.END, string)    #Inserting all stock items and their stock number into the listbox
    
    