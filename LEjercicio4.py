num_g = []

contador = 0

while contador <5:
    try:
        numeros = int(input("ingrese números: "))
        if numeros < 1 or numeros > 50:
            print("Ingrese números mayores que 1 y menores a 50")
        elif numeros in num_g:
            print("Ingrese números diferentes")

        else:
            num_g.append(numeros)
            contador += 1

    except ValueError:
        print("Ingreses números enteros, no escriba strings or floats")

num_g.sort()
print("Números guardados de menor a mayor")

# num_g.reverse()


for numeros in num_g:
    print(f"Tus números guardados son: {numeros}")

            
