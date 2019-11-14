
#declarar funcion saludar (Paradigma funcional)
def saludar():
    print('hola mundo')
#Lllamando a la funcion saludar 
saludar()

#saludar con un argumento

# def hablar(nombre):
#     print('hola ' + nombre )

#invocar función
# print("escribe un nombre")
# nombre = input()
# hablar(nombre)

#leer 2 numeros 

def sumar (numero1, numero2):
    resultado = numero1 + numero2
    print( "el resultado es: " + str(resultado) )

print("escribe el numero 1")
numero1 = int(  input() )
print("escribe el numero2")
numero2 = int(  input() )

sumar(numero1,numero2)