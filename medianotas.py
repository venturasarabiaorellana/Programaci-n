nota=int(input("Ingrese la nota: "))
print("la nota ingresada es:", nota)

total = 10
acumulador=0
aprobados=0
suma_notas=0


for i in range(10):
    nota=int(input("Ingrese la nota: "))
    if nota >= 5:
        print("aprobado")
        aprobados += 1
        suma_notas += nota
    else:
        print("suspendido")

media = suma_notas / 10

print("Número de aprobados:", aprobados)
print("Suma de notas:", suma_notas)
print("Nota media:", media)