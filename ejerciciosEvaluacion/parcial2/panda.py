import pandas as objPandas
from pandas import ExcelWriter

archivo = objPandas.DataFrame({
    'matricula': [12345, 1235],
    'Nombre': ['Joseph', 'pedro'],
    'Apellido': ['Mendez', 'lopez']
})

archivo = archivo[['matricula' , 'Nombre', 'Apellido']]

rut = ExcelWriter(r'C:\Users\Joseph\Desktop\excell\utm.xlsx')

archivo.to_excel(rut, 'Hoja de datos', index=False)

rut.save()