# 10) En un curso de computación, que consta de 24 alumnos, 
# deberán armar un algoritmo que informe por pantalla el apellido y nombre junto a la nota de examen de cada alumno.

num_alumnos = 24
alumnos = []
alumnos_numeros = [i for i in range(num_alumnos)]

i = 0
while i < num_alumnos:
    print(f"Alumno {alumnos_numeros[i] + 1}:")
    apellido = input("Ingrese el apellido: ")
    nombre = input("Ingrese el nombre: ")
    nota = float(input("Ingrese la nota de examen: "))
    alumnos.append((apellido, nombre, nota))
    i += 1
    print()

print("Información de los alumnos:")
for alumno in alumnos:
    print(f"{alumno[0]} {alumno[1]} - Nota de examen: {alumno[2]}")
