from tkinter import *
from juegoMatematico import JuegoMatematico

class root(JuegoMatematico):
    def __init__(self):
        JuegoMatematico.__init__(self)
        self.root = Tk()
        self.root.title("Juego matematico - [Preview]")

        self.txtContent = StringVar()
        self.txt = Entry(self.root, width=10, textvariable = self.txtContent)
        self.txt.grid(column=0, row=0)

        self.txtContent2 = StringVar()
        self.txt2 = Entry(self.root, width=10, textvariable = self.txtContent2)
        self.txt2.grid(column=2, row=0)
        self.lbl = Label(self.root, text="  ")
        self.lbl.grid(column=1, row=0)


        self.selected = IntVar()
        self.rad = Radiobutton(self.root, text="Sumar", value=0, variable=self.selected)
        self.rad.grid(column=0, row=1,sticky="W")

        self.rad2 = Radiobutton(self.root, text="Restar", value=1, variable=self.selected)
        self.rad2.grid(column=0, row=2,sticky="W")

        self.rad3 = Radiobutton(self.root, text="Multiplicar", value=2, variable=self.selected)
        self.rad3.grid(column=0, row=3,sticky="W")

        self.rad4 = Radiobutton(self.root, text="Dividir", value=3, variable=self.selected)
        self.rad4.grid(column=0, row=4,sticky="W")

        self.btn = Button(self.root, text="Nuevo Número", command= lambda: self.changeNumber() )
        self.btn.grid(column=3, row=1,sticky="W")

        self.txtContent3 = StringVar()
        self.txt3 = Entry(self.root, width=15, textvariable = self.txtContent3)
        self.txt3.grid(column=3, row=2,sticky="W")

        self.btn2 = Button(self.root, text="Resultado", command= lambda: self.sendResult())
        self.btn2.grid(column=3, row=3)

        self.lbl2 = Label(self.root, text="Juegos: 0")
        self.lbl2.grid(column=3, row=5,sticky="W")

        self.lbl3 = Label(self.root, text="Buenos: 0")
        self.lbl3.grid(column=3, row=6,sticky="W")

        self.lbl4 = Label(self.root, text="Malos: 0")
        self.lbl4.grid(column=3, row=7,sticky="W")


        self.selected2 = IntVar()
        self.rad4 = Radiobutton(self.root, text="Facil", value=0, variable=self.selected2, command= lambda : self.onDifficultyChange() )
        self.rad4.grid(column=0, row=9)

        self.rad5 = Radiobutton(self.root, text="Medio", value=1, variable=self.selected2, command= lambda : self.onDifficultyChange() )
        self.rad5.grid(column=1, row=9)

        self.rad6 = Radiobutton(self.root, text="Dificil", value=2, variable=self.selected2, command= lambda : self.onDifficultyChange() )
        self.rad6.grid(column=2, row=9)

        # self.lbl5 = Label(self.root, text=60, font=("Digital-7", 40), bd=2, relief="ridge", padx=20)
        # self.lbl5.grid(column=0, row=10)
        
        self.root.mainloop()


class Main(root):

    def __init__(self):
        root.__init__(self)  

    def changeNumber(self):
        self.start()
        self.txtContent.set(self.val1)
        self.txtContent2.set(self.val2)
        self.lbl['text'] = self.operaciones[self.currentOperation] + "  "
        self.selected.set(int(self.currentOperation))

    def sendResult(self):
        if self.txt3.get() == "":
            answer = 0
        else: 
            answer = float( self.txt3.get() )
        self.checkAnswer(answer)
        
        self.lbl2['text'] = "Juegos: {}".format(self.juegos)
        self.lbl3['text'] = "Juegos Buenos: {}".format(self.juegosBuenos)
        self.lbl4['text'] = "Juegos Malos: {}".format(self.juegosMalos)
        self.changeNumber()
        self.txtContent3.set("")

    def onDifficultyChange(self):
        difficulty = self.selected2.get()
        self.changeDifficulty(difficulty)

        self.lbl['text'] = "  "
        self.lbl2['text'] = "Juegos: {}".format(self.juegos)
        self.lbl3['text'] = "Juegos Buenos: {}".format(self.juegosBuenos)
        self.lbl4['text'] = "Juegos Malos: {}".format(self.juegosMalos)
        self.txtContent.set("")
        self.txtContent2.set("")
        self.txtContent3.set("")
    

obj = Main()