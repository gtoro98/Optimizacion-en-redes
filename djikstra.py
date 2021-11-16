matriz_distancias = []

def camino_mas_corto(matriz_ad):

    inicio = 2

    #matriz_distancias = []

    for i in range(len(matriz_ad)):
        if i == inicio:
            matriz_distancias.append({"nodo": i, "min_distancia": 0, "predecesor": None, "visitado": False})
        else:
            matriz_distancias.append({"nodo": i, "min_distancia": 999, "predecesor": None, "visitado": False})

    print(matriz_distancias)

    for x in range(len(matriz_ad)):
        print(matriz_ad[x])
    
        
    visitar_nodo(min(matriz_distancias, key=lambda x:x['min_distancia']), matriz_ad)

    #nodos_no_visitados = [t for t in enumerate(matriz_distancias) if t[1]['visitado'] == False]
    #print((min(nodos_no_visitados, key=lambda x:x[1]['min_distancia'])))
    #visitar_nodo(min(matriz_distancias, key=lambda x:x['min_distancia']), matriz_ad)
    while any(nodo['visitado'] == False for nodo in matriz_distancias):
        print("visitando nodos")
        nodos_no_visitados = [t for t in enumerate(matriz_distancias) if t[1]['visitado'] == False]
        visitar_nodo(min(nodos_no_visitados, key=lambda x:x[1]['min_distancia'])[1], matriz_ad)

    print(matriz_distancias)
    #print([t for t in enumerate(matriz_distancias)])
    print([t for t in enumerate(matriz_distancias) if t[1]['visitado'] == True])
    return

def visitar_nodo(nodo, matriz_ad):
    print(nodo)
    matriz_distancias[nodo['nodo']]['visitado'] = True

    for x in range(len(matriz_ad[nodo['nodo']])):
        if matriz_ad[nodo['nodo']][x] != 0:
            if matriz_distancias[x]['visitado'] == False:
                revisando = next(item for item in matriz_distancias if item["nodo"] == x)

                if matriz_ad[nodo['nodo']][x] + nodo['min_distancia'] < revisando['min_distancia']:

                    matriz_distancias[revisando['nodo']]['min_distancia'] = matriz_ad[nodo['nodo']][x] + nodo['min_distancia']
                    matriz_distancias[revisando['nodo']]['predecesor'] = nodo['nodo']

                    print("El camino al nodo " + str(revisando['nodo']) + " es mas corto")

    return