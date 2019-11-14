try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
from tkcalendar import Calendar, DateEntry
from openpyxl import load_workbook
import datetime
 
class printExcel():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x150")
        self.entry = ttk.Entry(self.root)
        self.entry.place(x=50, y=50)
        self.btn = ttk.Button(self.root, text='Calendar', command= lambda: self.example1() ).pack(padx=10, pady=10)
        self.btn2 = ttk.Button(self.root, text='Crear excel', command= lambda:self.createExcel())
        self.btn2.place(x=50, y=100)
        self.root.mainloop()

    def example1(self):
        def print_sel():
            print(cal.selection_get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, cal.selection_get())
            top.destroy()
    
        top = tk.Toplevel(self.root)
        cal = Calendar(top,
                    font="Arial 14", selectmode='day',
                    cursor="hand1", year=2019, month=10, day=24)
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=print_sel).pack()

    def createExcel(self):
        
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
        
        date = str(self.entry.get())
        date = date.split("-")
        date = datetime.datetime( int(date[0]), int(date[1]), int(date[2]) )
        
        print(self.date_format(date))
        datosTemplate['B8'] = self.date_format(date)
        
        
        # Formato final para guardar
        archivo.save("calendario.xlsx")

    def date_format(self, date):
        months = ("Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic")
        day = date.day
        month = months[date.month - 1]
        formato = "{}-{}".format(day, month)

        return formato


obj = printExcel()