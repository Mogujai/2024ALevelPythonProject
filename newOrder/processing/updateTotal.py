import sql_call as call
from newOrder.processing import pOrderButton

def update_total(total_frame, accountID, window, newOrder_frame, discount, newOrderList, discounts_label, total_label, subtotal_label, vat_label, orderArray):
    subtotal = 0
    vat = 0
    total = 0
    
    #print(orderArray)

    c = call.sq()
    cursor = c.cursor()
    for i in range(newOrderList.size()):    #Fetching price via name 
        item = newOrderList.get(i)
        cursor.execute('''
                        SELECT id,price FROM itemstock WHERE name = ?
                        ''',
                        (item,))
        data = cursor.fetchall()
        subtotal += float(data[0][1])
    
    minusPrice = round((subtotal * (discount/100)), 2)  #Subtraction price from discount
    vat = subtotal * 0.2
    total = subtotal - minusPrice

    discounts_label.config(text = f"Discounts: {discount}%")    #Set labels to current values
    subtotal_label.config(text = f"Subtotal: £{subtotal:.2f}")
    vat_label.config(text = f"VAT: £{vat:.2f}")                      
    total_label.config(text = f"Total: £{total:.2f}")
    
    pOrderButton.plorder(total_frame, accountID, window, total, vat, subtotal, newOrder_frame, orderArray)
    
    