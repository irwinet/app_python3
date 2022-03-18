# %%
from cProfile import label
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

# La figura crea un espacio donde dibujar el grafico
fig = plt.figure(figsize=(3,4), dpi=100)

# Necesitamos definir una relacion de tamaños para el rectangulo del dibujo (l,b,w,h)
rect = (0,0,1,1)

#Añadimos los limites para crear un objeto
axes = fig.add_axes(rect)

#A partir de este objeto podemos crear nuestro grafico
axes.plot(np.random.randint(100,size=[6]), label="Irwin", color="green")
axes.plot(np.random.randint(100,size=[6]), label="Pedro", color="red")
axes.plot(np.random.randint(100,size=[6]), label="Ana", color="cyan")

axes.set_ylim(0,100)
axes.set_xlabel("Meses")
axes.set_ylabel("Cantidad en $")
axes.set_title("Ahorros del primer semestre")

# La parte de mapear los nombres cambia un poco y requiere usar dos metodos
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
mapeado = range(len(meses))
axes.set_xticks(mapeado)
axes.set_xticklabels(meses)

fig.show()
# %%
