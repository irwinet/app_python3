# %%
# Dibujos con subgraficos
from cProfile import label
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

plt.subplot(1,3,1) # Tabla 1x3 y dibujamos en la celda 1
plt.plot(np.random.randint(100, size=[6]), label="Irwin", color="green")
plt.ylim(0,100)
plt.legend()

plt.subplot(1,3,2) # Tabla 1x3 y dibujamos en la celda 2
plt.plot(np.random.randint(100, size=[6]), label="Ana", color="red")
plt.ylim(0,100)
plt.legend()

plt.subplot(1,3,3) # Tabla 1x3 y dibujamos en la celda 3
plt.plot(np.random.randint(100, size=[6]), label="Marta", color="cyan")
plt.ylim(0,100)
plt.legend()

plt.show()
# %%
#Dibujos con subgraficos
for i in range(9):
    plt.subplot(3,3,i+1)
    plt.plot(np.random.randint(100,size=[6]))
    plt.ylim(0,100)
plt.show()
# %%
