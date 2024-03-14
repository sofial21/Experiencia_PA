import random

def cachipun():
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """
    opciones = (["piedra", "papel", "tijera"])
    print("Ingresa piedra, papel o tijera")
    sigue = True
    while sigue:
        opcion = input()
        computadora = random.choice(opciones)
        print(computadora)
        if opcion != computadora:
            sigue = False
            if opcion == "tijera" and computadora == "papel":
                print("Ganaste")
            elif opcion == "tijera" and computadora == "piedra":
                print("Perdiste")
            elif opcion == "papel" and computadora == "tijera":
                print("Perdiste")
            elif opcion == "papel" and computadora == "piedra":
                print("Ganaste")
            elif opcion == "piedra" and computadora == "tijera":
                print("Perdiste")
            elif opcion == "piedra" and computadora == "papel":
                print("Ganaste")
        

