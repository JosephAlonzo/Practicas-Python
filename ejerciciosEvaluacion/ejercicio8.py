class Conversiones(object):
    
    def convertToHex(self, number):
        x = number % 16
        digits = "0123456789ABCDEF"
        rest = number / 16
        if (int(rest) == 0):
            return digits[x]
        return self.convertToHex(int(rest)) + digits[x]

number = int(input("Escribe el numero que quieres convertir a hexadecimal: "))
obj = Conversiones()
print(obj.convertToHex(number))