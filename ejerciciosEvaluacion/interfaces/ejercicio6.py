from tkinter import *
from tkinter import ttk 

class root():
    def __init__(self):
        self.window = Tk()
        self.window.title("Peliculas - [Preview]")
        self.lbl= Label(self.window, text= "Escribe el titulo de una pelicula" )
        self.lbl.grid(column= 0, row=0, pady=(20,0))
        self.txtContent = StringVar()
        self.txt = Entry(self.window, width=20, textvariable=self.txtContent )
        self.txt.grid(column=0, row=1,sticky="N", pady=(20,0))
        self.btn = Button(self.window, text="Añadir", command= lambda: self.add())
        self.btn.place(x=60, y=90)
        self.lbl2= Label(self.window, text= "Peliculas")
        self.lbl2.grid(column= 1, row=0, pady=(20,0))
        self.listbox = Listbox(self.window)
        self.listbox.grid(column=1, row=1, pady=20, padx=20)

        self.window.mainloop()
        
class Peliculas(object):
    def __init__(self):
        root.__init__(self)  

    def add(self):
        self.listbox.insert(END, self.txtContent.get())
        self.txtContent.set("")

obj = Peliculas()
