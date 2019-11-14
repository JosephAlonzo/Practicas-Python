from calculadora import calculadora
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Calculadora")
window.geometry('350x200')

lbl = Label(window, text="Introduce los numeros")
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=0, row=1)

txt2 = Entry(window, width=10)
txt2.grid(column=1, row=1)

def resolver(Operacion):
    num1 = int(txt.get())
    num2 = int(txt2.get())
    obj = calculadora(num1, num2)
    if Operacion == "sumar":
        messagebox.showinfo( "Resultado ", str(obj.sumar()) )
    elif Operacion == "restar":
        messagebox.showinfo( "Resultado ",str(obj.restar()) )
    elif Operacion == "multiplicar":
        messagebox.showinfo( "Resultado ",str(obj.multiplicar()) )
    elif Operacion == "dividir":
        messagebox.showinfo( "Resultado ",str(obj.dividir()) )


btn = Button(window, text="sumar", command= lambda: resolver("sumar"))
btn.grid(column=0, row=2)
btn2 = Button(window, text="restar", command= lambda: resolver("restar"))
btn2.grid(column=1, row=2)
btn3 = Button(window, text="multiplicar", command= lambda: resolver("multiplicar"))
btn3.grid(column=0, row=3)
btn4 = Button(window, text="dividir", command= lambda: resolver("dividir"))
btn4.grid(column=1, row=3)
window.mainloop()