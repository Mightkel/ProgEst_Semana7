def multiplicar_matrices(matrizA, matrizB):
    filasA = len(matrizA)
    columnasA = len(matrizA[0])
    filasB = len(matrizB)
    columnasB = len(matrizB[0])

    if columnasA != filasB:
        return None

    matrizC = []
    for i in range(filasA):
        matrizC.append([])
        for j in range(columnasB):
            suma = 0
            for k in range(columnasA):
                suma += matrizA[i][k] * matrizB[k][j]
            matrizC[i].append(suma)
    return matrizC