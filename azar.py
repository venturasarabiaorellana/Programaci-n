import random

# Generamos un número aleatorio entre 1 y 10
numero = random.randint(1, 10)

intentos = 0
max_intentos = 5
acertado = False

while intentos < max_intentos and not acertado:

    usuario = int(input("Dame un número del 1 al 10: "))

    if usuario < 1 or usuario > 10:
        print("El número debe estar entre 1 y 10.")
        continue

    intentos += 1

    if usuario == numero:
        print("¡Has acertado!")
        acertado = True

    elif usuario < numero:
        print("El número es mayor")

    else:
        print("El número es menor")

    if not acertado:
        print("Te quedan", max_intentos - intentos, "intentos")

if not acertado:
    print("Te has quedado sin intentos.")
    print("El número era", numero)
