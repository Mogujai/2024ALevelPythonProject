import tkinter as tk
import sql_call as sql
import mainWindow
import time
from time import sleep

def buttonClicked(root, usernameBox, passwordBox, labelSuccess):
    c = sql.sq()
    cursor = c.cursor()
    cursor.execute('''
              SELECT * FROM accounts
              ''')
    results = cursor.fetchall()
    
    
    for result in results:
        #print(result)  #TEST
        
        if usernameBox.get("1.0","end-1c") == result[1] and passwordBox.get("1.0","end-1c") == result[2]:
            labelSuccess.config(text = "Success!")
            accountID = result[0]
            accessLevel = result[3]
            sleep(1)
            cursor.close()
            root.destroy()
            mainWindow.createWindow(accountID, accessLevel)     #main program
        else:
            break
    
    labelSuccess.config(text = "Fail, please try again")
    
def login():
    root = tk.Tk()                             #login window generation
    root.geometry("854x480")
    root.title("Dave's Fish n Chips Shop")

    labelTitle = tk.Label(root, 
                    text = "Dave's Fish n Chips Shop", 
                    font = ('Arial', 30))
    labelTitle.grid(row = 0,
                    column = 0,
                    padx = 0,
                    pady = 50)

    labelUsername = tk.Label(root,
                            text="Username",
                            font=('Arial', 20))
    labelUsername.grid(row = 1,
                    column = 0,
                    padx = 0,
                    pady = 0)

    usernameBox = tk.Text(root,
                        width = 20,
                        height = 1,
                        font = ('Arial', 20))
    usernameBox.grid(row = 2,
                    column = 0,
                    padx = 280,
                    pady = 0)

    labelPassword = tk.Label(root,
                            text = "Password",
                            font = ('Arial', 20))
    labelPassword.grid(row = 3,
                    column = 0,
                    padx = 0,
                    pady = 0)

    passwordBox = tk.Text(root,
                        width = 20,
                        height = 1,
                        font = ("Arial", 20))
    passwordBox.grid(row = 4,
                    column = 0,
                    padx = 280,
                    pady = 0)

    acceptInput = tk.Button(root,
                            text = "Login",
                            command = lambda: buttonClicked(root, usernameBox, passwordBox, labelSuccess),
                            activebackground = "gray",
                            activeforeground = "white",
                            cursor = "hand2",
                            height = 1,
                            width = 7,
                            font = ('Arial', 20))
    acceptInput.grid(row = 5,
                    column = 0,
                    padx = 0,
                    pady = 20)

    labelSuccess = tk.Label(root,
                            text = "",
                            activeforeground = "white",
                            font = ('Arial', 20))
    labelSuccess.grid(row = 6,
                    column = 0,
                    padx = 0,
                    pady = 10)

    root.mainloop()
