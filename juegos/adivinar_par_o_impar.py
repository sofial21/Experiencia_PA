def adivinar_par_o_impar():
    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """
    import random
    print("Debes ingresar Par o Impar")
    solucion = input()
    numero = random.randint(1, 500)
    if numero % 2 == 0:
        respuesta = Par
    else :
        respuesta = Impar
    if respuesta == solucion :
        print("Adivinaste correctamente")
    else:
        print("Respuesta incorrecta")
    