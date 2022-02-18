import sqlite3
from tkinter import *

#Configuracion de la raiz
root = Tk()
root.title("Bar Don Irwin - Menu")
root.resizable(0,0)
root.config(bd=25, relief="sunken")

Label(root, text="   Bar Don Irwin   ", fg="darkgreen", font=("Times New Roman",28,"bold italic")).pack()
Label(root, text="   Menú del dia   ", fg="green", font=("Times New Roman",24,"bold italic")).pack()

# Separacion de titulos y categorias
Label(root, text="").pack()

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

# Buscar las categorias y platos de la bd
categorias = cursor.execute("SELECT * FROM categoria").fetchall()

for categoria in categorias:    
    Label(root, text=categoria[1], fg="black", font=("Times New Roman",20,"bold italic")).pack()
    platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
    for plato in platos:
        Label(root, text=plato[1], fg="gray", font=("Verdana",15,"italic")).pack()

    # Separacion de titulos y categorias
    Label(root, text="").pack()

# conexion.commit()
conexion.close()

#Precio del menu
Label(root, text="12$ (IVA incl.)", fg="darkgreen", font=("Times New Roman",15,"bold italic")).pack(side="right")

root.mainloop()