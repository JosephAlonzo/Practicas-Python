class Bank(object):

    def calculateInterestRate(self, dollars, interestRate, years):
        dollars += (dollars * interestRate)
        years -= 1
        if years > 0:
            return self.calculateInterestRate(dollars, interestRate, years)
        else:
            return dollars

dollars = int(input("Escribe el numero de dolares: "))
interestRate = float(input("Escribe la tasa de interes por año: "))
years = int(input("Escribe el numero de años: "))

obj = Bank()

print( obj.calculateInterestRate(dollars, interestRate, years) )