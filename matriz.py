

def crear_matriz():
    nodos = 36

    #inicializamos la matriz
    matriz_ad = []
    for i in range(nodos):          #para las filas
        a = []
        for j in range(nodos):      #para las columnas
            a.append(0)
        matriz_ad.append(a)

    #ponemos los pesos de los caminos
    for y in range(len(matriz_ad)):
        
        if y >= 1:                                  #para evitar negativos en el primer nodo
            nodo_izquierda = y - 1     
            if(y%6 != 0):
                if int(y/6) == 1:
                    matriz_ad[y][nodo_izquierda] = 10    #calle 51
                else:
                    matriz_ad[y][nodo_izquierda] = 5    #se termina la ciudad a la izquierda("este")

        if y <= 34:
            nodo_derecha = y + 1                    #para evitar pasarse de la cantidad de nodos en el ultimo nodo
            if((y - 5)%6 != 0):
                if int(y/6) == 1:
                    matriz_ad[y][nodo_derecha] = 10      #calle 51
                else:
                    matriz_ad[y][nodo_derecha] = 5      #se termina la ciudad a la derecha("oeste")

        if(y >= 6):
            nodo_arriba = y - 6                    #para evitar negativos en la primera fila
            if(y%6 == 2 or y%6 == 3 or y%6 == 4):
                matriz_ad[y][nodo_arriba] = 7
            else:
                matriz_ad[y][nodo_arriba] = 5          #se termina la ciudad hacia arriba("sur")

        if(y <= 29):
            nodo_abajo = y + 6                     #para evitar negativos en la ultima fila
            if(y%6 == 2 or y%6 == 3 or y%6 == 4):
                matriz_ad[y][nodo_abajo] = 7
            else:
                matriz_ad[y][nodo_abajo] = 5           #se termina la ciudad hacia abajo("norte")
    
    return matriz_ad

def intento():
    
    matrix = []
    for i in range(36):          # A for loop for row entries
        a = []
        for j in range(36):      # A for loop for column entries
            a.append(0)
        matrix.append(a)
    matrix[0][1] = 5
    print(matrix[0][1])
    print(matrix)