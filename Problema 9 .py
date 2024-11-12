# 9) Ingresar un valor por teclado y determinar 
# si es positivo, negativo o igual a cero, 
# imprimir una leyenda en cada caso


numero = float(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
