import addData

print("Choose data entry")
entry = int(input("1. User and Password\n\
2. Stock Items\n\
3. something else idk\n\
4. quit\n\
:"))

if entry == 1:
    addData.addUserPass()
    
elif entry == 2:
    addData.addStock()