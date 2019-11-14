class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):
    def __init__(self,color, ruedas, velocidad, cilandrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilandrada = cilandrada
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h {} cc".format(self.velocidad, self.cilandrada)

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilandrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilandrada)
        self.carga = carga
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h {} cc".format(self.velocidad, self.cilandrada)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} tipo".format(self.tipo)

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilandrada):
        Bicicleta.__init__(self, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilandrada = cilandrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h {} cc".format(self.velocidad, self.cilandrada)

def catalogar(vehiculos, ruedas = False ):
    count = 0
    ruedas = str(ruedas)
    for x in vehiculos:
        if ruedas:
            if x.ruedas == int(ruedas):
                count +=1
                print(x.__class__.__name__)
                print(str(x ) + "\n")
        else:
            print(x.__class__.__name__)
            print(str(x ) + "\n")
    if ruedas:
        print("Se han encontrado {} vehículos con {} ruedas".format(count, ruedas))

        

c = Coche("azul", 4, 150, 1200)
ca = Camioneta("negra", 4, 150, 1200, 1000)
b = Bicicleta("verde", 2, "urbana")
m = Motocicleta("roja", 2, "deportiva", 200, 1500)

vehiculos = [ c , ca, b, m]

catalogar(vehiculos, 2)

       