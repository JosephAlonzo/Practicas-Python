class histogram():
    def __init__(self, array):
        self.array = array.split(",")
        self.array = [ int(x) for x in self.array ]
        self.length = len(self.array)
        self.maxValue = max(self.array) - 1

    def printHistogram(self):
        self.printHistogramHeader()
        self.printContent()
        self.printBaseLine()

    def printContent(self):
        whiteSpace= "_____"
        histogramContent = [ [whiteSpace] * self.length for x in range( self.maxValue+1 ) ]

        histogramContent = self.addValuesInContent(histogramContent)

        cadena = ""
        val =""
        k = self.maxValue+1
        for x in histogramContent:
            for i in range(len(x)):
                val = str(k) if k > 9 else str(k) + " " * (len(str(val)) - 1)
                x[0] = val + "|" + x[0]
                cadena += x[i]
            print(cadena)
            cadena = ""
            k -= 1

    def addValuesInContent(self, histogramContent):
        barra= "_███_"
        i = 0
        j = self.maxValue
        while i < self.length:
            stopValue =  self.maxValue+1 - int(self.array[i])
            while j >= stopValue:
                histogramContent[j][i] = barra
                j-=1
            j= self.maxValue 
            i+=1
        return histogramContent
    
    def printBaseLine(self):
        baseOfHistogram = [ ["     "] * self.length ]

        i = 0 
        cadena = "  "
        for x in baseOfHistogram[0]:
            x = "  " + str(self.array[i]) + "  "
            cadena += x
            i+= 1
        print(cadena)

    def printHistogramHeader(self):
        histogramHeader = [ ["     "] * self.length ]

        cadena = ""
        histogramHeader[0][ int(self.length / 2) ]  = "* Histograma *"

        for x in histogramHeader[0]:
            cadena += x
        print("\n" + cadena + "\n")

        
obj = histogram(input("Escribe una lista de numeros divididos por comas(,) ejemplo: 5,4,8: "))
obj.printHistogram()

# def printHostograma(array):
#     array = array.split(",")
#     i = 0
#     cadena = ""
#     for x in array:
#         while i < x:
#             cadena += "*"
#             i+=1
#         print(cadena)
#         cadena = ""
#         i = 0
    
    
