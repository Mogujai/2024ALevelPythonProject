import tkinter as tk
import sqlite3 as sql
import time
from time import sleep

def createWindow():
    window = tk.Tk()
    window.geometry("854x480")
    window.title("Kitchen Screen")

    def running():
        for widget in createWindow.winfo_children():
            widget.destroy()

        def moveOrder(col,orderID):

            with sql.connect("mF.db") as db:
                conn = db.cursor()

            conn.execute("""
                            UPDATE orders SET state = ? WHERE orderID = ?
                         """,
                         [(col),(orderID)])
            db.commit()

            running()

        

        
        


    waiting_frame = tk.Frame(window,
                             highlightbackground = "gray",
                             highlightthickness = 1,
                             height = 474,
                             width = 280)
    waiting_frame.place(x = 2,
                        y = 2)
    
    waiting_label = tk.Label(waiting_frame,
                             text = "Waiting",
                             font = ('Arial', 15))
    waiting_label.place(x = 103,
                        y = 5)

    processing_frame = tk.Frame(window,
                                highlightbackground = "gray",
                                highlightthickness = 1,
                                height = 474,
                                width = 280)
    processing_frame.place(x = 286,
                           y = 2)

    processing_label = tk.Label(processing_frame,
                                text = "Processing",
                                font = ('Arial', 15))
    processing_label.place(x = 90,
                           y = 5)

    completed_frame = tk.Frame(window,
                               highlightbackground = "gray",
                               highlightthickness = 1,
                               height = 474,
                               width = 280)
    completed_frame.place(x = 570,
                          y = 2)

    completed_label = tk.Label(completed_frame,
                               text = "Completed",
                               font = ('Arial', 15))
    completed_label.place(x = 90,
                          y = 5)

    running()
createWindow()
