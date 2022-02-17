from tkinter import *

root = Tk()

root.title("Hola Mundo")
root.resizable(1,1)
root.iconbitmap("./hola.ico")

frame = Frame(root, width=480, height=320)
#frame.pack(side="bottom", anchor="w") #left top right    e w
frame.pack(fill="both", expand=1) # x y both
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")

root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")

# Abajo del todo
root.mainloop()

# poner el archivo en tk.pyw
# forzar un modo sin terminal