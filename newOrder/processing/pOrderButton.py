import tkinter as tk
from newOrder.processing import placeOrder as pOrder

def plorder(total_frame, accountID, window, total, vat, subtotal, newOrder_frame, orderArray):  #Workaround button for placing order
    placeorder_button = tk.Button(total_frame,
                                  text = "Place order",
                                  font = ('Arial', 15),
                                  width = 13,
                                  command = lambda: pOrder.placeOrder(accountID, window, total, vat, subtotal, newOrder_frame, orderArray))
    placeorder_button.place(x = 165,
                            y = 160)