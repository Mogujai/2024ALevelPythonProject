import sql_call as sql
import tkinter as tk
import json
from viewOrder.processing import moveUpdate

def sorting(waiting, in_progress, completed):  
    
    #Creating the labels
    waiting_label = tk.Label(waiting,
                             text = "Waiting",
                             font = ('Arial', 20))
    waiting_label.place(x = 55,
                        y = 5)
    inProgress_label = tk.Label(in_progress,
                                text = "In Progress",
                                font = ('Arial', 20))
    inProgress_label.place(x = 45,
                          y = 5)
    completed_label = tk.Label(completed,
                               text = "Completed",
                               font = ('Arial', 20))
    completed_label.place(x = 50,
                          y = 5)
      
    c = sql.sq()
    cursor = c.cursor()
    cursor.execute("""
                   SELECT orderID,menuItems,state FROM orders
                   """)
    data = cursor.fetchall()
    
    u = 50
    p = 50
    z = 50
    for i in data:
        
        #Separating items into each current state "Waiting", "In Progress", "Completed"
        orderWItems = []
        if i[-1] == "Waiting":
            Wid = i[0]
            WmenuItems = i[1]
            Witems = json.loads(WmenuItems)
            #print(Witems) TEST
            for j in Witems:
                #print(j)
                cursor.execute("""
                            SELECT name FROM itemstock WHERE ID = ?
                            """,
                            (j,))
                Witem = cursor.fetchall()[0][0] 
                #print(Witem) TEST
                orderWItems.append(Witem)
            #print(orderItems)
            string = f"Order ID: {i[0]}\n\
{orderWItems}"
                
                
            #Movement buttons
            waiting_order = tk.Label(waiting,
                                     text = string,
                                     font = ('Arial', 10),
                                     wraplength = 190)
            waiting_order.place(x = 5,
                                y = z)
            buttonR = tk.Button(waiting,
                               text = ">",
                               height = 2,
                               width = 2,
                               command = lambda Wid=Wid: moveUpdate.buttonUpdateRight(Wid, waiting, in_progress, completed))
            buttonR.place(x = 195,
                          y = z)
            z += 100
            
        orderPItems = []
        if i[-1] == "In Progress":
            Pid = i[0]
            PmenuItems = i[1]
            Pitems = json.loads(PmenuItems)
            #print(Pitems) TEST
            for j in Pitems:
                #print(j)
                cursor.execute("""
                            SELECT name FROM itemstock WHERE ID = ?
                            """,
                            (j,))
                Pitem = cursor.fetchall()[0][0] 
                #print(Pitem) TEST
                orderPItems.append(Pitem)
            #print(orderItems)
            string = f"Order ID: {i[0]}\n\
{orderPItems}"
                
            in_progress_order = tk.Label(in_progress,
                                         text = string,
                                         font = ('Arial', 10),
                                         wraplength = 150)
            in_progress_order.place(x = 45,
                                    y = p)
            
            #Movement buttons
            buttonR = tk.Button(in_progress,
                               text = ">",
                               height = 2,
                               width = 2,
                               command = lambda Pid=Pid: moveUpdate.buttonUpdateRight(Pid, waiting, in_progress, completed))
            buttonR.place(x = 195,
                          y = p)
            
            buttonL = tk.Button(in_progress,
                               text = "<",
                               height = 2,
                               width = 2,
                               command = lambda Pid=Pid: moveUpdate.buttonUpdateLeft(Pid, waiting, in_progress, completed))
            buttonL.place(x = 5,
                          y = p)
            p += 100
            
        orderCItems = []
        if i[-1] == "Completed":
            Cid = i[0]
            CmenuItems = i[1]
            Citems = json.loads(CmenuItems)
            #print(Citems) TEST
            for j in Citems:
                #print(j)
                cursor.execute("""
                            SELECT name FROM itemstock WHERE ID = ?
                            """,
                            (j,))
                Citem = cursor.fetchall()[0][0] 
                #print(Citem) TEST
                orderCItems.append(Citem)
            #print(orderItems)
            string = f"Order ID: {i[0]}\n\
{orderCItems}"
                
            completed_order = tk.Label(completed,
                                       text = string,
                                       font = ('Arial', 10),
                                       wraplength = 150)
            completed_order.place(x = 45,
                                  y = u)
            
            #Movement buttons
            buttonR = tk.Button(completed,
                               text = "✓",
                               height = 2,
                               width = 2,
                               command = lambda Cid=Cid: moveUpdate.buttonUpdateRight(Cid, waiting, in_progress, completed))
            buttonR.place(x = 195,
                          y = u)
            buttonL = tk.Button(completed,
                               text = "<",
                               height = 2,
                               width = 2,
                               command = lambda Cid=Cid: moveUpdate.buttonUpdateLeft(Cid, waiting, in_progress, completed))
            buttonL.place(x = 5,
                          y = u)
            u += 100 