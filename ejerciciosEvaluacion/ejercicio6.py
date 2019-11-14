class Operaciones():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def get_numbers(self):
        if self.num1 + self.num2 >= 50:
            return self.multiplicar(self.num1, self.num2)
        else:
            return self.imprimirMedia()

    def multiplicar(self, num1, num2):
        return num1 * num2

    def imprimirMedia(self):
        total = 0
        num = 0
        i=0
        print("VAMOS A CREAR UNA MEDIA ARITMETICA")
        while i < 10:
            num = input("Escribe el numero " + str(i + 1 ) + ": ")
            total += float( num )
            i+=1
        return ( total / 10 )

num1 = float(input("Escribe el numero 1: "))
num2 = float(input("Escribe el numero 2: "))
obj = Operaciones(num1, num2)

print(obj.get_numbers())