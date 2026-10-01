contrasena = "7777"
intentos = 4
acertado = False

while intentos > 0 and not acertado:
    clave = input("Ingresa la contraseña: ")
    if clave == contrasena:
        acertado = True
    else:
        intentos -= 1
        if intentos > 0:
            print("Contraseña incorrecta. Te quedan", intentos, "intentos")

if acertado:
    print("BIENVENIDO AL SISTEMA")
else:
    print("ACCESO DENEGADO VUELVE A INTENTARLO EN 5 MINUTOS")

