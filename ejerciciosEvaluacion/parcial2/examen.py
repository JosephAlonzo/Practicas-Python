from tkinter import *


class btnCreator(object):

    class __btnCreator:
        def __init__(self, texto,ventana):
            self.texto = texto
            self.ventana = ventana
            self.btn = Button(self.ventana, text= self.texto)
            self.btn.place(x=60, y=30)
            
    instance = None

    def __new__(cls, texto, ventana):
        if not btnCreator.instance:
            btnCreator.instance = btnCreator.__btnCreator(texto, ventana)
        else:
            btnCreator.__btnCreator(texto, ventana)
        return btnCreator.instance

class Main():
    def __init__(self):
        self.ventanaPrincipal = Tk()
        self.ventanaPrincipal.title("Ventana Principal")
        self.ventanaPrincipal.geometry("300x150")
        self.contador=1
        self.btnAbrir = Button(self.ventanaPrincipal, text="Crear Botón", command=self.EventoBoton)
        self.btnAbrir.place(x=0, y=0)
        self.ventanaPrincipal.mainloop()
    
    def EventoBoton(self):
        texto = "Boton"+str(self.contador)
        btnNuevo=btnCreator(texto, self.ventanaPrincipal)
        btnNuevo.texto = texto
        print(btnNuevo)
        self.contador=self.contador+1

obj = Main()
