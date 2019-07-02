#Main backend code#
from tkinter import *
import pymongo

class Order(object):
    def __init__(self, orderNum, company, cost, numParts, date):
        self.orderNum = orderNum
        self.company = company
        self.cost = cost
        self.numParts = numParts
        self.date = date
    def get_orderNum(self):
        return self.orderNum
    def get_cost(self):
        return self.cost
    def get_company(self):
        return self.company
    def get_numParts(self):
        return self.numParts
    def get_date(self):
        return self.date
    
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = {"_id": 8,"name": "John", "address":"Highway 37"}

x = mycol.insert_one(mydict)

for x in mycol.find({}, {"_id":0, "name": 1}):
    print(x, type(x))
    print(x['name'])


print(myclient.list_database_names())
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exits.")
