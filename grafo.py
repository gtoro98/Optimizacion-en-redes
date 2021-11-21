import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths import weighted

def dibujarGrafo(persona, destino):

    if persona =="Javier":
        callenormal=5
        calle51=10
        calle12_13_14=7

    elif persona =="Andreina":
        callenormal=5+2
        calle51=10+2
        calle12_13_14=7+2

    else: 
        callenormal=""
        calle51=""
        calle12_13_14=""

    G=nx.Graph()

    for i in range(6):
        G.add_node(5-i,pos=(i,0))
        G.add_node(11-i,pos=(i,1))
        G.add_node(17-i,pos=(i,2))
        G.add_node(23-i,pos=(i,3))
        G.add_node(29-i,pos=(i,4))
        G.add_node(35-i,pos=(i,5))

    for j in range(5):
        G.add_edge(j,j+1,weight=callenormal)
        G.add_edge(j+6,j+6+1,weight=calle51)
        G.add_edge(j+12,j+12+1,weight=callenormal)
        G.add_edge(j+18,j+18+1,weight=callenormal)
        G.add_edge(j+24,j+24+1,weight=callenormal)
        G.add_edge(j+30,j+30+1,weight=callenormal)

        G.add_edge(0+(j*6), 6+(j*6), weight=callenormal)
        G.add_edge(1+(j*6), 7+(j*6), weight=callenormal)
        G.add_edge(2+(j*6), 8+(j*6), weight=calle12_13_14)
        G.add_edge(3+(j*6), 9+(j*6), weight=calle12_13_14)
        G.add_edge(4+(j*6), 10+(j*6), weight=calle12_13_14)
        G.add_edge(5+(j*6), 11+(j*6), weight=callenormal)


    color_map = []
    for node in G:
        if node == 28:
            color_map.append('red')
        elif node == 15: 
            color_map.append('#FF9188')
        elif node == 25 or node == 4 or node==2: 
            color_map.append('#99DC80')  
        else:
            color_map.append('#468DDA')  

    if(persona == "Ambos"):

        listaEdges = []
        color_edges=[]
        grosor_edges=[]
        for element in G.edges():
            listaEdges.append(element)
            color_edges.append('black')
            grosor_edges.append(0.5)
        
        if(destino == 25):
            caminoJavier = [19, 30, 41]
            caminoAndreina = [26, 37, 49, 51]

        elif(destino == 4):
            caminoJavier = [18, 15, 13, 11]
            caminoAndreina = [24, 22, 12]

        elif(destino == 2):
            caminoJavier = [18, 15, 13, 11, 12, 23]
            caminoAndreina = [26, 36, 33]

        for elem in caminoJavier:
            color_edges[elem] = "red"
            grosor_edges[elem] = 3

        for elem in caminoAndreina:
            color_edges[elem] = "#FF9188"
            grosor_edges[elem] = 3

        pos=nx.get_node_attributes(G,'pos')
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw(G,pos, node_color=color_map, edge_color =color_edges, width =grosor_edges, with_labels = True)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        plt.show()

    else:
        pos=nx.get_node_attributes(G,'pos')
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw(G,pos, node_color=color_map, with_labels = True)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        plt.show()

    return
