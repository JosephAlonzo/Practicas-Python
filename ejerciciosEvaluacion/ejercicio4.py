class Nombre():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def concatenarNombre(self):
        return nombre + " " + apellido
    def revers(self):
        return (nombre + " " + apellido) [::-1]


nombre = input("Escribe el nombre: ")
apellido = input("Escribe el apellido: ")

obj = Nombre(nombre, apellido)

print(obj.concatenarNombre())
print(obj.revers())
