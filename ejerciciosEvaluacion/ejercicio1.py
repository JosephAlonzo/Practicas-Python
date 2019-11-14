import re

class user(object):
    username= ""
    message=""
    
    def __init__(self, username):
        self.username = username
    
    def validateUserName(self):
        self.validateRegex()
        if len(self.message) == 0:
            return True
        return False
    
    def validateRegex(self):
        if re.match("[a-zA-Z0-9]{6,12}$", self.username):
            return True
        elif re.match("[a-zA-Z0-9]{0,5}$", self.username):
            self.message = "El nombre de usuario debe contener al menos 6 caracteres"
        elif re.match("[a-zA-Z0-9]{13,}$", self.username):
            self.message = "El nombre de usuario no puede contener más de 12 caracteres"
        elif re.match("[a-zA-Z0-9]$", self.username) == None:
            self.message = "El nombre de usuario puede contener solo letras y números"


obj = user(input("Escribe el nombre del usuario: "))

if obj.validateUserName():
    print( "El usuario es valido")
else:
    print(obj.message)