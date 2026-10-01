mayor = int(input("Ingrese el primer número: "))
for i in range(2, 6):
    numero = int(input("Ingrese el siguiente número: "))
    if numero > mayor:
        mayor = numero
print("El mayor número ingresado es:", mayor)