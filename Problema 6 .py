# 6) Dados 3 números determinar el mayor e informar por pantalla el resultado

a = int(input("Ingresar numero"))
b = int(input("Ingresar numero"))
c = int(input("Ingresar numero"))

if a >= b and a >= c :
    mayor = a
elif b >= a and b>= c :
    mayor = b
else:
    mayor = c

print ("El numero mayor es:", mayor)
