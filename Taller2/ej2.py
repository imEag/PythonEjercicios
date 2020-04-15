""" Realizar un código que genere

a.Las cadenas complementarias de cualquier secuencia de ADN
por medio de replicación.
b.Obtener el ARNm mediante la transcripciónde la secuencia de ADN obtenida en el punto anterior. 
El usuario debe tener la opción de ingresar la secuencia de ADN deseada. """

""" Solución """

""" Se imprime una descripción del rpograma y se recoge el dato y se convierte a lowercase"""
print("Usted ingresará la cadena de ADN, ejemplo: ATCGTGGATAAT y se le mostrará la \ncadena complementaria por medio de replicación y el ARNm mediante transcripción \nEl ARNm se mostrara a partir de la cadena complementaria obtenida.")
adn = input("Ingrese la secuencia de ADN: ").lower()

""" Se crean dos listas vacias en las que se añadirá las cadenas en formato de lista"""
adnCompList = []
arnmList = []

""" se pasa la cadena de str a list """
adnList = list(adn.strip())

""" Funcion para pasar de ADN a la cadena complementaria por medio de replicacion"""
def ToAdnComp(adnl):
    """ Recorrer lista """
    for i in adnl:
        """ comparar y añadir a la nueva lista"""
        if i == 'a':
            adnCompList.append('t')
        elif i == 't':
            adnCompList.append('a')
        elif i == 'c':
            adnCompList.append('g')
        elif i == 'g':
            adnCompList.append('c')
        """ convertir de nuevo a str """
    adnCompStr = ''.join(map(str, adnCompList))
    """ retornar valor en upper case """
    return adnCompStr.upper()

""" Funcion para pasar de la cadena complemetaria a ARNm """
def ToArnm(arnml):
    """ Recorrer lista """
    for i in arnml:
        """ comparar y añadir a la nueva lista"""
        if i == 'a':
            arnmList.append('u')
        elif i == 't':
            arnmList.append('a')
        elif i == 'c':
            arnmList.append('g')
        elif i == 'g':
            arnmList.append('c')
        """ convertir de nuevo a str """
    arnmStr = ''.join(map(str, arnmList))
    """ retornar valor en upper case """
    return arnmStr.upper()

""" imprimir resultados """
print("La cadena de ADN complemetario es: " + ToAdnComp(adnList))
print("La cadena de ARNm es: " + ToArnm(adnCompList))