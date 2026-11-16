import tkinter as tk
from viewOrder.processing import sortOrders


def viewOrder(window):
    viewOrder_frame = tk.Frame(window,
                               highlightbackground = "gray",
                               highlightthickness = 1,
                               height = 474,
                               width = 724)
    viewOrder_frame.place(x = 126,
                          y = 2)
    waiting_frame = tk.Frame(viewOrder_frame,
                             highlightbackground = "gray",
                             highlightthickness = 1,
                             height = 470,
                             width = 238)
    waiting_frame.place(x = 2,
                        y = 2)
    inProgress_frame = tk.Frame(viewOrder_frame,
                                highlightbackground = "gray",
                                highlightthickness = 1,
                                height = 470,
                                width = 238)
    inProgress_frame.place(x = 242,
                           y = 2)
    completed_frame = tk.Frame(viewOrder_frame,
                               highlightbackground = "gray",
                               highlightthickness = 1,
                               height = 470,
                               width = 238)
    completed_frame.place(x = 484,
                          y = 2) 
    
    sortOrders.sorting(waiting_frame, inProgress_frame, completed_frame)    #Passing the frames