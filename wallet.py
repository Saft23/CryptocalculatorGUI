from calculator import Calculator
import os
class Wallet(object):
    wallet = None
    def __init__(self):
        relativePath = os.path.dirname(__file__)
        self.path = os.path.join(relativePath,'.wallet')
        if not(os.path.isfile(self.path)):
            self.wallet=open(self.path, 'w+')
            self.wallet.close()

    def getWalletArray(self, currency, coinOrValue):
        self.calculator = Calculator()
        self.wallet=open(self.path)
        walletlist = self.wallet.read().split('\n')
        self.wallet.close()
        walletlist.pop()
        returnValue = []
        returnCoin = []
        returnCount = []
        for item in walletlist:
            if(item == ""):
                item = "bitcoin: 0"
            fin = item.find(':')
            beg = 0
            coin = ""
            numCoin = ""
            while(beg < fin):
                coin = coin + item[beg]
                beg = beg +1
            while(fin+2 < len(item)):
                numCoin = numCoin + item[fin+2]
                fin = fin +1
            coinWorth = float(self.calculator.priceOfCoin(coin,currency.upper()))
            numCoin = float(numCoin)
            returnValue.append(coinWorth * numCoin)
            returnCoin.append(coin)
            returnCount.append(numCoin)
        if(coinOrValue == 'coin'):
            return returnCoin
        elif(coinOrValue == 'value'):
            return returnValue
        elif(coinOrValue == 'count'):
            return returnCount

    def distribution(self):
        coinArray = self.getWalletArray('usd', 'coin')
        valueArray = self.getWalletArray('usd', 'value') 
        total = self.calculateWorth('usd') 
        i = 0
        for coin in coinArray:
            print(coin + ": " + ("%.2f" % ((valueArray[i] / total)*100)) + "%")
            i = i +1

    def add(self, value, coin):
        self.calculator = Calculator()
        if(self.calculator.priceOfCoin(coin, "USD") == -1):
            print("Coin doesnt exist")
            return

        dataArray = []
        coinExist = False
        coinCount = self.getWalletArray('usd', 'count')
        coins = self.getWalletArray('usd', 'coin')
        try:
            coinIndex = coins.index(coin)
            coinExist = True
        except Exception:
            coinExist = False
        if(coinExist):
            coinCount[coinIndex] = coinCount[coinIndex] + float(value)
            for index, coin in enumerate(coins):
                dataArray.append( coin + ": " + str(coinCount[index]))

            self.wallet = open(self.path, 'w')
            self.wallet.write('\n'.join(map(str, dataArray)) + '\n')
            self.wallet.close()
            
        else:
            self.wallet = open(self.path, "a")
            self.wallet.write(coin + ": " + value + "\n")
            self.wallet.close()


    def listWallet(self):
        coinArray = self.getWalletArray('usd','coin')
        countArray = self.getWalletArray('usd','count')
        i = 0
        for count in countArray:
            print(coinArray[i] + ": " + "%.8f" % count)
            i = i +1



    def distributionAndWorth(self, currency):
        self.calculator = Calculator()
        currencyVal = self.calculator.currency(currency.upper())
        coinArray = self.getWalletArray('usd','coin')
        valueArray = self.getWalletArray('usd','value')
        i = 0
        for value in valueArray:
            print(coinArray[i] + ": " + "%.1f" % (value * currencyVal) + " " + currency)
            i = i +1


    def calculateWorth(self, currency):
        return sum(self.getWalletArray(currency, 'value'))

    def editWallet(self):
        os.system("vim " + self.path)



