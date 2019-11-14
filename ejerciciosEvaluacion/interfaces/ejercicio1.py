from tkinter import *

class root():
    def __init__(self ):
        self.window = Tk()
        self.window.geometry("600x200")
        self.lbl = Label(self.window, text="Nombre: ")
        self.lbl.grid(column=0, row=0)
        self.txtContent = StringVar()
        self.txt = Entry(self.window, width=20, textvariable=self.txtContent )
        self.txt.grid(column=1, row=0)
        self.btn = Button(self.window, command= lambda: self.click(), text="Púlsame")
        self.btn.grid(column=2, row=0)
        self.window.mainloop()
class Main(root):
    def __init__(self):
        root.__init__(self)

    def click(self):
        print("Hola " + self.txtContent.get())
        self.txtContent.set("Julio")

obj = Main()
