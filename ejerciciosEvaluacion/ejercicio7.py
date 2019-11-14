from datetime import datetime

class Zodiaco():
    def __init__(self, dia, mes):
        self.mes = mes
        self.dia = dia
        self.zodiacSigns = [
            [ "Acuario" , "21", "01"],#0
            [ "Piscis" , "19", "02"],#1
            [ "aries" , "21", "03"],#2
            [ "Tauro" , "21", "04"],#3
            [ "Geminis" , "22", "05"],#4
            [ "Cancer" , "22", "06"],#5
            [ "Leo" , "23", "07"],#6
            [ "Virgo" , "24", "08"],#7
            [ "Libra" , "24", "09"],#8
            [ "Escorpio" , "24", "10"],#9
            [ "Sagitario" , "23", "11"],#10
            [ "Capricornio" , "22", "12"]#11
        ]

    def getSign(self):
        #año, mes, dia
        userDate = datetime(1980, self.mes, self.dia)

        i = 0
        lengthArray = len(self.zodiacSigns) - 1

        while i < lengthArray:
            zodiacSignDate = datetime(1980, int(self.zodiacSigns[i][2]), int(self.zodiacSigns[i][1]))
            nextZodiacSignDate = datetime(1980, int(self.zodiacSigns[i+1][2]), int(self.zodiacSigns[i+1][1]))

            if userDate >= zodiacSignDate and userDate < nextZodiacSignDate:
                return self.zodiacSigns[i][0]
            i += 1
        return self.zodiacSigns[i][0]

dia = int(input("Escribe tu dia de nacimiento: "))
mes = int(input("Escribe tu mes de nacimiento: "))
obj = Zodiaco(dia, mes)
sign = obj.getSign()
print("Tu signo zodiacal es: {}". format( sign ) )