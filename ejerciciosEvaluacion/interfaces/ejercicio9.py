from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class root():
    def __init__(self):
       self.window = Tk()
       self.window.geometry("250x50")
       self.menu = Menu(self.window)

       self.radioMenu = Menu(self.menu, tearoff=0)
       self.radioMenu.add_command(label="Agregar", command=self.addRadio)
       self.menu.add_cascade(label="Radio", menu=self.radioMenu)

       self.comboMenu = Menu(self.menu, tearoff=0)
       self.comboMenu.add_command(label="Agregar", command=self.addCombo)
       self.menu.add_cascade(label="Combo", menu=self.comboMenu)

       self.botonMenu = Menu(self.menu, tearoff=0)
       self.botonMenu.add_command(label="Agregar", command = self.addBoton)
       self.menu.add_cascade(label="Boton", menu=self.botonMenu)

       self.entryMenu = Menu(self.menu, tearoff=0)
       self.entryMenu.add_command(label="Agregar", command = self.addEntry)
       self.menu.add_cascade(label="Entry", menu=self.entryMenu)


       self.choiseMenu = Menu(self.menu, tearoff=0)
       self.choiseMenu.add_command(label="Agregar", command =  self.addCheck)
       self.menu.add_cascade(label="Choise", menu=self.choiseMenu)

       self.window.config(menu = self.menu)
       self.window.mainloop()

class elementos(root):
    def __init__(self):
        root.__init__(self)

    def nuevaVentana(self):
        window = Tk()
        window.geometry("250x100")
        return window
    def addRadio(self):
        window = self.nuevaVentana()
        selected = IntVar()
        selected2 = IntVar()
        for i in range(1, 4):
            radio = Radiobutton(window, text="Radio"+str(i), value=i, variable=selected, tristatevalue="x")
            radio.grid(row=0, column=i)
            radio2 = Radiobutton(window, text="Radio"+str(i+3), value=i+3, variable=selected2, tristatevalue="x")
            radio2.grid(row=2, column=i)
    def addCombo(self):
        window = self.nuevaVentana()
        array = []
        for i in range(0,5):
            array.append("value: "+str(i))

        comboList = ttk.Combobox(window, values=array)
        comboList.grid(row=3, column=0)


    def addBoton(self):
        window = self.nuevaVentana()
        boton = Button(window, text="clickeame", command=lambda : messagebox.showinfo("Hiciste click", "Hiciste click"))
        boton.grid(row=5, column=5)
    def addEntry(self):
        window = self.nuevaVentana()
        entrada = Entry(window, width=10)
        entrada.grid(row=3, column=2)
        boton = Button(window, text="Ver Texto", command=lambda :  messagebox.showinfo("Hiciste click", entrada.get()))
        boton.grid(row=3, column=1)
    def addCheck(self):
        window = self.nuevaVentana()
        var1 = IntVar()
        Checkbutton(window, text="check 1", variable=var1).grid(row=0, sticky=W)
        var2 = IntVar()
        Checkbutton(window, text="check 2", variable=var2).grid(row=1, sticky=W)
        mainloop()


obj = elementos()