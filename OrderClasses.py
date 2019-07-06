#Classes for ordering and parts in order to make it easy to display in GUI
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
    