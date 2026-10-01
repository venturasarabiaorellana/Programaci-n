edad = int (input("Introduce tu edad: "))
dia = input("Introduce el día (L, M, X, J, V, S, D): ")

if dia=="S" or dia=="D":
    precio=20
else:
    precio=15

if edad < 18:
    porcentaje = 30
    descuento = (precio * porcentaje) / 100
    precio = precio - descuento
    print("Precio final",precio)
else:
    descuento=0
    precio_final=precio
    print("precio final:",precio)


