'''
Dada una matriz de identidad nxn
mostrar en color azul solo la diagonal de 1
'''
from colorama import Fore, Style
n = int(input("Digite el tamaño de la matriz: "))
matriz = []
#indentificacion

for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)
            
for i in range(n):
    for j in range(n):
        if i == j:
            print(Fore.BLUE + str(matriz[i][j]) + Style.RESET_ALL, end=" ")
        else:
            print(matriz[i][j], end=" ")
    print()