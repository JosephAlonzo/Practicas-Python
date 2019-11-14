class Oculta_x():
    def __init__(self):
        self.__x = 0
    def mostrar_x (self):
        return self._Oculta_x__x
    def incrementa_x(self):
        self._Oculta_x__x += 1

class ClaseOtroEjemplo():
    def __init__(self):
        self.publico = 'variable publica'
        self.__privado = 'variable privada'
    def obtener_privado(self):
        print(self.__privado)
        
o = ClaseOtroEjemplo()
o.obtener_privado()