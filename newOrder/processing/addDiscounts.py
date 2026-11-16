import tkinter as tk
from newOrder.processing import updateTotal
from newOrder.processing import back as bBack

def addDiscounts(total_frame, accountID, window, newOrder_frame, newOrderList, discounts_label, total_label, subtotal_label, vat_label, orderArray):
                 
    def returnNumber(j):
        discountFrame.place_forget()    #Removes the frame from the window
        updateTotal.update_total(total_frame, accountID, window, newOrder_frame, j, newOrderList, discounts_label, total_label, subtotal_label, vat_label, orderArray)

    
    discountFrame = tk.Frame(total_frame,
                             highlightbackground = "gray",
                             highlightthickness = "1",
                             height = 200,
                             width = 330)
    discountFrame.place(x = 4,
                        y = 4)
    
    j = 0
    xpos = 5
    ypos = 5
    
    #Generate buttons for adding discounts
    for i in range(6):
        j += 5
        percent = tk.Button(discountFrame,
                            text = f"{j}%",
                            font = ('Arial', 15),
                            width = 5,
                            command = lambda j = j: returnNumber(j))
        percent.place(x = xpos,
                      y = ypos)
        xpos += 70
        if xpos > 216:
            ypos += 45
            xpos = 5
            
    backB = tk.Button(discountFrame,
                        text = "back",
                        font = ('Arial', 15),
                        width = 5,
                        command = lambda: bBack.back(discountFrame))
    backB.place(x = 5,
                y = 160)