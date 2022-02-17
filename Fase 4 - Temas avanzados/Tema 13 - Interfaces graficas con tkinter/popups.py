from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

#Configuracion de la raiz
root = Tk()

def test():
    #MessageBox.showinfo("Hola!", "Hola Mundo")
    #MessageBox.showwarning("Alerta!", "Seleccion solo para administradores")
    #MessageBox.showerror("Error!", "Ha ocurrido un error")
    
    # resultado = MessageBox.askquestion("Salir", "Estas seguro que quieres salir?")
    # if(resultado == "yes"): # no
    #     root.destroy()

    #resultado = MessageBox.askokcancel("Salir", "Sobreescribir el fichero actual?")
    # resultado = MessageBox.askyesno("Salir", "Sobreescribir el fichero actual?")

    # if(resultado):
    #     root.destroy()

    # resultado = MessageBox.askretrycancel("Reintentar","No se puede conectar")
    # if resultado:
    #     root.destroy()

    # color = ColorChooser.askcolor(title="Elige un color")
    # print(color)

    # siempre dejar una coma en filetypes
    # ruta = FileDialog.askopenfilename(title="Abrir un fichero", initialdir="C:", 
    #     filetypes=(("Ficheros de texto","*.txt"),
    #                 ("Ficheros de texto avanzado","*.txt2"),
    #                 ("Todos los ficheros","*.*")))
    # print(ruta)

    fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode="w", defaultextension=".txt")
    #print(fichero) # equivale a open('ruta','w')
    if fichero is not None:
        fichero.write("Hola Mundo")
        fichero.close()


Button(root, text="Clicame", command=test).pack()

#Finalmente bucle de la aplicacion
root.mainloop()