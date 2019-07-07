#Classes for ordering and parts in order to make it easy to display in GUI
import datetime
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
    def get_dict(self):
        date = datetime.datetime.today()
        return {"Order Number" : self.orderNum, 
                "Cost" : self.cost, "Company" : self.company, 
                "Number of Parts" : self.numParts,
                "Date" : date.strftime('%d-%m-%Y')}

class Part(object):
    def __init__(self, orderNum, partNum, quote, notes):
        self.orderNum = orderNum
        self.partNum = partNum
        self.quote = quote
        self.notes = notes
    def get_orderNum(self):
        return self.orderNum
    def get_partNum(self):
        return self.partNum
    def get_quote(self):
        return self.quote
    def get_notes(self):
        return self.notes
    def get_dict(self):
        return {"Order Number" : self.orderNum, 
                "Part Number" : self.partNum, 
                "Quote" : self.quote, "Notes" : self.notes}