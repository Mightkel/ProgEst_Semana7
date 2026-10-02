vector = ["j", "u", "a", "n"]
print(type(vector))

for letra in vector:
    print(letra)

nombre = "juan"
print("*"*13)
for letra in nombre:
    print(letra)

print("*"*13)
print(len(vector))
print(len(nombre))

def convertirMayus(texto):
    return f"{texto.upper()}"

print(convertirMayus(nombre))

for i in vector:
    print(convertirMayus(i), end="")
    

v = ""
for i in vector:
    v += i
print("\n=")
print(v.upper())

def minus(texto):
    return f"{texto.lower()}"
    
def caps(texto):
    return f"{texto.capitalize()}"

def title(texto):
    return f"{texto.title()}"

def Email(texto):
    nombre = texto.split()
    email = ''.join(palabra[:3].lower() for palabra in nombre)
    return f"{email}@uamv.edu.ni"
    
print(f"minus: {minus(nombre)}")
print(f"caps: {caps(nombre)}")
print(f"title: {title(nombre)}")
print(Email("Mikel Cruz"))