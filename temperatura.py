temperatura = int(input("¿Qué temperatura hace?"))
estacion = input("¿En que estación estamos (Primavera, Verano, Otoño, Invierno)?")
if estacion.title()=="Verano" and temperatura>25:
    print("Enciende el aire acondicionado")
elif estacion.title()=="Invierno" and temperatura<20:
    print("Enciende la calefacción")
else:
    print("La temperatura es óptima")
