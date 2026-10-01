bebidas = [["Coca Cola", 15, 1.50],
    ["Fanta naranja", 10, 1.40],
    ["Agua", 20, 1.00],
    ["Nestea", 8, 1.60],
    ["Aquarius", 12, 1.70]]

ventas = []
while opcion != 4:
    print("Bienvenido a la máquina expendedora, elige una opción:")
    print("1. Comprar bebida")
    print("2. Listar bebidas disponibles")
    print("3. Mostrar ventas realizadas")
    print("4. Salir del programa")
    opcion = int(input("Opción: "))

    if opcion == 1:
        print("Bebidas disponibles:")
        for i, bebida in enumerate(bebidas):
            print(f"{i + 1}. {bebida[0]} - Cantidad: {bebida[1]} - Precio: {bebida[2]}")
        seleccion = int(input("Selecciona el número de la bebida que deseas comprar: ")) - 1
        if seleccion >= 0 and seleccion < len(bebidas):
            cantidad = int(input(f"¿Cuántas unidades de {bebidas[seleccion][0]} deseas comprar? "))
            if cantidad <= bebidas[seleccion][1]:
                total = cantidad * bebidas[seleccion][2]
                print(f"Total a pagar: {total}€")
                confirmacion = input("¿Deseas confirmar la compra? (s/n): ")
                if confirmacion.lower() == 's':
                    bebidas[seleccion][1] -= cantidad
                    ventas.append([bebidas[seleccion][0], cantidad, total])
                    print("Compra realizada con éxito.")
                else:
                    print("Compra cancelada.")
            else:
                print("No hay suficiente stock disponible.")
        else:
            print("Selección no válida.")

    elif opcion == 2:
        print("Listado de bebidas disponibles:")
        for bebida in bebidas:
            print(f"Nombre: {bebida[0]}, Cantidad: {bebida[1]}, Precio: {bebida[2]}")

    elif opcion == 3:
        if ventas:
            print("Ventas realizadas:")
            for venta in ventas:
                print(f"Bebida: {venta[0]}, Cantidad: {venta[1]}, Total: {venta[2]}€")
        else:
            print("No se han realizado ventas aún.")

    elif opcion == 4:
        print("Saliendo del programa...")
