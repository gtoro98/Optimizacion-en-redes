def llenar_matriz():

    return

def bogota():
    nodos = 36

    matriz_ad = [ [0 for i in range(nodos)]] * nodos

    for y in range(len(matriz_adj)):
 
        abajo = y + 6
        derecha = y + 1
        if(y >= 0):
            izquierda = y -1
            matriz_ad[y][izquierda] = 5
        #if()
        if (y >= 6):
            arriba = y - 6
            matriz_ad[y][arriba] = 5
        matriz_ad[y][abajo] = 5
        matriz_ad[y][derecha] = 5
        

    print("matriz " + str())