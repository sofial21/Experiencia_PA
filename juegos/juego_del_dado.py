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
        print(f'Te salió un {lanzamiento}')
        puntuacion_usuario += lanzamiento
        lanzamiento_computador = random.randint(1,7)
        print(f'El computador lanzó un {lanzamiento_computador}')
        puntuacion_computador += lanzamiento_computador
        print("Puntaje jugador: " + str(puntuacion_usuario))
        print("Puntaje computador: " + str(puntuacion_computador))
        print("Juego continua ... ")

        if puntuacion_usuario >= 30 and puntuacion_computador >= 30:
            print("Puntaje jugador" + str(lanzamiento))
            print("Puntaje computador" + str(lanzamiento_computador))            
            juego = False
            print("Juego terminado ... ")
            print('Empate!')
        
        else:
            if puntuacion_usuario >= 30:
                print("Puntaje jugador" + str(lanzamiento))
                print("Puntaje computador" + str(lanzamiento_computador))            
                juego = False
                print("Juego terminado ... ")
                print('Ganaste!')

            if puntuacion_computador >= 30:
                print("Puntaje jugador" + str(lanzamiento))
                print("Puntaje computador" + str(lanzamiento_computador))
                juego = False
                print("Juego terminado ... ")
                print('Perdiste :(')
