import tkinter as tk
from viewOrder.processing import sortOrders

def refresh(waiting, in_progress, completed):
    
    #Refreshing all widgets in each frame
    for widget in waiting.winfo_children():
        widget.destroy()
        
    for widget in in_progress.winfo_children():
        widget.destroy()
        
    for widget in completed.winfo_children():
        widget.destroy()
        
    sortOrders.sorting(waiting, in_progress, completed)