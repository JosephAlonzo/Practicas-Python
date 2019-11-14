from tkinter import *
import random

class root():
    def __init__(self):
        self.root = Tk()
        self.root.title("Generador de numeros - [Preview]")

        self.lbl= Label(self.root, text="Número 1")
        self.lbl.grid(column=0, row=0, pady=(20,3), padx=10,sticky="W")
        self.spin = Spinbox(self.root, from_=0, to=100, width=10)
        self.spin.grid(column=1, row=0, pady=(20,3), sticky='nesw')
        self.lbl2= Label(self.root, text="Número 2")
        self.lbl2.grid(column=0, row=1,sticky="W")
        self.spin2 = Spinbox(self.root, from_=0, to=100, width=10)
        self.spin2.grid(column=1, row=1, sticky='nesw', pady=(0,3))
        self.lbl3= Label(self.root, text="Número generado")
        self.lbl3.grid(column=0, row=2, pady=3)
        self.txtContent = StringVar()
        self.txt = Entry(self.root, width=10, textvariable= self.txtContent)
        self.txt.grid(column=1, row=2, sticky='nesw', pady=(0,3))

        self.btn = Button(self.root, text="Generar", command= lambda: self.generar())
        self.btn.grid(column=1, row=3, sticky='nesw')

        self.root.mainloop()

class Main(root):
    def __init__(self):
        root.__init__(self)  

    def generar(self):
        minVal = int( self.spin.get())
        maxVal = int( self.spin2.get())
        if minVal > maxVal:
            maxVal = int( self.spin.get())
            minVal = int( self.spin2.get())

        self.txtContent.set( random.randint(minVal, maxVal) )

obj = Main()