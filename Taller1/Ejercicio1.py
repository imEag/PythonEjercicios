""" Sean f y g dos números enteros de tres dígitos cada uno.
 1. Realice un algoritmo que permita invertir los valores de los dígitos de g e intercambiar
 el primer y segundo dígito de f, de tal forma que se muestre el resultado del intercambio
 de los dígitos.
 2. Además se debe mostrar el resultado de la suma y la multiplicación
 entre los números si f es mayor que g y si g es mayor que f se debe
 mostrar la resta y la división de estos """

""" Por: Emmanuel Arizabaleta Garcés """

""" BUG CUANDO SE PONE 0 AL INICIO  """

print("Debe ingresar dos numeros enteros, cada uno de tres dígitos")
i = True
k = True
""" VALIDACIÓN PARA QUE SEA ENTERO (sin detener el programa) """
while i == True:
    g = input("--- Ingrese el primer número (Debe ser de tres dígitos): ")
    try:
        value = int(g)
        gverficacion = list(str(g))
        """ Validación que sea de 3 dígitos """
        if len(gverficacion) == 3:
            i = False
        elif len(gverficacion) != 3:
            print("No ingresaste un numero de tres dígitos")
    except ValueError:
        value = 0
        print("No ingresaste un entero")

while k == True:
    f = input("--- Ingrese el segundo número (Debe ser de tres dígitos): ")
    try:
        value = int(f)
        fverficacion = list(str(f))
        """ Validación que sea de 3 dígitos """
        if len(fverficacion) == 3:
            k = False
        elif len(fverficacion) != 3:
            print("No ingresaste un numero de tres dígitos")
    except ValueError:
        value = 0
        print("No ingresaste un entero")
""" CONVERTIR LOS INPUTS A ENTEROS """
f = int(f)
g = int(g)

""" CONVERTIR G A LISTA Y APLICAR LAS OPERACIONES """
g = list(str(g))

g1 = list(g)
g1.reverse()
g2 = ""
g3 = g2.join(g1)
print("Al invertir el numero queda(primer numero): " + str(g3))

""" CONVERTIR F A LISTA Y APLICAR LAS OPERACIONES """
f = list(str(f))
f1 = list(f)
f1.insert(2, f1[0])
f1.pop(0)
f2 = ""
f3 = f2.join(f1)
print("Al invertir la primer y segunda cifra queda(segundo numero): " + str(f3))

""" OPERACIONES MATEMATICAS SEGUN F O G ES MAYOR """
if f > g:
    print("suma de las cifras del primer numero: " +
          str(int(g[0])+int(g[1])+int(g[2])))
    print("suma de las cifras del segundo numero: " +
          str(int(f[0])+int(f[1])+int(f[2])))
    print("multipliacion de las cifras del primer numero: " +
          str(int(g[0])*int(g[1])*int(g[2])))
    print("multiplicacion de las cifras del segundo numero: " +
          str(int(f[0])*int(f[1])*int(f[2])))
elif f < g:
    print("resta de las cifras del primer numero: " +
          str(int(g[0])-int(g[1])-int(g[2])))
    print("resta de las cifras del segundo numero: " +
          str(int(f[0])-int(f[1])-int(f[2])))
    print("division de las cifras del primer numero: " +
          str(int(g[0])/int(g[1])/int(g[2])))
    print("division de las cifras del segundo numero: " +
          str(int(f[0])/int(f[1])/int(f[2])))
