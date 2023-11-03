
palabra = input("Ingresa una palabra: ")

# lista de vocales
vocales = ['a', 'e', 'i', 'o', 'u']

# Comprensión de lista
conteos = [palabra.lower().count(j) for j in vocales]

for i, j in enumerate(vocales):
    print(f"Número de '{j}' en la palabra: {conteos[i]}")




