matriz = [
    [1, 2],
    [3, 4]
]

for f in matriz:
    print(f)
    

#Escalar
k = 5

matrizB = []
for f in range(len(matriz)):
    matrizB.append([])
    for j in range(len(matriz)):
        matrizB[f].append(k * matriz[f][j])
        
print("="*13)
print("Escalar", k)        
        
for f in matrizB:
    print(f)
    
