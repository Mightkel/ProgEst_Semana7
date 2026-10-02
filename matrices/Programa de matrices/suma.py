def sumar_matrices(matriz1, matriz2):
    matrizSuma = []
    for i in range(len(matriz1)):
        matrizSuma.append([])
        for j in range(len(matriz1[i])):
            matrizSuma[i].append(matriz1[i][j] + matriz2[i][j])
    return matrizSuma