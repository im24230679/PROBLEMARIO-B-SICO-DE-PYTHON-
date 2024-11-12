# 4) Calcular la nota del trimestre a partir de tres notas, luego determinar si aprobó o debe recuperar e informarlo.

nota1 = int(input("Ingresa nota1"))
nota2 = int(input("Ingresar nota2"))
nota3 = int(input("Ingresa nota3"))

promedio = (nota1 + nota2 + nota3)/3

if promedio >= 70:
    print ("Aprobo")
elif promedio <70:
    print ("No aprobo, debe recuperar")
