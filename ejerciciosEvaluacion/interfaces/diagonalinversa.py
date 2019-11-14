class diagonalInversa():
    def __init__(self, n):
        self.array = [["" for x in range(n)] for x in range(n)]
        self.result = 0
    def llenarArray(self):
        i = 0
        j= 0
        for x in self.array:
            for y in x:
                self.array[i][j] = int(input("Escribe el numero en la posicion {}, {}: ".format( i , j) ))
                j+=1
            i +=1
            j=0
    def checkCross(self):
        for i in range(len( self.array[0]) ):
                self.array[i] = self.array[i][::-1]
                self.result += self.array[i][i]
        print( "La suma de la diagonal inversa es: " + str(self.result) )
obj = diagonalInversa( int(input("Elige el tamaño de tu matriz: ")  ) )
obj.llenarArray()
obj.checkCross()