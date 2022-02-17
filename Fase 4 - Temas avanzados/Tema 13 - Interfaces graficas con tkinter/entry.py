from tkinter import *

#Configuracion de la raiz
root = Tk()

#frame = Frame(root)
#frame.pack()

label = Label(root, text="Nombre")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="right", state="normal") #disabled


# frame2 = Frame(root)
# frame2.pack()

label2 = Label(root, text="Contraseña")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="center", show="*")





#Finalmente bucle de la aplicacion
root.mainloop()