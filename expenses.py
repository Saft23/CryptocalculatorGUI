import os

class Expenses(object):
    def __init__(self):
        self.currency = ""
        relativePath = os.path.dirname(__file__)
        self.path = os.path.join(relativePath,'.expenses')
        if not(os.path.isfile(self.path)):
            self.expenses=open(self.path,'w+')
            self.expenses.close()

    def calculateExpenses(self):
        self.expenses=open(self.path)
        final = 0.0
        self.currency = self.expenses.readline()
        self.currency = self.currency.splitlines()
        self.currency = self.currency[0]
        for item in self.expenses:
            final = final + float(item)

        return final

    def editExpenses(self):
        os.system("vim " + self.path)

    def add(self, value):
        self.expenses = open(self.path, "a")
        self.expenses.write(value + "\n")
        self.expenses.close()

    def remove(self, value):
        self.add("-" + value)
        

    def currency(self):
        if(self.expenses == ""):
            self.expenses=open(self.path)
            self.currency = self.expenses.readline()
            self.currency = self.currency.splitlines()
            self.currency = self.currency[0]
        return self.currency
