import tkinter as tk
import sql_call as call
from newOrder.processing import removeItem
from newOrder.processing import addDiscounts
from newOrder.processing import itemAdd

def newOrder(accountID, window):
    global d
    global orderArray
    orderArray = []
    d = 0
    
    #Main SQL call
    c = call.sq()
    cursor = c.cursor()
                           
    def callback(selection):    #Function to generate menu item buttons
        #print(selection) test
        cursor.execute('''
                       SELECT id,name,price FROM itemstock WHERE category = ?
                       ''',
                       (selection,))
        sInfo = cursor.fetchall()
        
        #Frame to contain the buttons
        items_frame = tk.Frame(item_frame,
                               highlightbackground = "gray",
                               highlightthickness = 1,
                               height = 428,
                               width = 372)
        items_frame.place(x = 3,
                          y = 40)

        posx = 5
        posy = 5
        for i in sInfo:
            #Button contains the item ID and item name needed for passing parameters
            menu_item = tk.Button(items_frame,
                                  text = (f"{i[1]} \n £{float(i[2]):.2f}"),
                                  height = 5,
                                  width = 15,
                                  wraplength = 120,
                                  command = lambda item_id = i[0], itemname = i[1]: itemAdd.iAdd(total_frame, accountID, window, newOrder_frame, item_id, itemname, orderArray, newOrderList, d, discounts_label, total_label, subtotal_label, vat_label))
            if posx > 250:
                posx = 5
                posy += 91
            
            menu_item.place(x = posx,
                            y = posy)
            posx += 122

    
    newOrder_frame = tk.Frame(window,
                              highlightbackground = "gray",
                              highlightthickness = 1,
                              height = 474,
                              width = 724)
    newOrder_frame.place(x = 126,
                         y = 2)
    item_frame = tk.Frame(newOrder_frame,
                          highlightbackground = "gray",
                          highlightthickness = 1,
                          height = 474,
                          width = 380)
    item_frame.place(x = -1,
                     y = -1)

    newOrderW_frame = tk.Frame(newOrder_frame,
                               highlightbackground = "gray",
                               highlightthickness = 1,
                               height = 260,
                               width = 340)
    newOrderW_frame.place(x = 383,
                          y = -1)

    newOrderW_title = tk.Frame(newOrderW_frame,
                               highlightbackground = "gray",
                               highlightthickness = 1,
                               height = 25,
                               width = 330)
    newOrderW_title.place(x = 4,
                          y = 4)
    
    newOrderW_tLabel = tk.Label(newOrderW_title,
                                text = "New Order",
                                font = ('Arial', 10))
    newOrderW_tLabel.place(x = 1,
                           y = 1)

    newOrderList = tk.Listbox(newOrderW_frame,
                              height = 10,
                              width = 55)
    newOrderList.place(x = 4,
                       y = 35)
    
    newOrderPop = tk.Button(newOrderW_frame,
                            text = "Remove",
                            height = 2,
                            width = 7,
                            command = lambda: removeItem.removeFromOrder(total_frame, accountID, window, newOrder_frame, d, newOrderList, discounts_label, total_label, subtotal_label, vat_label, orderArray))
    newOrderPop.place(x = 4,
                      y = 210)

    total_frame = tk.Frame(newOrder_frame,
                           highlightbackground  = "gray",
                           highlightthickness = 1,
                           height = 209,
                           width = 340)
    total_frame.place(x = 383,
                      y = 264)
    
    subtotal_label = tk.Label(total_frame,
                                text = "Subtotal: £0.00",
                                font = ('Arial', 15))
    subtotal_label.place(x = 5,
                         y = 5)
    
    vat_label = tk.Label(total_frame,
                            text = "VAT: £0.00",
                            font = ('Arial', 15))
    vat_label.place(x = 5,
                    y = 30)
    
    discounts_label = tk.Label(total_frame,
                               text = "Discounts: 0%",
                               font = ('Arial', 15))
    discounts_label.place(x = 5,
                          y = 105)
    
    total_label = tk.Label(total_frame,
                           text = "Total: £0.00",
                           font = ('Arial', 15))
    total_label.place(x = 5,
                      y = 130)
    
    addDiscounts_button = tk.Button(total_frame,
                                    text = "Add discounts",
                                    font = ('Arial', 15),
                                    width = 13,
                                    command = lambda: addDiscounts.addDiscounts(total_frame, accountID, window, newOrder_frame, newOrderList, discounts_label, total_label, subtotal_label, vat_label, orderArray))
    addDiscounts_button.place(x = 5,
                              y = 160)
    
    searchBar = tk.Entry(item_frame,
                         highlightbackground  = "gray",
                         highlightthickness = 1,
                         bg = "white",
                         width = 45)
    searchBar.place(x = 5,
                    y = 5)

    OPTIONS = ["Fish", "Sausages & Chicken", "Chips", "Extra", "Drinks"] #Category list
    variable = tk.StringVar(item_frame)
    variable.set(OPTIONS[0])
    dropdownOption = tk.OptionMenu(item_frame,
                                   variable,
                                   *OPTIONS,
                                   command = callback)
    dropdownOption.place(x = 290,
                         y = 0)
    
    callback(OPTIONS[0]) #Default drop down set to "Fish"