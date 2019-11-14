from tkinter import *
import random

class root(object):
    def __init__(self):
        self.window = Tk()
        self.window.geometry("600x300")
        self.window.title(" Ejercicio 1 –GUI ")
        self.window.configure(background='#F5F5DC')
        self.lbl = Label(self.window, text="0", )
        self.lbl.grid(column=0, row=0,  pady=10, padx=150)
        self.lbl2 = Label(self.window, text="0", padx=10)
        self.lbl2.grid(column=0, row=1)
        self.btn = Button(self.window, text="Plusar", command= lambda: self.makeRandomNumber(self.lbl, 1, 10))
        self.btn.grid(column=1, row=0)
        self.btn2 = Button(self.window, text="Plusar", command= lambda: self.makeRandomNumber(self.lbl2, 1000, 2000))
        self.btn2.grid(column=1, row=1)
        self.result= 0
        self.window.mainloop()

class Main(root):
    def __init__(self):
        root.__init__(self)

    def makeRandomNumber(self, lbl, minVal, maxVal):
        lbl['text'] = random.randint(minVal, maxVal)

obj = Main()