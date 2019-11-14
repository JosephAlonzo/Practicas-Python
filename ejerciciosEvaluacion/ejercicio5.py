class Persona():

    def __init__(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.estado = estado
    
class Ciudadano(Persona):
        
    def __init__(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado):
        Persona.__init__(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado)
        self.claves = [
            ["AGUASCALIENTES", "AS"],
            ["BAJACALIFORNIA", "BC"],
            ["BAJACALIFORNIASUR", "BS"],
            ["CAMPECHE", "CC"],
            ["COAHUILA", "CL"],
            ["COLIMA", "CM"],
            ["CHIAPAS", "CS"],
            ["CHIHUAHUA", "CH"],
            ["DF", "DF"],
            ["DURANGO", "DG"],
            ["GUANAJUATO", "GT"],
            ["GUERRERO", "GR"],
            ["HIDALGO", "HG"],
            ["JALISCO", "JC"],
            ["MEXICO", "MC"],
            ["MICHOACAN", "MN"],
            ["MORELOS", "MS"],
            ["NAYARIT", "NT"],
            ["NUEVO LEON", "NL"],
            ["OAXACA", "OC"],
            ["PUEBLA", "PL"],
            ["QUERETARO", "QT"],
            ["QUINTANA ROO", "QR"],
            ["SAN LUIS POTOSI", "SP"],
            ["SINALOA", "SL"],
            ["SONORA", "SR"],
            ["TABASCO", "TC"],
            ["TAMAULIPAS", "TS"],
            ["TLAXCALA", "TL"],
            ["VERACRUZ", "VZ"],
            ["YUCATAN", "YN"],
            ["ZACATECAS", "ZS"]
        ]


    def getCurp(self):
        curp = self.apellido_paterno[0:1] + self.getVocal(self.apellido_paterno[1:]) + self.apellido_materno[0:1] + self.nombre[0:1] + self.dateFormat() + self.sexo[0:1] + self.getClaveEstado() + self.getConsonante(self.apellido_paterno[1:]) + self.getConsonante(self.apellido_materno[1:]) + self.getConsonante(self.nombre[1:]) 
        return curp.upper()

    def getVocal(self, txt):
        vocales = "aeiou"
        for x in txt:
            for y in vocales:
                if y == x:
                    return y
    def dateFormat(self):
        newDate = self.fecha_nacimiento.split("/")
        newDate = newDate[::-1]
        newDate[0] = newDate[0][-2:]
        newDate = "".join(newDate)
        return str(newDate)
        
    def getClaveEstado(self):
        for x in self.claves:
            if x[0] == self.estado.upper():
                return x[1]
        else:
            return "NE"

    def getConsonante(self, txt):
        consonantes = "bcdfghjklmnpqrstvwxyz"
        for x in txt:
            for y in consonantes:
                if y == x:
                    return y

class Contribuyente(Ciudadano):
    def __init__(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado):
        Ciudadano.__init__(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado)

    def getRFC(self):
        rfc = self.apellido_paterno[0:1] + self.getVocal(self.apellido_paterno[1:]) + self.apellido_materno[0:1] + self.nombre[0:1] + self.dateFormat()
        return rfc

    def getDocument(self):
        if int(self.fecha_nacimiento[-4:]) > 2000:
            return self.getRFC()
        else:
            return self.getCurp()

nombre = input("Escribe tu nombre: ")
apellido_paterno = input("Escribe tu primer apellido: ")
apellido_materno = input("Escribe tu segundo apellido: ")
fecha_nacimiento = input("Escribe tu fecha de nacimiento (dd/mm/yyyy): ")
sexo = input("Escribe tu sexo (Hombre o Mujer): ")
estado = input("Escribe tu estado: ")

# obj = Contribuyente("joseph", "alonzo", "aranda", "26/12/1996", "Hombre", "Yucatan")
obj = Contribuyente(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado)

print(obj.getDocument())