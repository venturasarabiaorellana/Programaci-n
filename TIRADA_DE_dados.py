import random

input("Presiona Enter para lanzar los dados...")

puntuacion = 0

print("Has lanzado los dados:")
for i in range(1, 11):
    dado = random.randint(1, 6)
    print("Dado", i, ":", dado)

    if dado == 6:
        puntuacion += 12
    else:
        puntuacion += dado

print("Puntuación total:", puntuacion)