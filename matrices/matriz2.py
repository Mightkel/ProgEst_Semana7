matrizC = []

filas = int(input("Filas: "))
columnas = int(input("Columnas: "))


for f in range(filas):
    matrizC.append([])
    for j in range(columnas):
        num = int(input("Ingrese un numero: "))
        matrizC[f].append(num)
        
for f in matrizC:
    print(f)