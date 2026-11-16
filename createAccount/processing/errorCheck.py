import tkinter as tk
import re
from createAccount.processing import creation

def check(confirm, window, createAcc_frame, accessLevel, uBox, uCheck, pwBox, pwCheck, pwRBox, fnBox, fnCheck, snBox, snCheck, emBox, emCheck, pnBox, pnCheck, addBox, addCheck):
    nameRule = "[A-Z,a-z,0-9]"
    special = "[,]"
    emailRule = re.compile("([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")   
    pnumRule = "^(07[\d]{8,12})$"
    
    #Retrieve data from boxes where data is not null
    username = uBox.get("1.0","end-1c")
    password = pwBox.get("1.0","end-1c")
    password_reentry = pwRBox.get("1.0","end-1c")
    firstname = fnBox.get("1.0","end-1c")
    surname = snBox.get("1.0","end-1c")
    email = emBox.get("1.0","end-1c")
    pnum = pnBox.get("1.0","end-1c")
    address = addBox.get("1.0","end-1c")
    
    #Setting access levels
    if accessLevel == "Admin":
        accessLevel = 1
    elif accessLevel == "Staff":
        accessLevel = 2
    
    checks = 0
    while True:
        if len(username) > 2 and len(username) < 17:
            if re.search(nameRule, username):
                checks += 1
                uCheck.config(text = " ")
            else:
                uCheck.config(text = "Username cannot contain special characters")
        else:
            uCheck.config(text = "Username has to be 3-16 characters")
            
        if len(password) > 7:
            if password == password_reentry:
                checks += 1
                pwCheck.config(text = " ")
            else:
                pwCheck.config(text = "Passwords must match")
        else:
            pwCheck.config(text = "Password must be 8 or more characters")
            
        if len(firstname) > 2 and len(firstname) < 20:
            if re.search(nameRule, firstname):
                checks += 1
                fnCheck.config(text = " ")
            else:
                fnCheck.config(text = "Name cannot contain special characters")
        else:
            fnCheck.config(text = "Name must be 3-20 characters")
            
        if len(surname) > 2 and len(surname) < 20:
            if re.search(nameRule, surname):
                checks += 1
                snCheck.config(text = " ")
            else:
                snCheck.config(text = "Name cannot contain special characters")
        else:
            snCheck.config(text = "Name must be 3-20 characters")
            
        if len(email) > 5 and len(email) < 40:
            if re.fullmatch(emailRule, email):
                checks += 1
                emCheck.config(text = " ")
            else:
                emCheck.config(text = "Email is invalid")
        else:
            emCheck.config(text = "Email is invalid")    
            
        if len(pnum) == 11:
            if re.match(pnumRule, pnum):
                checks += 1
                pnCheck.config(text = " ")
            else:
                pnCheck.config(text = "Phone number is invalid")
        else:
            pnCheck.config(text = "Phone number is invalid")
            
        if len(address) > 4:
            if re.search(nameRule,address):
                checks += 1
                addCheck.config(text = " ")
            else:
                addCheck.config(text = "Address cannot contain special characters")
        else:
            addCheck.config(text = "Address has to be longer than 4 characters")
            
        break
    
    if checks == 7: #If all checks completed it will finish the account creation process
        creation.finishAccountProcess(confirm, window, createAcc_frame, accessLevel, username, password, firstname, surname, email, pnum, address)
        
            
        
                
                
    
    
        
            