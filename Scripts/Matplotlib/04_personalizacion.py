# %%
from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

ahorros = np.random.randint(100, size=[6])
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
mapeado = range(len(meses))

#Mapeado de los valores horizontales
plt.xticks(mapeado,meses)
plt.title("Ahorros del primer trimestre")
plt.xlabel("Meses")
plt.ylabel("Cantidad en $")
plt.ylim(0,100)
plt.plot(ahorros)
plt.show()
# %%
# Mostramos una leyenda
plt.xticks(mapeado, meses)
plt.title("Ahorros del primer semestre")
plt.xlabel("Meses")
plt.ylabel("Cantidad en $")
plt.legend(loc=4)
plt.ylim(0,100)
plt.plot(ahorros)
plt.show()
# %%
# Mostramos una leyenda con un texto
plt.plot(ahorros, label="Evolucion")
plt.xticks(mapeado, meses)
#plt.xlim(2,4)
plt.title("Ahorros del primer semestre")
plt.xlabel("Meses")
plt.ylabel("Cantidad en $")
plt.legend(loc=4)
plt.show()
# %%
# Mostramos los ahorros de tres personas diferentes
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
mapeado = range(len(meses))

plt.plot(np.random.randint(100, size=[6]), label="Pedro")
plt.plot(np.random.randint(100, size=[6]), label="Irwin")
plt.plot(np.random.randint(100, size=[6]), label="Ana")

plt.xticks(mapeado, meses)
plt.title("Ahorros del primer semestre")
plt.xlabel("Meses")
plt.ylabel("Cantidad en $")
plt.legend()
plt.show()
# %%
for t in range(1,11):
    plt.plot(
        range(1,11),
        [t * n for n in range(1,11)],
        label=f"Tabla del {t}"
    )
plt.title('Tabla')
plt.xlabel('Numero')
plt.ylabel('Resultado')
plt.legend()
plt.show()
# %%
