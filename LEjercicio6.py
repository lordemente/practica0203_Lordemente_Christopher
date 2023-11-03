
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

Mrepetidas = []

for i in materias:
    calificaciones = float(input(f"Introduce tus calificacion de {i}: "))
    
    if calificaciones < 5:
        Mrepetidas.append(i)

if Mrepetidas:
    print("Usted debe repetir estás materias: ")

    for i in Mrepetidas:
        print(i)
else:
    print("!Felicidades!, usted no debe repetir ni una materia")
