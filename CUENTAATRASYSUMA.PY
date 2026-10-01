numero=int(input("Ingrese un numero: "))
suma=0
for i in range(numero, -1, -1):
    print(i)

suma=0
for i in range(0, numero + 1):
    suma += i
print("La suma es:", suma)