import sql_call as sql
import tkinter as tk
from createAccount import createAccount
from time import sleep

def finishAccountProcess(confirm, window, createAcc_frame, accessLevel, username, password, firstname, surname, email, pnum, address):
    saved = tk.Label(createAcc_frame,
                     text = "Saved!",
                     font = ('Arial', 20))
    saved.place(x = 340,
                y = 390)
    
    #Writing to database
    c = sql.sq()
    cursor = c.cursor()
    cursor.execute("""
                   INSERT INTO accounts(username,password,accessLevel) VALUES(?,?,?)
                   """,
                   (username,password,accessLevel,))
    c.commit()
    cursor.execute("""
                   SELECT accountID FROM accounts WHERE username = ?
                   """,
                   (username,))
    aID = cursor.fetchall()[0][0] #Selecting accountID to link to personal details as foreign key
    
    cursor.execute("""
                   INSERT INTO accountsDetails(accountID,firstName,surName,email,phoneNumber,address) VALUES(?,?,?,?,?,?)
                   """,
                   (aID,firstname,surname,email,pnum,address))
    c.commit()
    cursor.close()
    
    sleep(1)
    createAcc_frame.place_forget()
    saved.place_forget()
    createAccount.createAcc(window)
    
    
    
    
    