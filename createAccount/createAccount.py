import tkinter as tk
from tkinter import ttk
from createAccount.processing import errorCheck

def createAcc(window):
    createAcc_frame = tk.Frame(window,
                               highlightbackground = "gray",
                               highlightthickness = 1,
                               height = 474,
                               width = 724)
    createAcc_frame.place(x = 126,
                          y = 2)
    
    username_Label = tk.Label(createAcc_frame,
                              text = "Username",
                              font = ('Arial',12))
    username_Label.place(x = 30,
                         y = 20)
    username_box = tk.Text(createAcc_frame,
                           width = 16,
                           height = 1,
                           font = ('Arial',12))
    username_box.place(x = 30,
                       y = 40)
    username_error = tk.Label(createAcc_frame,
                              text = " ",
                              font = ('Arial',12))
    username_error.place(x = 260,
                         y = 40)
    
    password_Label = tk.Label(createAcc_frame,
                              text = "Password",
                              font = ('Arial',12))
    password_Label.place(x = 30,
                         y = 65)
    password_box = tk.Text(createAcc_frame,
                           width = 16,
                           height = 1,
                           font = ('Arial',12))
    password_box.place(x = 30,
                       y = 85)
    
    passwordReentry_Label = tk.Label(createAcc_frame,
                              text = "Password (Re-enter)",
                              font = ('Arial',12))
    passwordReentry_Label.place(x = 30,
                                y = 110)
    passwordReentry_box = tk.Text(createAcc_frame,
                                  width = 16,
                                  height = 1,
                                  font = ('Arial',12))
    passwordReentry_box.place(x = 30,
                              y = 130)
    password_error = tk.Label(createAcc_frame,
                              text = " ",
                              font = ('Arial',12))
    password_error.place(x = 260,
                         y = 130)
    
    firstname_label = tk.Label(createAcc_frame,
                               text = "First Name",
                               font = ('Arial',12))
    firstname_label.place(x = 30,
                          y = 155)
    firstname_box = tk.Text(createAcc_frame,
                            width = 16,
                            height = 1,
                            font = ('Arial',12))
    firstname_box.place(x = 30,
                        y = 175)
    firstname_error = tk.Label(createAcc_frame,
                               text = " ",
                               font = ('Arial',12))
    firstname_error.place(x = 260,
                          y = 175)
    
    surname_label = tk.Label(createAcc_frame,
                             text = "Surname",
                             font = ('Arial',12))
    surname_label.place(x = 30,
                        y = 200)
    surname_box = tk.Text(createAcc_frame,
                          width = 16,
                          height = 1,
                          font = ('Arial',12))
    surname_box.place(x = 30,
                      y = 220)
    surname_error = tk.Label(createAcc_frame,
                             text = " ",
                             font = ('Arial',12))
    surname_error.place(x = 260,
                        y = 220)
    
    email_label = tk.Label(createAcc_frame,
                           text = "Email",
                           font = ('Arial',12))
    email_label.place(x = 30,
                      y = 245)
    email_box = tk.Text(createAcc_frame,
                        width = 16,
                        height = 1,
                        font = ('Arial',12))
    email_box.place(x = 30,
                    y = 265)
    email_error = tk.Label(createAcc_frame,
                           text = " ",
                           font = ('Arial',12))
    email_error.place(x = 260,
                      y = 265)
    
    pnumber_label = tk.Label(createAcc_frame,
                             text = "Phone Number",
                             font = ('Arial',12))
    pnumber_label.place(x = 30,
                        y = 290)
    pnumber_box = tk.Text(createAcc_frame,
                          width = 16,
                          height = 1,
                          font = ('Arial',12))
    pnumber_box.place(x = 30,
                      y = 310)
    pnumber_error = tk.Label(createAcc_frame,
                             text = " ",
                             font = ('Arial',12))
    pnumber_error.place(x = 260,
                        y = 310)
    
    address_label = tk.Label(createAcc_frame,
                             text = "Address",
                             font = ('Arial',12))
    address_label.place(x = 30,
                        y = 335)
    address_box = tk.Text(createAcc_frame,
                          width = 16,
                          height = 1,
                          font = ('Arial',12))
    address_box.place(x = 30,
                      y = 355)
    address_error = tk.Label(createAcc_frame,
                             text = " ",
                             font = ('Arial',12))
    address_error.place(x = 260,
                        y = 355)

    accessLevelCombobox = ttk.Combobox(createAcc_frame,
                                       font = ('Arial',12),
                                       values = ["Admin", "Staff"])
    accessLevelCombobox.place(x = 30,
                              y = 395)
    accessLevelCombobox.set("Staff")
    accessLevel = accessLevelCombobox.get()
    
    confirm = tk.Button(createAcc_frame,
                        text = "Confirm",
                        activebackground = "gray",
                        activeforeground = "white",
                        cursor = "hand2",
                        height = 1,
                        width = 7,
                        font = ('Arial', 20),
                        command = lambda: errorCheck.check(confirm, window, createAcc_frame, accessLevel,  #Passing all parameters needed for account creation
                                                           username_box, username_error,
                                                           password_box, password_error,
                                                           passwordReentry_box,
                                                           firstname_box, firstname_error,
                                                           surname_box, surname_error,
                                                           email_box, email_error,
                                                           pnumber_box, pnumber_error,
                                                           address_box, address_error))
    confirm.place(x = 270,
                  y = 390)


    