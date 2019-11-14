import random

class JuegoMatematico(object):
    def __init__(self):
        self.val1 = 0
        self.val2 = 0
        self.currentOperation = 0
        self.juegos = 0
        self.juegosMalos = 0
        self.juegosBuenos = 0
        self.maxValue = 10
        self.minValue = 0
        self.operaciones =["+", "-", "*", "/"]
        
    def start(self):
        self.val1 = random.randint(self.minValue, self.maxValue)
        self.val2 = random.randint(self.minValue, self.maxValue)
        self.currentOperation = random.randint(0, 3)

    def checkAnswer(self, answer):
        correctAnswer = ""
        if self.operaciones[self.currentOperation] == "+":
            correctAnswer = self.val1 + self.val2
        elif self.operaciones[self.currentOperation] == "-":
            correctAnswer = self.val1 - self.val2
        elif self.operaciones[self.currentOperation] == "*":
            correctAnswer = self.val1 * self.val2
        elif self.operaciones[self.currentOperation] == "/":
            correctAnswer = self.val1 / self.val2

        if answer == correctAnswer:
            self.juegosBuenos +=1 
        else:
            self.juegosMalos += 1
        self.juegos += 1

    def changeDifficulty(self, difficulty):
        if difficulty == 0:
            self.maxValue = 10
            self.minValue = 0
        elif difficulty == 1:
            self.maxValue = 100
            self.minValue = 0
        elif difficulty == 2:
            self.maxValue = 1000
            self.minValue = 0
        self.juegosBuenos = 0
        self.juegos = 0
        self.juegosMalos = 0
        self.val1 = 0
        self.val2 = 0
        self.currentOperation = 0
