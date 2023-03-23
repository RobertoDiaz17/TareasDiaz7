import sqlite3
import tkinter as tk

# Creación de la ventana principal
root = tk.Tk()
root.title("Gestión De Sabores De Helado")

# Creación de la base de datos y la tabla si no existen
conn = sqlite3.connect('helados.db')
conn.execute('''CREATE TABLE IF NOT EXISTS sabores
                (ID INT PRIMARY KEY NOT NULL,
                SABOR TEXT NOT NULL,
                PRECIO FLOAT NOT NULL);''')
conn.commit()

# Función para insertar un nuevo sabor en la base de datos
def insertar_sabor():
    id = int(id_entry.get())
    sabor = sabor_entry.get()
    precio = float(precio_entry.get())
    conn.execute("INSERT INTO sabores (ID, SABOR, PRECIO) \
                  VALUES (?, ?, ?)", (id, sabor, precio))
    conn.commit()
    mostrar_sabores()

# Función para mostrar los sabores y sus precios en la lista
def mostrar_sabores():
    sabores_listbox.delete(0, tk.END)
    cursor = conn.execute("SELECT ID, SABOR, PRECIO from sabores")
    for row in cursor:
        sabores_listbox.insert(tk.END, f"{row[1]} - ${row[2]:.2f}")

# Creación de los widgets en la ventana
tk.Label(root, text="ID:").grid(row=0, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

tk.Label(root, text="Sabor:").grid(row=1, column=0)
sabor_entry = tk.Entry(root)
sabor_entry.grid(row=1, column=1)

tk.Label(root, text="Precio:").grid(row=2, column=0)
precio_entry = tk.Entry(root)
precio_entry.grid(row=2, column=1)

insertar_button = tk.Button(root, text="Insertar", command=insertar_sabor)
insertar_button.grid(row=3, column=1)

sabores_listbox = tk.Listbox(root)
sabores_listbox.grid(row=6, column=0, columnspan=8)
mostrar_sabores()

# Arranque de la ventana
root.mainloop()

# Cierre de la conexión a la base de datos
conn.close()
