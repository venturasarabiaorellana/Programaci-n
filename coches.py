coches = []
print("Escribe un modelo de coche (o fin para terminar):")
modelo = input()
while modelo != "fin":
    coches.append(modelo)
    print("coches en la lista:", len(coches))
    modelo = input()
print(coches)

print("Listado de coches:")
for posicion in range(len(coches)):
    print("Posición", posicion, "->", coches[posicion])