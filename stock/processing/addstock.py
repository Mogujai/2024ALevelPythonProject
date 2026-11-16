import tkinter as tk
from tkinter import ttk
import sql_call as sql
from newOrder.processing import back
from stock.processing import addtostock


def addstock(window, results):
    itemnames = []
    
    viewStock_frame = tk.Frame(window,
                               highlightbackground = "gray",
                               highlightthickness = 1,
                               height = 474,
                               width = 724)
    viewStock_frame.place(x = 126,
                          y = 2)
    
    for i in results:
        itemnames.append(i[0])
    
    itemListbox = tk.Listbox(viewStock_frame,
                             height = 12,
                             width = 50)
    itemListbox.place(x = 6,
                      y = 6)
     
    selectStock = ttk.Combobox(viewStock_frame,
                               font = ('Arial',12),
                               values = itemnames)
    selectStock.place(x = 6,
                      y = 310)
    
    insertValue_label = tk.Label(viewStock_frame,
                                 text = "Number to add",
                                 font = ('Arial',12))
    insertValue_label.place(x = 6,
                            y = 340)
    
    insertValue_text = tk.Text(viewStock_frame,
                               width = 16,
                               height = 1,
                               font = ('Arial',12))
    insertValue_text.place(x = 6,
                           y = 360)
    

    addStockNumber_button = tk.Button(viewStock_frame,
                                      text = "Confirm",
                                      activebackground = "gray",
                                      activeforeground = "white",
                                      cursor = "hand2",
                                      height = 2,
                                      width = 15,
                                      font = ('Arial', 12),
                                      command = lambda: addtostock.addNumber(selectStock.get(), insertValue_text.get("1.0","end-1c"), window)) #Adding number to existing stock number for selected item
    addStockNumber_button.place(x = 6,
                                y = 390)
    
    addNew_label = tk.Label(viewStock_frame,
                            text = "Add new item",
                            font = ('Arial',30))
    addNew_label.place(x = 400,
                       y = 6)
    
    category_label = tk.Label(viewStock_frame,
                              text = "Category",
                              font = ('Arial',12))
    category_label.place(x = 400,
                         y = 150)
    category_list = ttk.Combobox(viewStock_frame,
                                 font = ('Arial',12),
                                 values = ["Fish", "Sausages & Chicken", "Chips", "Extra", "Drinks"])
    category_list.place(x = 400,
                        y = 170)
    
    addNewName_label = tk.Label(viewStock_frame,
                                text = "Name",
                                font = ('Arial',12))
    addNewName_label.place(x = 400,
                           y = 200)
    addNewName_text = tk.Text(viewStock_frame,
                              width = 16,
                              height = 1,
                              font = ('Arial',12))
    addNewName_text.place(x = 400,
                          y = 220)
    
    addNewPrice_label = tk.Label(viewStock_frame,
                                 text = "Price",
                                 font = ('Arial',12))
    addNewPrice_label.place(x = 400,
                            y = 250)
    addNewPrice_text = tk.Text(viewStock_frame,
                               width = 16,
                               height = 1,
                               font = ('Arial',12))
    addNewPrice_text.place(x = 400,
                           y = 270)
    
    addNewStock_label = tk.Label(viewStock_frame,
                                 text = "Stock Number",
                                 font = ('Arial',12))
    addNewStock_label.place(x = 400,
                            y = 300)
    addNewStock_text = tk.Text(viewStock_frame,
                               width = 16,
                               height = 1,
                               font = ('Arial',12))
    addNewStock_text.place(x = 400,
                           y = 320)
    
    addNewStock_button = tk.Button(viewStock_frame,
                                   text = "Add new stock",
                                   activebackground = "gray",
                                   activeforeground = "white",
                                   cursor = "hand2",
                                   height = 2,
                                   width = 15,
                                   font = ('Arial', 12),
                                   command = lambda: addtostock.addNewStock(category_list.get(),    #Adding new items to the stock record
                                                                            addNewName_text.get("1.0","end-1c"), 
                                                                            addNewPrice_text.get("1.0","end-1c"), 
                                                                            addNewStock_text.get("1.0","end-1c"), 
                                                                            window))
    addNewStock_button.place(x = 400,
                             y = 390)
    
    back_button = tk.Button(viewStock_frame,
                            text = "x",
                            height = 2,
                            width = 2,
                            command = lambda: back.back(viewStock_frame))
    back_button.place(x = 690,
                      y = 6)
    
    for i in results:
        string = f"Item: {i[0]}, Stock: {i[1]}"
        itemListbox.insert(tk.END, string)
        

    