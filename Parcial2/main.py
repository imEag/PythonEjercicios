""" Parcial 2 - Informática 1 

Solución por Emmanuel Arizabaleta Garcés 

Análisis del problema y de variables 

El ejercicio me pide hacer un programa para dar un diagnóstico de LH a un paciente.
El programa debe tener ciertas características que se piden, como por ejemplo, varios menus, 
guardar pacientes en diccionarios, permitir buscar un paciente y ver sus datos. Estas funcionalidades
desben estar contruidas siguiendo los requisitos dados.

Análisis de variables:
-un diccionario vacío donde voy a amacenar los datos de los pacientes
-una lista para los datos de cada paciente que al final se agregará al diccionario y que cada
vez que añadan uno nuevo se vaciará la lista.
-contadores para cada eps y poder generar el código.
-algunas variables para guardar cada dato del paciente y hacer las operaciones necesarias con ellos.
- variable para manejar el menú.
-variable para almacenar la busqueda de paciente y el resultado.

solución planteada:

La solución que planteo es:
importar modulos
declarar varibles (no es necesario en python pero lo tengo como una práctica)
tener un menú principal hecho con un ciclo while. 
declarar mas variabes dentro del ciclo while, que se vaciarán cada vez que se agregue un usario

Para la opción 1 de ingresar usuario:
se recogen todos los datos necesarios, con la metodología pedida
en el ejercicio (usando try/excepts, funciones hechas en otro archivo, etc)
utilizo mas ciclos while para verificar que si pongan algunos datos de forma correcta, por ejemplo el género
o la menopausia.
utilizo funciones con try/exceps para verificar datos que son numericos.
utilizo una función para calcular el diagnóstico
utilizo condicionales, contadores y una funcion con diferentes parámetros en cada caso para generar el código para cada user.
luego la lista creada con la info del user se agrega al diccionario general.

Para la opción 2 de buscar un paciente.
Utilizo un ciclo while y un try/except para verificar que la entrada sea correcta (que si sean números y que el paciente si exista)
Guardo el resultado de la busqueda en una variable que quedará en lista
imprimo los valores de la lista de manera ordenada.

Para la opción 3 simplemente utilizo el brake para terminar el ciclo.


SOLUCIÓN """


from funciones import Generar_codigo, Diagnostico_LH, Introducir_Num
print('Bienvenido al sistema de dianóstico de LH')

pacientes = {}
cont_sisben = 0
cont_sura = 0
cont_coomeva = 0
cont_medimas = 0
cont_ipsu = 0
cont_saludt = 0

while True:

    paciente = []
    menu_op = ''
    bandera_genero = False
    pac_genero = ''
    pac_menopausia = ''
    pac_eps = ''
    dx_lh = ''
    busqueda = ''
    resultado = ''

    print('\nMenú\n1 - Ingresar un paciente\n2 - Informe de afiliación a EPS\n3 - Salir')
    menu_op = input('Ingrese una opción: ')

    if menu_op == '1':
        print('Ingrese los siguientes datos')

        paciente.append(input('Nombre: '))
        paciente.append(Introducir_Num('Identificación', 'int'))
        pac_edad = Introducir_Num('Edad', 'int')
        paciente.append(str(pac_edad))

        while bandera_genero == False:
            pac_genero = input('Género:\n1 - Masculino\n2 - Femenino\n : ')

            if pac_genero == '2':
                paciente.append('Femenino')

                while True:
                    pac_menopausia = input('Menopausia:\n1 - Si\n2 - No\n : ')

                    if pac_menopausia == '1':
                        paciente.append('Si')
                        bandera_genero = True
                        break

                    elif pac_menopausia == '2':
                        paciente.append('No')
                        bandera_genero = True
                        break

                    else:
                        print('Ingrese una opción válida')

            elif pac_genero == '1':
                paciente.append('Masculino')
                paciente.append('Menopausia no aplica')
                break
            else:
                print('Ingrese una opción válida')

        pac_lh = Introducir_Num('LH en UI/L', 'float')
        paciente.append(str(pac_lh))
        dx_lh = Diagnostico_LH(pac_genero, pac_edad, pac_menopausia, pac_lh)
        paciente.append(dx_lh)

        while True:
            pac_eps = input(
                'EPS:\n1 - Sisben\n2 - Sura\n3 - Coomeva\n4 - Medimas\n5 - IPS Universitaria\n6 - Salud Total\n : ')

            if pac_eps == '1':
                paciente.append('Sisben')
                cont_sisben += 1
                paciente.append(Generar_codigo(pac_eps, cont_sisben))
                break

            elif pac_eps == '2':
                paciente.append('Sura')
                cont_sura += 1
                paciente.append(Generar_codigo(pac_eps, cont_sura))
                break

            elif pac_eps == '3':
                paciente.append('Coomeva')
                cont_coomeva += 1
                paciente.append(Generar_codigo(pac_eps, cont_coomeva))
                break

            elif pac_eps == '4':
                paciente.append('Medimas')
                cont_medimas += 1
                paciente.append(Generar_codigo(pac_eps, cont_medimas))
                break

            elif pac_eps == '5':
                paciente.append('IPS Universitaria')
                cont_ipsu += 1
                paciente.append(Generar_codigo(pac_eps, cont_ipsu))
                break

            elif pac_eps == '6':
                paciente.append('SaludTotal')
                cont_saludt += 1
                paciente.append(Generar_codigo(pac_eps, cont_saludt))
                break

            else:
                print('Ingrese una opción válida')

        print('Código de paciente ingresado: '+paciente[8])
        print('Diagnóstico del paciente: ' + paciente[6])

        pacientes.update({str(paciente[1]): paciente})

    elif menu_op == '2':
        while True:
            try:
                busqueda = str(Introducir_Num(
                    'Ingrese el número de documento para buscar un paciente', 'int'))
                resultado = pacientes[busqueda]
                break
            except KeyError:
                print('El paciente con id ' + busqueda + ' no está en la BD')
        print('\n--- RESULTADO BUSQUEDA---')
        print('Nombre: {0}\nIdentificación: {1}\nEdad: {2}\nGénero: {3}\nMenopausia: {4}\nLH: {5}\nDiagnóstico: {6}\nEPS: {7}\nCódigo: {8}'.format(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6], resultado[7], resultado[8]))
    elif menu_op == '3':
        print('Cerrando programa.')
        break
    else:
        print('Ingrese una opción válida')
