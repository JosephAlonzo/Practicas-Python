class saludo(object):
    #atributos
    nombre="Joseph"
    apellidos="Alonzo aranda"
    #Metodo
    def saludar(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        print("Hola " + self.nombre + " " + self.apellidos)

nombre = input()
apellidos = input()

objeto = saludo()
objeto.saludar(nombre, apellidos)