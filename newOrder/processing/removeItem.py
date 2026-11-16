import tkinter as tk
import sql_call as call
from newOrder.processing import updateTotal

def removeFromOrder(total_frame, accountID, window, newOrder_frame, discount, newOrderList, discounts_label, total_label, subtotal_label, vat_label, orderArray):
    j = 0
    select = newOrderList.curselection()    #Selecting selected item inside listbox
    selectName = newOrderList.get([select]) 
    #print(selectName)
    if select:
        newOrderList.delete(select[0])  #Removing item from listbox
        c = call.sq()
        cursor = c.cursor()
        cursor.execute('''
                        SELECT id FROM itemstock WHERE name = ?
                        ''',
                        (selectName,))
        popArray = cursor.fetchone()[0] #Retrieving ID from database via name
        #print(popArray)
        
        for i in orderArray:
            #print(i)
            if i == popArray:
                orderArray.pop(j)   #Removing ID from order array
                #print(orderArray)
            j += 1    
    updateTotal.update_total(total_frame, accountID, window, newOrder_frame, discount, newOrderList, discounts_label, total_label, subtotal_label, vat_label, orderArray)