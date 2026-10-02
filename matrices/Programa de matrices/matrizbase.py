def crear_matriz():
    matriz = []

    filas = int(input("Filas: "))
    columnas = int(input("Columnas: "))

    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            num = int(input(f"Ingrese un número para [{i}][{j}]: "))
            matriz[i].append(num)
    return matriz


def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)