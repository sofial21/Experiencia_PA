import random

def adivinar_numero():
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    numero = random.randint(1, 11)
    entrada = int(input('Elija un número entre 1 y 10'))
    if entrada == numero:
        print('Felicitaciones! Adivinaste')
    else:
        print('No has adivinado :(')