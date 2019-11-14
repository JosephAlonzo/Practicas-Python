from tkinter import *
from calculadora import Operaciones

class root():
     def __init__(self):
        self.window = Tk()
        self.window.title("Calculadora - [Preview]")
        self.window.geometry("250x300")
        self.lbl = Label(self.window, text="Primer numero")
        self.lbl.grid(column=0, row=0, pady=10, padx=20)
        self.txtContent= StringVar()
        self.txt = Entry(self.window, width=20, textvariable= self.txtContent)
        self.txt.grid(column=1, row=0, pady=10)
        self.lbl2 = Label(self.window, text="Segundo numero")
        self.lbl2.grid(column=0, row=1, pady=10)
        self.txtContent2= StringVar()
        self.txt2 = Entry(self.window, width=20, textvariable= self.txtContent2)
        self.txt2.grid(column=1, row=1, pady=10)
        self.lbl3 = Label(self.window, text="Resultado")
        self.lbl3.grid(column=0, row=2, pady=10)
        self.txtContent3= StringVar()
        self.txt3 = Entry(self.window, width=20 , textvariable = self.txtContent3 )
        self.txt3.grid(column=1, row=2, pady=10)

        self.btn = Button(self.window, text="+",command= lambda: self.resolver("sumar"))
        self.btn.grid(column=0, row=3, sticky='nesw', pady=10)
        self.btn2 = Button(self.window, text="-",command= lambda: self.resolver("restar"))
        self.btn2.grid(column=1, row=3, sticky='nesw', pady=10)
        self.btn3 = Button(self.window, text="*",command= lambda: self.resolver("multiplicar"))
        self.btn3.grid(column=0, row=4, sticky='nesw', pady=10)
        self.btn4 = Button(self.window, text="/",command= lambda: self.resolver("dividir"))
        self.btn4.grid(column=1, row=4, sticky='nesw', pady=10)
        self.btn5 = Button(self.window, text="%",command= lambda: self.resolver("mod"))
        self.btn5.grid(column=0, row=5, sticky='nesw', pady=10)
        self.btn6 = Button(self.window, text="CLEAR",command= lambda: self.clear())
        self.btn6.grid(column=1, row=5, sticky='nesw', pady=10)
        self.window.mainloop()


class Calculadora(object):
    
    def __init__(self):
            root.__init__(self)

    def resolver(self,Operacion):
        num1 = int(self.txtContent.get())
        num2 = int(self.txtContent2.get())
        obj = Operaciones(num1, num2)
        if Operacion == "sumar":
            self.txtContent3.set(str(obj.sumar()) ) 
        elif Operacion == "restar":
            self.txtContent3.set(str(obj.restar()) )
        elif Operacion == "multiplicar":
            self.txtContent3.set( str(obj.multiplicar()) )
        elif Operacion == "dividir":
            self.txtContent3.set(str(obj.dividir()) )
        elif Operacion == "mod":
            self.txtContent3.set(str(obj.mod()) )

    def clear(self):
        self.txtContent.set("")
        self.txtContent2.set("")
        self.txtContent3.set("")

obj = Calculadora()