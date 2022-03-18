# %%
import numpy as np
import matplotlib.pyplot as plt

ahorros = np.random.randint(100, size=[6])
meses = ['Enero', 'Febrero','Marzo','Abril','Mayo','Junio']
mapeado = range(len(meses))

plt.plot(ahorros) #añadimos el grafico
plt.xticks(mapeado, meses) #mapeados los valores horizontales
plt.show() #finalmente lo mostramos
# %%
x = np.arange(6)
y = np.random.randint(20, size=[6])
plt.plot(x,y)
plt.show()
# %%
plt.plot(y,x)
plt.show()
# %%
x = np.random.randint(20, size=[6])
y = np.random.randint(20, size=[6])

plt.plot(x,y)
plt.show()
# %%
