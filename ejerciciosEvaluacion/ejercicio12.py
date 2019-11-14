class Palabra(object):
    def __init__(self, word ):
        self.word = word

    def isPalindrome(self):
        self.word = self.word.replace(" ", "").lower()
        if(self.word == self.word[::-1]):
            return "Es palindroma"
        else:
            return "NO es palindroma"

word = input("Escribe una palabra: ")
obj = Palabra(word)
print(obj.isPalindrome())