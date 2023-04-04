import tkinter as tk
import mysql.connector
from tkinter import ttk

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mercado"
)

mi_cursor = bd.cursor()
mi_cursor.execute("SELECT * from ventas")
resultado = mi_cursor.fetchall()

# crear ventana de Tkinter
ventana = tk.Tk()
ventana.title("REGISTRO DE VENTAS")

# crear Table
tabla = ttk.Treeview(ventana)
tabla['columns'] = ('Producto', 'Precio','Piezas')

# ajustar las columnas
tabla.column('#0', width=0, stretch=tk.NO)
tabla.column('Producto', anchor=tk.CENTER, width=200)
tabla.column('Precio', anchor=tk.CENTER, width=300)
tabla.column('Piezas', anchor=tk.CENTER, width=400)

# heading
tabla.heading('#0', text='', anchor=tk.CENTER)
tabla.heading('Piezas', text='Piezas', anchor=tk.CENTER)
tabla.heading('Precio', text='Precio', anchor=tk.CENTER)
tabla.heading('Producto', text='Producto', anchor=tk.CENTER)

# agregar datos
for Codigo in resultado:
  tabla.insert(parent='', index='end', iid=Codigo[0], values=(Codigo[1], Codigo[2],Codigo[3]))

# mostrar tabla en ventana
tabla.pack()

ventana.mainloop()