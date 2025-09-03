pregunta = str(input("¿Trabajas desde casa? (si/no): "))

if pregunta == "si":
    print("Bien")

if pregunta == "no":
    print("Tiempo de traslado")

    tiempo = input("¿Cuánto tiempo dura tu trayecto al trabajo: introduce la cantidad de minutos en número: " )
    if tiempo == "0":
        print("Introduce otro número diferente de cero")
    else :
        print("Recuerda tener todo listo con 15 min de anticipación. Prevee retrasos o tráfico")
