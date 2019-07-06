#Main backend code#
from tkinter import *
import pymongo
import OrderClasses


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["MachineCompany"]
orders = mydb["Orders"]
parts = mydb["Parts"]

#Ask for user input in tkinter
master = Tk()
Label(master, text="Company Name").grid(row=0)
Label(master, text="Order Number").grid(row=1)

entryCN = Entry(master)
entryON = Entry(master)
entryCN.grid(row=0,column=1)
entryON.grid(row=1,column=1)
master.mainloop()

mydict = {"_id": 2,"Company": "Metal Industy", "Parts": 1}



print(myclient.list_database_names())
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exits.")
