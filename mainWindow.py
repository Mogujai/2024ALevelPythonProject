import tkinter as tk
from newOrder import orderScreen
from viewOrder import viewOrder
from createAccount import createAccount
from viewLog import viewLog
from logout import logout
from stock import viewStock

def createWindow(accountID, accessLevel):
    
    #New global window that will be used
    window = tk.Tk()   
    window.geometry("854x480")
    window.title("Dave's Fish n Chips Shop")

    #Button to create new order
    newOrderButton = tk.Button(window,
                               text = "New Order",
                               command = lambda: orderScreen.newOrder(accountID,window), 
                               height = 2,
                               width = 10,
                               activebackground = "gray",
                               activeforeground = "white",
                               cursor = "hand2",
                               font = ('Arial', 15))
    newOrderButton.grid(row = 0,
                        column = 0,
                        padx = 2,
                        pady = 2)
   
    #Button to view current incompleted orders
    viewOrdersButton = tk.Button(window,
                                 text = "View Orders",
                                 command = lambda: viewOrder.viewOrder(window),
                                 height = 2,
                                 width = 10,
                                 activebackground = "gray",
                                 activeforeground = "white",
                                 cursor = "hand2",
                                 font = ('Arial', 15))
    viewOrdersButton.grid(row = 1,
                        column = 0,
                        padx = 2,
                        pady = 2)
   
    #Button to view all previous orders and their state
    viewLogButton = tk.Button(window,
                              text = "View Log",
                              height = 2,
                              width = 10,
                              activebackground = "gray",
                              activeforeground = "white",
                              cursor = "hand2",
                              font = ('Arial', 15),
                              command = lambda: viewLog.viewLog(window))
    viewLogButton.grid(row = 2,
                       column = 0,
                       padx = 2,
                       pady = 2)
   
    #Button to logout and return login screen
    logoutButton = tk.Button(window,
                             text = "Log Out",
                             height = 2,
                             width = 10,
                             activebackground = "gray",
                             activeforeground = "white",
                             cursor = "hand2",
                             font = ('Arial', 15),
                             command = lambda: logout.logout(window))
    logoutButton.grid(row = 3,
                      column = 0,
                      padx = 2,
                      pady = 2)
   
    if accessLevel == 1:    #Admin level permission
        
        #Button to create a new account for the system
        createAccountButton = tk.Button(window,
                                        text = "Create Account",
                                        wraplength = 120,
                                        height = 2,
                                        width = 10,
                                        activebackground = "gray",
                                        activeforeground = "white",
                                        cursor = "hand2",
                                        font = ('Arial', 15),
                                        command = lambda: createAccount.createAcc(window))
        createAccountButton.grid(row = 4,
                                 column = 0,
                                 padx = 2,
                                 pady = 2)
        
        #Button to view and add new stock or increase stock
        viewStockButton = tk.Button(window,
                                    text = "View Stock",
                                    wraplength = 120,
                                    height = 2,
                                    width = 10,
                                    activebackground = "gray",
                                    activeforeground = "white",
                                    cursor = "hand2",
                                    font = ('Arial', 15),
                                    command = lambda: viewStock.viewStock(window))
        viewStockButton.grid(row = 5,
                             column = 0,
                             padx = 2,
                             pady = 2)
        
    orderScreen.newOrder(accountID, window)    #Order Screen is set to default
    window.mainloop()

#a = 1
#b = 1
#createWindow(a,b)
