#!/usr/bin/python3
from pprint import pprint
from calculator import Calculator
from wallet import Wallet
from expenses import Expenses
import sys

wallet = Wallet()
expenses = Expenses()
class Coin():
    def __init__(self):
        self.wallet = Wallet()
        self.expenses = Expenses()
        pass

    def getWalletWorth(self,currency):
        self.worth = self.wallet.calculateWorth(currency)
        return self.worth

    def getSumPercent(self):
        sumExpenses = expenses.calculateExpenses()
        sumWallet = wallet.calculateWorth("sek")
        final = sumWallet / sumExpenses
        final = final - 1
        final = final * 100
        final = int(final)
        return(str(final) + "%")

    def getSum(self,currency):
        sumExpenses = expenses.calculateExpenses()
        calculator = Calculator()
        expensesCurrency = expenses.currency
        currencyChanger = calculator.currency(expensesCurrency.upper())
        rates = calculator.currency(expensesCurrency)
        sumWallet = wallet.calculateWorth('usd')
        sumExpenses = sumExpenses / currencyChanger
        result = sumWallet - sumExpenses
        changer = calculator.currency(currency.upper())
        if(changer == 0):
            changer = 1
        result = changer * result
        return((str(("%.2f" % (result))) + currency))

    def getExpenses(self):
        sumExpenses = expenses.calculateExpenses()
        currency = expenses.currency
        return(("%.2f" % sumExpenses) + currency)





if(len(sys.argv) > 1):

    if(sys.argv[1] == "sum"):
        sumExpenses = expenses.calculateExpenses()
        if(len(sys.argv) > 2):
            if(sys.argv[2] == "percent"):
                sumWallet = wallet.calculateWorth("sek")
                final = sumWallet / sumExpenses
                final = final - 1
                final = final * 100
                final = int(final)
                print(str(final) + "%")
            else:
                calculator = Calculator()
                expensesCurrency = expenses.currency
                currencyChanger = calculator.currency(expensesCurrency.upper())
                rates = calculator.currency(expensesCurrency)
                sumWallet = wallet.calculateWorth('usd')
                sumExpenses = sumExpenses / currencyChanger
                result = sumWallet - sumExpenses
                changer = calculator.currency(sys.argv[2].upper())
                if(changer == 0):
                    changer = 1
                result = changer * result
                print(str(("%.2f" % (result))) + sys.argv[2])
        else:
            print("The sum command requires one additional argument")
    

    if(sys.argv[1] == "expenses"):
        if(len(sys.argv) > 2):
            if(sys.argv[2] == "e"):
                expenses.editExpenses()
            elif(sys.argv[2] == "add" and len(sys.argv) > 3):
                expenses.add(sys.argv[3])
            elif(sys.argv[2] == "remove" and len(sys.argv) > 3):
                expenses.remove(sys.argv[3])
        else:
            sumExpenses = expenses.calculateExpenses()
            currency = expenses.currency
            print(("%.2f" % sumExpenses) + currency)



    if(sys.argv[1] == "wallet"):
        if(len(sys.argv) > 2):
            if(sys.argv[2] == "e"):
                wallet.editWallet()
            elif(sys.argv[2] == "list"):
                if(len(sys.argv) > 3):
                    if(sys.argv[3] == "distribution" or sys.argv[3] == "dist" or sys.argv[3] == "percent" ):
                        wallet.distribution()
                    elif(sys.argv[3] == "value"):
                        if(len(sys.argv) > 4):
                            wallet.distributionAndWorth(sys.argv[4])
                        else:
                            print("Need currency argument")
                else: 
                    wallet.listWallet()
            elif(sys.argv[2] == "add"):
                if(len(sys.argv) > 4):
                    wallet.add(sys.argv[3], sys.argv[4])
                else:
                    print("Need more arguments")
            elif(sys.argv[2] == "remove"):
                if(len(sys.argv) > 4):
                    wallet.add("-" + sys.argv[3], sys.argv[4])
                else:
                    print("Need more arguments")
            else:
                sumWallet = wallet.calculateWorth(sys.argv[2])
                if(sumWallet == 0):
                    print("Unkown currency or empty wallet")
                print(str(sumWallet) + sys.argv[2].upper())
        else:
            print("Wallet command requires additional arguments")
            
    if(sys.argv[1] == "value"):
        if(len(sys.argv) > 3):
            calculator = Calculator()
            print(str(calculator.priceOfCoin(sys.argv[2], sys.argv[3])) + sys.argv[3])
        else:
            print("Value needs cryptoname and currency as argument")

    if(sys.argv[1] == "diversify"):
        if(len(sys.argv) > 4):
            calculator = Calculator()
            args = sys.argv
            value = args[2]
            currency = args[3]
            args.pop(0);args.pop(0);args.pop(0);args.pop(0)
            coins = args
            calculator.diversify(value, currency, coins)
        else:
            print("Need more arguments(at least 3). Ex. Value Currency Coin Coin ...")

else:
    print("Give the program more arguments")

