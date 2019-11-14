from tkinter import *
from tkinter.ttk import *

#poner otro grupo de radios sin que se marque el otro
window = Tk()
window.title("Hola")
window.geometry("350x200")
chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text="choose", var=chk_state)
chk.grid(column=0, row=0)

rad1 = Radiobutton(window, text="First", value=1)
rad2 = Radiobutton(window, text="Second", value=2)
rad3 = Radiobutton(window, text="third", value=3)

rad4 = Radiobutton(window, text="uno", value=4)
rad5 = Radiobutton(window, text="dos", value=5)
rad6 = Radiobutton(window, text="tres", value=6)

rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)
rad3.grid(column=2, row=1)

rad4.grid(column=0, row=2)
rad5.grid(column=1, row=2)
rad6.grid(column=2, row=2)

window.mainloop()