class calculadora(object):
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

objeto = calculadora(3,4)
print(objeto.sumar())
print(objeto.restar())
print(objeto.multiplicar())
print(objeto.dividir())

a = float(input("Escribe un numero"))
b = float(input("Escribe otro numero"))

objeto = calculadora(a,b)

print(objeto.sumar())
print(objeto.restar())
print(objeto.multiplicar())
print(objeto.dividir())
