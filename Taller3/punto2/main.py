""" triángulo de carácteres"""
numero_maximo = int(input('Ingrese la altura que desea: '))

def generar_blanco(i):
    """ crea los espacio en blanco"""
    return (' ' * (numero_maximo - i - 1))

def generar_asteriscos(i):
    """ crea los asteriscos """
    return ('*' * (2 * i + 1))

for i in range(numero_maximo):
    """ ciclo que concatena los espacios en blanco y los asteriscos """
    print(generar_blanco(i) + generar_asteriscos(i))
