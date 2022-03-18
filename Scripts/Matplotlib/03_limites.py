# %%
import numpy as np
import matplotlib.pyplot as plt

ahorros = np.random.randint(100, size=[6])
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
mapeado = range(len(meses))

plt.plot(ahorros) #añadimos el grafico
plt.xticks(mapeado, meses) #mapeados los valores horizontales
plt.show() #finalmente lo mostramos

# %%
# Limites verticales
plt.plot(ahorros)
plt.xticks(mapeado, meses)
plt.ylim(0,100)
plt.show()
# %%
# Limites horizontales
plt.plot(ahorros)
plt.xticks(mapeado, meses)
plt.xlim(2,4)
plt.ylim(0,100)
plt.show()
# %%
