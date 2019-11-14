class Operaciones(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def sumar(self):
        return self.a+self.b
    def restar(self):
        return self.a-self.b
    def dividir(self):
        return self.a/self.b
    def multiplicar(self):
        return self.a*self.b
    def porcentage(self):
        return (self.a+self.b)/100
    def mod(self):
        return self.a%self.b