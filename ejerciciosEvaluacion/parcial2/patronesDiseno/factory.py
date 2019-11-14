import tkinter as tk


class Ventanas:

    def __init__(self):
        self.name = None
        self.size = None

    def getName(self):
        return self.name

    def getSize(self):
        return self.size


class Mediana(Ventanas):
    def __init__(self, name):
        print("Soy Mediana " + name)
        window = tk.Tk()
        window.title(name)
        window.geometry('250x350')
        window.mainloop()


class Grande(Ventanas):
    def __init__(self, name):
        print("Soy Grande " + name)
        window = tk.Tk()
        window.title(name)
        window.geometry('500x600')
        window.mainloop()


class Chica(Ventanas):
    def __init__(self, name):
        print("Soy Chica " + name)
        window = tk.Tk()
        window.title(name)
        window.geometry('100x200')
        window.mainloop()


class Factory:
    def getDatos(self, name, gender):

        if gender == 'M':
            return Mediana(name)
        if gender == 'G':
            return Grande(name)
        if gender == 'C':
            return Chica(name)


if __name__ == '__main__':
    factory = Factory()
    FabVentana = factory.getDatos("Chica", "C")
