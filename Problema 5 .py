# 5) Realizar un algoritmo para determinar el sueldo de un empleado, 
# teniendo en cuenta que si trabajo menos de 5 años 
# la antigüedad será del 30% y si trabajo igual o más de 5 años del 50%. 
# (Sueldoacobrar=(sueldo+sueldo)*%)

yearsworking = int(input("Ingrese yearsworking"))
salario = int(input("Ingrese salario"))

porcentaje = 0
 if yearsworking <5:
    porcentaje = 0.30
 elif yearsworking >=5:
    porcentaje = 0.50
    
salario_a_cobrar = (salario + (salario * porcentaje))
print("El salario a cobrar es", salario_a_cobrar)
