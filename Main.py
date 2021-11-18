import networkx as nx
import numpy as np
import matplotlib as plt

from matriz import *
from djikstra import *

matriz_ad_javier = crear_matriz_javier()
matriz_ad_anadreina = crear_matriz_andreina(matriz_ad_javier)

camino_mas_corto(matriz_ad_javier, 28)

G = nx.from_numpy_matrix(np.array(matriz_ad_javier))  
nx.draw(G, with_labels=True)
plt.show() 
#intento()
recontruir_camino(matriz_distancias, 28, 2) #Pacion: 25 / Darkness: 4 / Rolita:2
