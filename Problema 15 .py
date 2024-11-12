# 15) Ingresar 100 valores por teclado y determinar cuántas veces el valor ingresado es: 
# a) Mayor a 0 y menor a 10
# b) Esta comprendido entre 10 y 100 ambos inclusive.
# c) Es mayor a 100
# d) Es negativo
# e) Es igual a Olmprimir los resultados.

cont_entre_0_y_10 = 0
cont_entre_10_y_100 = 0
cont_mayor_a_100 = 0
cont_negativos = 0
cont_igual_a_0 = 0

for i in range(10):
    valor = float(input(f"Ingrese el valor {i + 1}: "))
    
    if 0 < valor < 10:
        cont_entre_0_y_10 += 1
    elif 10 <= valor <= 100:
        cont_entre_10_y_100 += 1
    elif valor > 100:
        cont_mayor_a_100 += 1
    elif valor < 0:
        cont_negativos += 1
    elif valor == 0:
        cont_igual_a_0 += 1

print("Valores mayores a 0 y menores a 10:", cont_entre_0_y_10)
print("Valores entre 10 y 100 (inclusive):",cont_entre_10_y_100)
print("Valores mayores a 100:", cont_mayor_a_100)
print("Valores negativos:", cont_negativos)
print("Valores iguales a 0:", cont_igual_a_0)


