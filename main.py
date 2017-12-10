import pyglet
from pyglet.gl import *
from pyglet.window import mouse
from pyglet.window import key
from elements import *
from pprint import pprint
from calculator import Calculator
from wallet import Wallet
from expenses import Expenses
from coin import Coin
import sys

window = pyglet.window.Window()
batch = pyglet.graphics.Batch()
coin = Coin()

elements = []
centerLabel = []




expenses = Square(0, window.height-50, window.width//3, window.height,0,255,0)
elements.append(expenses)

percent = Square(window.width//3, window.height-50, int(window.width//1.5), window.height, 255,0,0)
elements.append(percent)

wallet = Square(int(window.width//1.5),window.height-50,window.width,window.height,0,0,255)
elements.append(wallet)



walletLabel = Label("Wallet", "Helvetica", 24, wallet.averageX, wallet.averageY, "center", "center")
elements.append(walletLabel)

expensesLabel = Label("Expenses", "Helvetica", 24, expenses.averageX, expenses.averageY, "center", "center")
elements.append(expensesLabel)

percentLabel = Label("Percent", "Helvetica", 24, percent.averageX, percent.averageY, "center", "center")
elements.append(percentLabel)

def printLabelCenter(value):
    if(len(centerLabel) > 0):
        centerLabel.pop()
    label = Label(value, "Helvetica", 36, window.width//2, window.height//2, "center", "center")
    centerLabel.append(label)



@window.event
def on_draw():
    window.clear()
    for i in elements:
        i.draw()

    for i in centerLabel:
        i.draw()


@window.event
def on_mouse_press(x,y,symbol,modifiers):
    if symbol == mouse.LEFT:
        if(wallet.within(x,y) == 1):
            value = coin.getWalletWorth('sek')
            printLabelCenter(str(value) + "sek")
            print("Wallet click")
        elif(expenses.within(x,y) == 1):
            value = coin.getExpenses()
            printLabelCenter(str(value))
            print("Expenses click")
        elif(percent.within(x,y) == 1):
            value = coin.getSumPercent()
            print(value)
            printLabelCenter(str(value))
            print("Percent click")
        else:
            print("NO")
    else:
        print(hello)

@window.event
def on_key_press(symbol,modifiers):
    if(symbol == key.Q):
        quit()
    print("yolo")

pyglet.app.run()
