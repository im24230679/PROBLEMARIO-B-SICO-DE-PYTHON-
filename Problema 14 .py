# 14) Ingresar 10 valores numéricos por teclado y calcular la suma, el promedio e imprimir la suma, 
# el promedio agregando una leyenda en cada caso.

suma = 0
contador = 0

while contador < 10:
    valor = float(input("Ingresa un valor: "))
    suma += valor
    contador += 1

promedio = suma / 10

print("La suma de los 10 valores es:", suma)
print("El promedio de los 10 valores es:", promedio)

