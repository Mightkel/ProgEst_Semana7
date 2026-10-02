def multiplicar_escalar(matriz, k):
    matrizB = []
    for i in range(len(matriz)):
        matrizB.append([])
        for j in range(len(matriz[i])):
            matrizB[i].append(k * matriz[i][j])
    return matrizB