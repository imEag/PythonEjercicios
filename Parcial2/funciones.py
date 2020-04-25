""" Archivo de funciones """ 

def Generar_codigo(eps, cont_eps):
    if eps == '1':
        return ('EPS-SISBEN-'+str(cont_eps))
    elif eps == '2':
        return ('EPS-SURA-'+str(cont_eps))
    elif eps == '3':
        return ('EPS-COOMEVA-'+str(cont_eps))
    elif eps == '4':
        return ('EPS-MEDIMAS-'+str(cont_eps))
    elif eps == '5':
        return ('EPS-IPSU-'+str(cont_eps))
    elif eps == '6':
        return ('EPS-SALUDT-'+str(cont_eps))
""" print(Generar_codigo('6', 146)) """

def Diagnostico_LH(genero, edad, menopausia, lh):
    if genero == '1':
        if edad <= 18:
            if 1 <= lh <= 1.8:
                return 'Resultado normal'
            else:
                return 'Resultado anormal - Se requieres estudios complementarios'
        else:
            if 1.8 <= lh <= 8.6:
                return 'Resultado normal'
            else:
                return 'Resultado anormal - Se requieres estudios complementarios'
    else:
        if menopausia == '1':
            if 14.2 <= lh <=52.3:
                return 'Resultado normal'
            else:
                return 'Resultado anormal - Se requieres estudios complementarios'
        elif edad <= 18 and menopausia == '2':
            if 0 <= lh <= 5:
                return 'Resultado normal' 
            else:
                return 'Resultado anormal - Se requieres estudios complementarios'
        elif menopausia == '2':
            if 5 <= lh <= 25:
                return 'Resultado normal'
            else:
                return 'Resultado anormal - Se requieres estudios complementarios'

""" print(Diagnostico_LH('2', 20, '1', 27.9))
print(Diagnostico_LH('1', 20, '1', 27.9))
print(Diagnostico_LH('2', 20, '1', 7.9))
print(Diagnostico_LH('2', 20, '2', 17.9)) """

def Introducir_Num(dato_a_ingresar, tipo_de_dato):
    while True: 
        if tipo_de_dato == 'float':   
            try:
                numero = float(input(str(dato_a_ingresar)+': '))
                break
            except (ValueError, TypeError):
                print('Solo se permiten números')
        elif tipo_de_dato == 'int':
            try:
                numero = int(input(str(dato_a_ingresar)+': '))
                break
            except (ValueError, TypeError):
                print('Solo se permiten números')
    return numero

pacientes = {'1234':['emma', 18, 'si']}

""" while True:
    try:
        busqueda = input('Ingrese el número de documento para buscar un paciente: ')
        resultado = pacientes[busqueda]
        print(resultado)
        break
    except KeyError:
        print('El paciente con id ' + busqueda + ' no está en la BD') """