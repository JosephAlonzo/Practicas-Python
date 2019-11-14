from tkinter import *

class root():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("350x100")
        self.window.title(" Factorial - [Preview] ")
        self.lbl = Label(self.window, text="n")
        self.lbl.grid(column=1, row=1, padx=30, pady=35)
        self.txtContent = StringVar()
        self.txtContent.set("1")
        self.txt = Entry(self.window, width=10, textvariable=self.txtContent)
        self.txt.grid(column=2, row=1)
        self.lbl2 = Label(self.window, text="Factoral (n)")
        self.lbl2.grid(column=3, row=1)
        self.txtContent2 = StringVar()
        self.txtContent2.set("1")
        self.txt2 = Entry(self.window, width=10, textvariable=self.txtContent2)
        self.txt2.grid(column=4, row=1)
        self.btn = Button(self.window, text="siguiente", command= lambda: self.click())
        self.btn.grid(column=5, row=1)
        self.result= 0
        self.window.mainloop()

class Factorial(root):
    def __init__(self):
            root.__init__(self)

    def click(self):
        n =  int(self.txtContent.get()) + 1
        self.txtContent.set(n)

        if n == 1 or n == 0:
            self.txtContent.set( str( n + 1) )
            self.txtContent2.set(str(n))
        else:
            result = 0
            self.txtContent2.set(self.calcularFactorial(result))
    
    def calcularFactorial(self, result, n = False):
        if n == False:
            n =  int(self.txtContent.get()) 
            
        if n > 1:
                result += n * self.calcularFactorial( result, n-1 )  
                return result
        else:
            return n              
obj = Factorial()