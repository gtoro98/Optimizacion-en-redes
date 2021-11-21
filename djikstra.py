def crear_matriz_javier():
    nodos = 36
    
    #inicializamos la matriz
    matriz_ad = []
    for i in range(nodos):          #para las filas 0-35
        a = []
        for j in range(nodos):      #para las columnas 0-35
            a.append(0)
        matriz_ad.append(a)

    #ponemos los pesos de los caminos
    for y in range(len(matriz_ad)): #0-35

        if y >= 1:  
            nodo_izquierda = y - 1 #1-1=0 / 7-1=6
            if(y%6 != 0):
                if int(y/6) == 1: #entran 7,8,9,10,11
                    matriz_ad[y][nodo_izquierda] = 10    #calle 51 matriz_ad[7][6] [8][7] [9][8] [10][9] [11][10]
                else:
                    matriz_ad[y][nodo_izquierda] = 5   #se termina la ciudad a la izquierda("este") [1][0] [2][1] [3][2] 

        if y <= 34: #entra de 0-34
            nodo_derecha = y + 1                    #para evitar pasarse de la cantidad de nodos en el ultimo nodo
            if((y - 5)%6 != 0): # 5 11 17 23 29 no entran
                if int(y/6) == 1: #entra 6,7,8,9,10
                    matriz_ad[y][nodo_derecha] = 10     #[6][7] [7][8] [8][9] [9][10] [10][11]         #calle 51 
                else:
                    matriz_ad[y][nodo_derecha] = 5      #se termina la ciudad a la derecha("oeste")

        if(y >= 6): #6-35
            nodo_arriba = y - 6 #6-6=0 7-6=1 8-6=2
            if(y%6 == 2 or y%6 == 3 or y%6 == 4): #entra 8 9 10 14 15 16 20 21 22 26 27 28 32 33 34
                matriz_ad[y][nodo_arriba] = 7 
            else:
                matriz_ad[y][nodo_arriba] = 5          #se termina la ciudad hacia arriba("sur")

        if(y <= 29):# 0-29
            nodo_abajo = y + 6                     #para evitar negativos en la ultima fila
            if(y%6 == 2 or y%6 == 3 or y%6 == 4): # entra 2 3 4 8 9 10 14 15 16 20 21 22 26 27 28
                matriz_ad[y][nodo_abajo] = 7
            else:
                matriz_ad[y][nodo_abajo] = 5           #se termina la ciudad hacia abajo("norte")
    
    print("MATRIZ DE ADYACENCIA JAVIER:")
    print("    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35]")
    for i in range(len(matriz_ad)):
        if i<10:
            print(" "+str(i)+" "+str(matriz_ad[i]))
        else:
            print(str(i)+" "+str(matriz_ad[i]))
          
    return matriz_ad


def crear_matriz_andreina(matriz_ad_javier):
    nodos = 36
    
    #inicializamos la matriz
    matriz_ad = []
    for i in range(nodos):          #para las filas 0-35
        a = []
        for j in range(nodos):      #para las columnas 0-35
            a.append(0)
        matriz_ad.append(a)
    
    for i in range(len(matriz_ad)):
        for j in range(len(matriz_ad)):
            if (matriz_ad_javier[i][j]!=0):
                matriz_ad[i][j] = matriz_ad_javier[i][j]+2
            
    print("\nMATRIZ DE ADYACENCIA ANDREINA:")
    print("    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35]")
    for i in range(len(matriz_ad)):
        if i<10:
            print(" "+str(i)+" "+str(matriz_ad[i]))
        else:
            print(str(i)+" "+str(matriz_ad[i]))
    
    return matriz_ad
