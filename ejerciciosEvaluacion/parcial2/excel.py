from openpyxl import load_workbook
 
archivo = load_workbook('template.xlsx')
 
# leer y prepara para escribir
datosTemplate = archivo.active
 
# Celdas para llenar datos
datosTemplate['B2'] = '5D' #la columna de grado y grupo
datosTemplate['B3'] = 'TIC-ITI Sep-Dic 2019' # Carrera y periodo sep-dic,etc..
 
# Fechas de Parciales y extras
datosTemplate['B8'] ='04-oct'  #fecha primer parcial
datosTemplate['C8'] ='06-nov'  #fecha segundo parcial
datosTemplate['D8'] ='06-dic'  #fecha tercer parcial
datosTemplate['E8'] ='13-dic'   #fecha ordinarios
datosTemplate['F8'] ='09-ene'   #fecha primer extra
datosTemplate['G8'] ='09-ene'  #fecha segundo extra
 
 
# Formato final para guardar
archivo.save("sample1.xlsx")