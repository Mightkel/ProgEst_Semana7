#Suma de matrices
import os
'''Leer 2 matrices 3 x 3 y sumar en una matriz'''
print("Matriz 1:")
matriz1 = []

for f in range(3):
    matriz1.append([])
    for j in range(3):
        num = int(input(f"Ingrese un numero para el elemento {f}, {j}: "))
        matriz1[f].append(num)
        
for f in matriz1:
    print(f)
    
print("Matriz 2:")
matriz2 = []

for f in range(3):
    matriz2.append([])
    for j in range(3):
        num = int(input(f"Ingrese un numero para el elemento {f}, {j}: "))
        matriz2[f].append(num)
        
for f in matriz2:
    print(f)
    
os.system('cls')
print("Suma de matrices:")     
    
matrizSuma = []    

for f in range(len(matriz1)):
    matrizSuma.append([])
    for j in range(len(matriz1)):
        matrizSuma[f].append(matriz1[f][j] + matriz2[f][j])
        
for f in matrizSuma:
    print(f)