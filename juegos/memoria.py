import random
def memoria():
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    secuencia = []
    for i in range(10):
        numero = random.randint(0,101)
        secuencia = secuencia.append(numero) 
        print(numero)
    
    for i in secuencia:
        ingresar = input('Ingresa un número: ')
        if ingresar != i:
            return("Fallaste")
    
    return("Ganaste")
            