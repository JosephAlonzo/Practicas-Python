import random
from tkinter import * 
from tkinter import messagebox 
from gato import Player
from gato import Gato

class root():
    def __init__(self):
        self.window = Tk()
        self.window.title("Juego del gato")
        self.frame = Frame(self.window)
        self.frame.grid(row=3, column=0)
        self.lbl = Label(self.window, text="Player 1: X")
        self.lbl2 = Label(self.window, text="Player 2: O")
        self.txt = Entry(self.window, width=15, state='normal')
        self.txt2 = Entry(self.window, width=15, state='normal')
        self.lbl.grid(sticky="W", column=0 ,row=0)
        self.lbl2.grid(sticky="W",column=0 ,row=1)
        self.txt.grid(column=1, row=0)
        self.txt2.grid(column=1, row=1)
        self.b = Button(self.window, text="Comenzar", command=self.start)
        self.b.grid(column=0, row=2)
        self.player1 = Player("","")
        self.player2 = Player("","")
        self.juego = Gato(self.player1, self.player2)
        self.currentPlayer = ""

        self.btn = ""
        self.text = ""   
        self.window.mainloop()

class main(root):

    def __init__(self):
        root.__init__(self)
        
    def start(self):
        self.b['text'] = "Reiniciar"
        self.txt.grid(column=0, row=0)
        self.txt2.grid(column=0, row=1)
        self.player1 = Player(self.txt.get(), "X")
        self.player2 = Player(self.txt2.get(), "O")
        self.juego = Gato(self.player1, self.player2)
        self.btn = [["-" for x in range(3)] for x in range(3)]
        self.text = [["-" for x in range(3)] for x in range(3)]    
        list = [self.player1, self.player2]
        self.currentPlayer = random.choice(list)
        i =0
        j=0
        for x in self.btn:
            for y in x:
                self.btn[i][j] = Button(self.frame, text= "".format(i,j), font=('Times 20 bold'), bg="gray", fg="white", height=4, width=8, command= lambda x1=i, y1=j : self.click(x1,y1) )
                self.btn[i][j].grid(column=j, row=i)
                j+=1
            j=0
            i+=1
        messagebox.showinfo("Jugador elegido al azar", "El jugador : \n{} comienza".format(self.currentPlayer.name))

    def click(self, x,y):
        self.btn[x][y]['text'] = self.currentPlayer.symbol
        self.text[x][y] = self.currentPlayer.symbol
        self.btn[x][y]['state'] = 'disabled'
        self.btn[x][y]['disabledforeground'] = 'white'
        
        if self.juego.checkIfPlayerWon( self.text, self.currentPlayer):
            res = messagebox.askyesno("Tenemos un ganador", "El jugador {} gano \n ¿Quieres jugar de nuevo?".format(self.currentPlayer.name))
            if res:
                self.start()
            else:
                self.window.quit()
        
        elif self.currentPlayer == self.player1:
           self.currentPlayer = self.player2
        elif self.currentPlayer == self.player2: 
            self.currentPlayer = self.player1
        
obj = main()