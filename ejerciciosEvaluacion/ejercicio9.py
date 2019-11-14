class Character (object):
    def __init__(self, text):
        self.text = text

    def count(self):
        whiteSpaces = 0
        for x in self.text:
            if x == " ":
                whiteSpaces += 1
        characters = len(text) - whiteSpaces    
        
        return "El texto tiene {} letras y {} espacios en blanco".format(characters, whiteSpaces)

text = input("Escribe un texto: ")
obj = Character(text)
print(obj.count())


