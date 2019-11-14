class Rimas():
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def checkIfRhyme(self):
        if(self.word1[-3:] == self.word2[-3:]):
            return "Las palabras riman"
        elif (self.word1[-2:] == self.word2[-2:]):
            return "las palabras riman un poco"
        else:
            return "No riman"

word1= input("Escribe una palabra: ")
word2= input("Escribe otra palabra: ")
obj = Rimas(word1, word2)

print(obj.checkIfRhyme())