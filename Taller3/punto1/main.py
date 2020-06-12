from db_connect import get_user_information, change_password
 
#--------------------------


def loged_menu(user):
    """ Menú de sesión iniciada. No retorna. Parámetro: Nombre de usuario (variable string) """
    #Verificación de opción válida
    while True:
        print('1 - Cambiar contraseña\n2 - Cerrar Sesión')
        op_loged_menu = input(' : ')
        #menu
        if op_loged_menu == '1':
            #pide nueva password y llama la función del modulo.
            new_password = input('Ingrese la nueva contraseña: ')
            change_password(user, new_password)
            break
        elif op_loged_menu == '2':
            break

#Programa
print('--SISTEMA DE USUARIOS--')
while True:
    #menú
    op_menu = input('1 - Ingresar\n2 - Salir\n  : ')
    if op_menu == '1':
        print('Ingrese sus datos a continuación: ')
        while True:
            #pide nombre de usuario, verifica que exista y trae la info.
            user = input('Nombre de usuario: ')
            user_info = get_user_information(user)
            if user == user_info[0]:
                while True:
                    passw = input('Contraseña: ')
                    #verifica la contraseña
                    if passw == user_info[1]:
                        print('Contraseña correcta')
                        #llama la función del menú con sesión iniciada.
                        loged_menu(user_info[0])
                        break
                    else:
                        print('Contraseña incorrecta.')
                break
            else:
                print('ERROR: Este usuario no existe')
    elif op_menu == '2':
        print('Selecionó opción salir')
        break
