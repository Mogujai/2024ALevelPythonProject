import tkinter as tk
from newOrder.processing import updateTotal

def iAdd(total_frame, accountID, window, newOrder_frame, itemid, itemname, orderArray, newOrderList, d, discounts_label, total_label, subtotal_label, vat_label):
            newOrderList.insert(tk.END, itemname)   #Adds to the listbox
            orderArray.append(itemid)   #Adds to the array for writing to database
            updateTotal.update_total(total_frame, accountID, window, newOrder_frame, d, newOrderList, discounts_label, total_label, subtotal_label, vat_label, orderArray)