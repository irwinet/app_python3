from tkinter import *

#Configuracion de la raiz
root = Tk()

"""
# variables dinamicas
texto = StringVar()
texto.set("Un nuevo texto")

#Configuracion de un marco
#frame = Frame(root, width=480, height=320)
#frame.pack()

#label = Label(root, text="Hola Mundo")
#label.place(x=500, y=500) # x=0 y = 0
#label.pack()

Label(root, text="Hola Mundo").pack(anchor="nw")

label = Label(root, text="Otra etiqueta")
label.pack(anchor="center")
label.config(bg="green", fg="blue", font=("Verdana",24))
label.config(textvariable=texto)

Label(root, text="Ultima etiqueta").pack(anchor="se")
"""

imagen = PhotoImage(file="./imagen.gif")
Label(root, image=imagen, bd=0).pack(side="left")

#Finalmente bucle de la aplicacion
root.mainloop()