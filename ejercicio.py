nota = input("introduce la nota: ")
nota = int(nota)
if nota < 6:
    if nota <5:
           if nota <3:
               print("muy deficiente")
           else:
               print("insuficiente")
    else:
        print("suficiente")
else:
    if nota < 7:
        print("Bien")
    else: 
        if nota <9:
            print("notable")
        else:
            print("sobresaliente")
    
