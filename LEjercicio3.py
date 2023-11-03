Materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

calificaciones = []

for i in Materias:
    Calificación = float(input(f"Introduce tu calificación de {i}: "))
    calificaciones.append(Calificación)

for j in range(len(Materias)):
    print(f"En {Materias[j]} has sacado {calificaciones[j]}")

