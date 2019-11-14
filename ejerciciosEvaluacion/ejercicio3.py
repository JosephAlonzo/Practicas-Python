class bisiesto():
    def __init__(self, year):
        self.year = year

    def es_bisiesto(self):
        if self.year%4 == 0 and self.year%100 > 0 or self.year%400 == 0:
            return True
        return False
   
obj = bisiesto(int(input("Escribe el año que deseas verificar: ")))
if obj.es_bisiesto():
    print("El año es bisiesto")
else:
    print("El año NO es bisiesto")
