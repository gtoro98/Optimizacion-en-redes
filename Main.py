import networkx as nx 
import numpy as np
import matplotlib.pyplot as plt 

from matriz import *
from djikstra import *

matriz_ad = crear_matriz()

camino_mas_corto(matriz_ad)


#G = nx.from_numpy_matrix(np.array(matriz_ad))  
#nx.draw(G, with_labels=True)
#plt.show() 
#intento()