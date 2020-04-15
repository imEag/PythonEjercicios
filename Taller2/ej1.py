"""Se tiene el siguiente código
L = [9, 8, -9, -6, -8, 7, 0, 3, -8] 
def filtrar(Lista, P = []):
    for i in Lista:
        if i>0:
            P+=[i,]
    return(P)

print(filtrar(L))

a. Describa con sus propias palabras el paso a paso del funcionamiento de dicho código.
b. Según lo visto en clase, optimice el código (use funciones propias de Python, cree
funciones, use diccionarios y/o listas... Lo que considere necesario)."""

""" Solución """
""" por: Emmanuel Arizabaleta Garcés """

""" a) """ 
""" Crea lista de numeros que contiene enteros. """
L = [9, 8, -9, -6, -8, 7, 0, 3, -8] 

""" crea función llamada filtrar que recibe dos parametros, una que es la lista a filtrar
y otro que es opcional que es un alista a llenar"""
def filtrar(Lista, P = []):
    """ crea un array para recorrer la lista que se le pasó como parámetro"""
    for i in Lista:
        """ Verifica si el valor es mayor que cero (es positivo) y si lo es lo aññade a la nueva lista"""
        if i>0:   
            P+=[i,]
    """ retorna la nueva lista """
    return(P)

""" llama la funcion y le pasa la lista L como parámetro e imprime lo que retorna.
"""
print(filtrar(L))

""" b) Código optimizado """

""" Crea la lista """
L = [9, 8, -9, -6, -8, 7, 0, 3, -8] 

""" Utiliza filter, que es una inbuilt function de python. Dentro le pasa dos parametros, la condición que se debe cumplir
y la lista que se va a filtrar.
El primer parametro se le pasa con una lambda function que de nuevo, se le pasa un parámetro
que va a ser el valor de cada indice a medida que se recorrar la lista, y luego de los puntos va la condicion a cumplir.
Por ultimo se le asigna a una variable llamada "filtrado" """
filtrado = filter(lambda i: i > 0, L)
""" Se convierte en lista y se le asigna a D"""
D = list(filtrado)
""" se imprime D """
print(D)