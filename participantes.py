participantes = ["Ana", "Luis", "Marta", "Luis", "Pablo"]
print("Participantes llamados Luis: ", participantes.count("Luis"))
print(participantes.index("Marta"))
participantes.append("Sara")
participantes.insert(2, "Ana")
borrado = participantes.remove("Pablo")
ultimo = participantes.pop()
print(ultimo)
print(participantes)

