#Main backend code#
import tkinter as tk
import pymongo
import OrderClasses

#Function to make a new part and store in database
def newPart():
    partGui = tk.Tk()
    tk.Label(partGui, text="Order Number").grid(row=0)
    tk.Label(partGui, text="Part Number").grid(row=1)
    tk.Label(partGui, text="Quote").grid(row=2)
    tk.Label(partGui, text="Notes").grid(row=3)
    
    eON = tk.Entry(partGui).grid(row=0, column=1)
    ePN = tk.Entry(partGui).grid(row=1, column=1)
    eQ = tk.Entry(partGui).grid(row=2, column=1)
    eN = tk.Entry(partGui).grid(row=3, column=1)
    
    tk.Button(partGui, text='Quit', command=partGui.quit).grid(row=4,column=0, sticky=tk.W, pady=4)
    
    partGui.mainloop()
        
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["MachineCompany"]
orders = mydb["Orders"]
parts = mydb["Parts"]

#Ask for user input in tkinter
master = tk.Tk()
tk.Label(master, text="Company Name").grid(row=0)
tk.Label(master, text="Order Number").grid(row=1)

entryCN = tk.Entry(master)
entryON = tk.Entry(master)
entryCN.grid(row=0,column=1)
entryON.grid(row=1,column=1)

tk.Button(master, text='Quit', command=master.quit).grid(row=4,column=0, sticky=tk.W, pady=4)
tk.Button(master, text='New Part', command=newPart).grid(row=4,column=1, sticky=tk.W, pady=4)

master.mainloop()

print(myclient.list_database_names())
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exits.")
