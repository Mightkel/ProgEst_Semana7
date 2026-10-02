from matrizbase import crear_matriz, mostrar_matriz
from escalar import multiplicar_escalar
from suma import sumar_matrices
from multiplicacion import multiplicar_matrices
from identidad import crear_identidad, mostrar_identidad


def esperar_tecla():
    import msvcrt
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()
    

def menu():
    while True:

        print("\n==============================")
        print("       PROGRAMA DE MATRICES")
        print("==============================")
        print("1. Crear y mostrar matriz")
        print("2. Multiplicar matriz por escalar")
        print("3. Sumar dos matrices")
        print("4. Multiplicar dos matrices")
        print("5. Crear matriz identidad")
        print("6. Salir")
        print("==============================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n=== CREAR MATRIZ ===")
            matriz = crear_matriz()

            print("\nMatriz:")
            mostrar_matriz(matriz)
            esperar_tecla()

        elif opcion == "2":
            print("\n=== ESCALAR ===")
            matriz = crear_matriz()

            k = int(input("Ingrese el escalar: "))

            matrizResultado = multiplicar_escalar(matriz, k)

            print("\nMatriz original:")
            mostrar_matriz(matriz)

            print(f"\nMatriz multiplicada por {k}:")
            mostrar_matriz(matrizResultado)
            esperar_tecla()

        elif opcion == "3":
            print("\n=== SUMA DE MATRICES ===")
            print("\nMatriz 1:")
            matriz1 = crear_matriz()

            print("\nMatriz 2:")
            matriz2 = crear_matriz()

            if (len(matriz1) == len(matriz2) and len(matriz1[0]) == len(matriz2[0])):

                matrizResultado = sumar_matrices(matriz1, matriz2)
                print("\nResultado:")
                mostrar_matriz(matrizResultado)

            else:
                print("\nError: las matrices deben tener")
                print("las mismas dimensiones.")
            
            esperar_tecla()

        elif opcion == "4":
            print("\n=== MULTIPLICACIÓN DE MATRICES ===")
            print("\nMatriz A:")
            matrizA = crear_matriz()

            print("\nMatriz B:")
            matrizB = crear_matriz()
            matrizResultado = multiplicar_matrices(matrizA, matrizB)

            if matrizResultado is None:
                print("\nError: no se pueden multiplicar")
                print("estas matrices.")

            else:
                print("\nResultado:")
                mostrar_matriz(matrizResultado)
            
            esperar_tecla()

        elif opcion == "5":
            print("\n=== MATRIZ IDENTIDAD ===")
            n = int(input("Digite el tamaño de la matriz: "))
            matriz = crear_identidad(n)

            print("\nMatriz identidad:")
            mostrar_identidad(matriz)
            
            esperar_tecla()
            
        elif opcion == "6":
            print("\nPrograma finalizado.")
            esperar_tecla()
            break
        
        else:
            print("\nOpción inválida.")
            esperar_tecla()


menu()