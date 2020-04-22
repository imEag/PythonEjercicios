""" importar funciones """
from funciones import Generar_Numero
from funciones import Introducir_Serial

print('---Bienvenido al sistema de inventario de Activos---')
""" diccionario principal donde se guardará todo """
activos = {'biomed': {}, 'sis': {}, 'inf': {}}

""" Contadores """
act_bio_cont = 0
act_sis_cont = 0
act_inf_cont = 0

""" menú que se repite"""
while True:
    print('Menú\n1 - Ingresar un activo\n2 - Buscar un activo\n3 - Informe de activos\n4 - Salir')
    op_menu = input('Seleccione una opción: ')
    if op_menu == '1':
        """ opción 1 -> ingresar un activo """
        activo = {'nombre': '', 'marca': '', 'serial': '',
                  'mant': '', 'calib': '', 'numero': ''}
        while True:
            """ menú de tipo de activo """
            print(
                'Area a la que pertenece\n1 - Biomédica\n2 - Sistemas\n3 - Infrastuctura')
            op_ingresar_act = input('Seleccione una opción: ')

            """ ------ Incremento contadores-------- """
            if op_ingresar_act == '1':
                act_bio_cont += 1
            elif op_ingresar_act == '2':
                act_sis_cont += 1
            elif op_ingresar_act == '3':
                act_inf_cont += 1

            """ ingresar datos """
            if op_ingresar_act == '1' or op_ingresar_act == '2'or op_ingresar_act == '3':
                print('Ingrese los siguientes datos: ')
                activo['nombre'] = input('Nombre: ')
                activo['marca'] = input('Marca: ')
                activo['serial'] = Introducir_Serial()
                activo['mant'] = input('Frecuencia de mantenimiento: ')
                if op_ingresar_act == '1':
                    activo['calib'] = input('Frecuencia de calibración: ')
                else:
                    activo['calib'] = 'No aplica'

                """ Generar numero de activo según tipo """
                if op_ingresar_act == '1':
                    activo['numero'] = Generar_Numero(
                        op_ingresar_act, act_bio_cont)
                elif op_ingresar_act == '2':
                    activo['numero'] = Generar_Numero(
                        op_ingresar_act, act_sis_cont)
                elif op_ingresar_act == '3':
                    activo['numero'] = Generar_Numero(
                        op_ingresar_act, act_inf_cont)

                """ llenar diccionario """
                if op_ingresar_act == '1':
                    activos['biomed'].update({activo['numero']: activo})
                elif op_ingresar_act == '2':
                    activos['sis'].update({activo['numero']: activo})
                elif op_ingresar_act == '3':
                    activos['inf'].update({activo['numero']: activo})
                print(activos)
                break
            else:
                print('Ingrese una opción correcta')
        
    elif op_menu == '2':
        """  nuevo diccionario sin divisiones"""
        activos_totales = {}
        activos_totales.update(activos['biomed'])
        activos_totales.update(activos['sis'])
        activos_totales.update(activos['inf'])
        print(activos_totales)

        """ buscar un activo por numero """
        busqueda = input('Ingrese el numero de activo: ')
        activos_totales.get(busqueda, "El activo no está en la BD.")
        for i in activos_totales[busqueda]:
            print(str(i) + ': '+ str(activos_totales[busqueda][i]))
    elif op_menu == '3':
        """ imprimir cantidad de activos por tipo y en total"""
        print('equipos biomedicos: ' + str(act_bio_cont))
        print('equipos de sistemas: ' + str(act_sis_cont))
        print('equipos de infrastructura: ' + str(act_inf_cont))
        print('Total de equipos: ' + str(act_bio_cont+act_inf_cont+act_sis_cont))

    elif op_menu == '4':
        """ cerrar prog. """
        print('Se cerró el prog.')
        break
    else:
        print('Ingrese una opción correcta')
    print('Sigue en el main menu')
