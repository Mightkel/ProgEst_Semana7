'''
Leer una cadena de texto y buscar una palabra o texto
'''

def buscar(cadena, valor):
    posicion = cadena.find(valor)
    if posicion >= 0:
        return "Se encontro el valor buscado."
    else:
        return "No se encuentra el valor que busca."
    
def saberSiContiene(cadena, valor):
    return valor in cadena

cadena =input("Dime una frase: ")
valor =input("Dime el dato a buscar: ")

print(buscar(cadena, valor))
