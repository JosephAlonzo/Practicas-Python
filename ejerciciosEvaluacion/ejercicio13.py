class Character(object):
    def __init__(self, n):
        self.n = n

    def multiplyCharacter(self):
        return str(self.n) * int(self.n)
    
n = input("Escribe un numero: ")
obj = Character(n)
print(obj.multiplyCharacter())