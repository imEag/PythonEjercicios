""" Realice una función que genere las primeras n filas del triángulo de pascal.
El usuario debe tener la opción de ingresar el número de filas deseadas """

""" solución """
""" por: Emmanuel Arizabaleta Garcés """


""" variables de cuantas filas quiere el usuario y se hace una lista inicial para hacer el trangulo a partir de ella"""

""" """
nfilas = int(input("Ingrese el numero de filas para el trangulo de pascal: "))
triangulo = [[1], [1, 1]]
""" contador de filas """
contfila = 2

""" ciclo while para hacer cada fila """

while contfila < nfilas:
    """ lista que se borrara y llenara para hace cada fila """
    fila = []
    """ genera los primeros 2 numeros de cada fila """
    fila.append(1)
    fila.append(contfila)

    """ ------------------------------------- """
    """ este codigo se ejecuta a partir de la fila #5 
    ya que con el otro codigo anterior y siguiente de este, es suficiente para generar
    las primeras 4 filas del triagulo  """
    if contfila >= 4:
        """ ciclo para generar los numeros a partir de la siguiente operación.
        El ciclo acaba en el antepenultimo indice de la fila"""
        while len(fila) <= (contfila - 1):
            def CalcularNumero():
                """ variable para almacenar el indice del numero a calcular en su fila """
                indicenumero = len(fila)
                """ calcula el numero a partir del indice del mismo.
                Utilizo esta operacion para hallar cada número:
                NumeroNdelafilaY = NumeroN-1deLaFilaY-1+NumeroNdeLaFilaY-1"""
                nuevonumero = triangulo[contfila-1][indicenumero -
                                                    1] + triangulo[contfila-1][indicenumero]
                """ Agrego el nuevo numero a la lista """
                fila.append(nuevonumero)
            CalcularNumero()
    """ ------------------------------------- """

    """ este codigo genera los ultimos dos números de cada fila """
    if contfila - 1 == len(fila):
        fila.append(contfila)
    if contfila == len(fila):
        fila.append(1)
        """ Agrega la fila a la lista mayor """
    triangulo.append(fila)

    """ incrementa el contador de fila """
    contfila += 1

""" Función que imprime el triángulo de pascal """
def imprimirtriangulo():
    """ las condiciones son para imprimir el triangulo en caso de que el usuario haya
    pedido 0, 1, o 2 filas.
    Esto lo hago así porque el triangulo lo contruyo a partir de la fila 3 """
    if nfilas == 0:
        print("No se mostrarán filas, usted pidió 0")
    elif nfilas == 1:
        print("[1]")
    elif nfilas == 2:
        print("[1]")
        print("[1 ,1]")
    else:
        """ recorre  la lista y la imprime """
        contfilas2 = 1
        for filaprint in triangulo:
            print("Fila #{0}:  {1}".format(contfilas2, filaprint))
            contfilas2 += 1
""" Llama la función para imprimir el resultado """
imprimirtriangulo()
