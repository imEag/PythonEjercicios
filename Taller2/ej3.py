""" Simular  una  carrera  de  2  caballos con  cadenas  de  strings  y  con  ganador  aleatorio.
 A continuación,se muestra una posible forma de mostrarlo en pantalla. """

""" solución """

""" importar modulo """
import random

""" iniciializar variables en formato de lista para cada caballo"""
c1 = ['Caballo1']
c2 = ['Caballo2']
meta = '----------------------------------------------------------------------| meta' 
""" meta de 70 guiones """

""" imprimir inicio de carrera """
print("Inicio de carrera")
print("Caballo1")
print("Caballo2")
print(meta)

""" contadores que almacenan el avance de cada caballo """
cont1 = 0
cont2 = 0
k = 1
""" ciclo para calcular el avance de la carrera """
while True:

    """ Se define de manera aleatoria cuanto avanza cada caballo (al final los pasos son menores para ver mejor el resultado) """
    if cont1 > 63 or cont2 > 63:
        nrandom1 = random.randrange(2, 5, 1)
        nrandom2 = random.randrange(2, 5, 1)
    else:
        nrandom1 = random.randrange(5, 9, 1)
        nrandom2 = random.randrange(5, 9, 1)
    """ aumentar contadores """
    cont1 += nrandom1
    cont2 += nrandom2
    """ insertar avance en la lista de cada caballo """
    i = 0
    while i < nrandom1:
        c1.insert(0, '-')
        i += 1
    j = 0
    while j < nrandom2:
        c2.insert(0, '-')
        j += 1
    """ convertir la lista de cada caballo a str """
    c1str = ''.join(map(str, c1))
    c2str = ''.join(map(str, c2))
    """imprimir avance de la carrera """
    print("MOMENTO #" + str(k))
    print(c1str)
    print(c2str)
    print(meta)
    print("\n")

    """ determinar si la carrera finalizó o no y quién ganó """
    if cont1 >= 70 and cont2 < 70:
        ganador = 'Caballo1'
        print("Ganó Caballo1")
        break
    elif cont2 >= 70 and cont1 < 70:
        ganador = 'Caballo2'
        print("Ganó Caballo2")
        break
    elif cont1 >= 70 and cont2 >= 70:
        ganador = 'Empate'
        print("Hubo empate")
        break
    k += 1
""" comentario final de la carrera """
print("Fin de la competencia, ganó " + ganador)    

