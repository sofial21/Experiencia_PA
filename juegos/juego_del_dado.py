def juego_del_dado():
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    import random
    puntuacion_usuario = 0
    puntuacion_computador = 0
    juego = True 
    while juego: 
        print("Debes apretar enter para lanzar el dado")
        inicio = input() # representa que aprete enter
        lanzamiento = random.randint(1,7)
        puntuacion_usuario += lanzamiento
        lanzamiento_computador = random.randint(1,7)
        puntuacion_computador += lanzamiento_computador
        print(lanzamiento)
        print(lanzamiento_computador)
        print("Juego continua ... ")
        if lanzamiento == 30:
            juego = False
        if lanzamiento_computador == 30:
            juego = False
    