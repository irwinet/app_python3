# %%
#Grafico Lineal
from cProfile import label
import random
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,11)
y = np.random.randint(10, size=10)

plt.plot(x,y)
plt.show()
# %%
# Grafico de lineas verticales
plt.stem(x,y)
plt.show()
# %%
# Grafico de series comparadas
for t in range(1,11)[::-1]:
    plt.fill_between(
        range(1,11),
        [t * n for n in range(1,11)],
        label=f"Tabla del {t}"
    )
plt.title("Tablas de multiplicar")
plt.legend(loc='upper left')
plt.show()
# %%
#Grafico circular o de pastel
turistas = [86.9, 81.8, 75.9, 60.7, 58.2, 39.3, 37.7, 37.6, 37.5, 35.4]
paises = ['Francia','España','EEUU','China','Italia','Mexico','Reino Unico','Turquia','Alemania','Tailandia']
explode = [0,0.2,0,0,0,0.4,0,0,0,0]
plt.pie(turistas, labels=paises, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("TOP 10 DESTINOS TURISTICOS EN 2017")
plt.show()

# %%
# Grafico de cajas y bigotes
jap = np.random.uniform(166,176,100)
ale = np.random.uniform(175,185,100)
arg = np.random.uniform(170,180,100)

plt.boxplot([jap,ale,arg])
plt.xticks([1,2,3],['Japon','Alemania','Argentina'])
plt.ylabel('Estaturas (cm)')
plt.show()
# %%
#Grafico histograma
alturas = np.random.uniform(170,180,1000)
plt.hist(alturas,bins=10,edgecolor='black')
plt.title("Distribucion de 1000 alturas")
plt.xlabel("Altura media (cm)")
plt.ylabel("Muestras")
plt.show()
# %%
#Grafico Histograma gaussiano
numeros = np.random.normal(size=1000)
plt.hist(numeros, bins=10, edgecolor='black')
plt.title("Histograma Gaussiano")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()
# %%
#Grafico de barras
fechas = ['19/08/2019','20/08/2019','21/08/2021','22/08/2019','23/08/2019']
primas = [79,80,79,80,82]
plt.bar(range(5), primas, edgecolor='black')
plt.xticks(range(5), fechas, rotation=60)
plt.title("PRIMA DE RIESGO EN ESPAÑA")
plt.ylim(min(primas)-1, max(primas)+1)
plt.show()
# %%
#Grafico de horizontal
fechas = ['19/08/2019','20/08/2019','21/08/2021','22/08/2019','23/08/2019']
primas = [79,80,79,80,82]
plt.barh(range(5), primas, edgecolor='black')
plt.yticks(range(5), fechas, rotation=60)
plt.title("PRIMA DE RIESGO EN ESPAÑA")
plt.xlim(min(primas)-1, max(primas)+1)
plt.show()
# %%
#Grafico de escaleras
x = np.arange(1,11)
y = np.random.randint(10, size=10)

plt.step(x,y)
plt.show()
# %%
