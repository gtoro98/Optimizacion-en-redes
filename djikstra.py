matriz_distancias = []

def camino_mas_corto(matriz_ad, nodoInicio):
    inicio = nodoInicio

    for i in range(len(matriz_ad)): #0-35 preparar estructura de datos auxiliar: matriz nodo distancia minima predecesor y visitado
        if i == inicio:
            matriz_distancias.append({"nodo": i, "min_distancia": 0, "predecesor": None, "visitado": False})
        else:
             matriz_distancias.append({"nodo": i, "min_distancia": 999, "predecesor": None, "visitado": False})
                
    #Imprimir la matriz auxiliar
    print("\nINICIALIZACIÓN MATRIZ AUXILIAR:")
    for x in range(len(matriz_ad)):
        print(matriz_distancias[x])

    visitar_nodo(min(matriz_distancias, key=lambda x:x['min_distancia']), matriz_ad)

    while any(nodo['visitado'] == False for nodo in matriz_distancias): #cuando todos los nodos sean visitados
        
        print("----------------------------------------------------------------------------------------------------------------")
        nodos_no_visitados = [t for t in enumerate(matriz_distancias) if t[1]['visitado'] == False] #lista con todos los nodos no visitados enumerados / todos menos el 2
        visitar_nodo(min(nodos_no_visitados, key=lambda x:x[1]['min_distancia'])[1], matriz_ad)


    print("\nMATRIZ AUXILIAR ACTUALIZADA:")
    for i in range(len(matriz_ad)):
        print(matriz_distancias[i])
        
    return

def visitar_nodo(nodo, matriz_ad):
    print("\nSe visita el nodo de menor dist. minima: ("+str(nodo['nodo'])+")  " +str(nodo))
    
    matriz_distancias[nodo['nodo']]['visitado'] = True #actualiza visitado con true
    print("Se actualiza el estado del nodo "+str(nodo['nodo'])+" a VISITADO: "+str(nodo))
    
    print("\nSe determinan sus vecinos NO visitados y se actualiza la matriz:")
    for x in range(len(matriz_ad[nodo['nodo']])): #0-35
        if matriz_ad[nodo['nodo']][x] != 0: #matriz_ad[2][x] encontramos un nodo vecino
            if matriz_distancias[x]['visitado'] == False:  # revisamos si no ha sido visitado 1 3 8 
                revisando = next(item for item in matriz_distancias if item["nodo"] == x) #revisado es la info del nodo
                print("*NODO:"+str(revisando["nodo"])+" "+str(revisando))
                
                if matriz_ad[nodo['nodo']][x] + nodo['min_distancia'] < revisando['min_distancia']: #5 + 0 < 999
                    print("-El nuevo camino al nodo ("+str(revisando['nodo'])+") es "+str(matriz_ad[nodo['nodo']][x] + nodo['min_distancia'])+", es más corto que el viejo "+str(revisando['min_distancia']))
                    matriz_distancias[revisando['nodo']]['min_distancia'] = matriz_ad[nodo['nodo']][x] + nodo['min_distancia'] # cambia 999 por 5
                    matriz_distancias[revisando['nodo']]['predecesor'] = nodo['nodo']
                    print("-Nodo:"+str(revisando["nodo"])+" "+ str(matriz_distancias[revisando['nodo']])+"\n")
                else:
                    print("-El nuevo camino al nodo ("+str(revisando['nodo'])+") es "+str(matriz_ad[nodo['nodo']][x] + nodo['min_distancia'])+", es más largo o igual que el viejo "+str(revisando['min_distancia']))
                    print("-NO se actualiza el nodo ("+str(revisando["nodo"])+")\n")
                    
    return

def recontruir_camino(matriz_distancias, nodoInicio, nodoDestino):
    Inicio = nodoInicio
    Destino = nodoDestino
    Cadena = Destino
    Este_nodo = Destino
    
    while (Este_nodo != Inicio):
        Este_nodo = matriz_distancias[Este_nodo]['predecesor']
        Cadena = str(Este_nodo) +" -> "+str(Cadena)
    
    print("\nReconstruyendo el camino más corto desde el nodo inicio ("+str(Inicio)+") hasta el nodo destino ("+str(Destino)+")")
    print("CAMINO MÁS CORTO: "+str(Cadena))
    print("DISTANCIA: "+str(matriz_distancias[Destino]['min_distancia']))
