from db_connect import get_user_information, change_password
 
#--------------------------

def loged_menu(user):
    while True:
        print('1 - Cambiar contraseña\n2 - Cerrar Sesión')
        op_loged_menu = input(' : ')
        if op_loged_menu == '1':
            new_password = input('Ingrese la nueva contraseña: ')
            change_password(user, new_password)
            break
        elif op_loged_menu == '2':
            break


print('--SISTEMA DE USUARIOS--')
while True:
    op_menu = input('1 - Ingresar\n2 - Salir\n  : ')
    if op_menu == '1':
        print('Ingrese sus datos a continuación: ')
        while True:
            user = input('Nombre de usuario: ')
            user_info = get_user_information(user)
            if user == user_info[0]:
                while True:
                    passw = input('Contraseña: ')
                    if passw == user_info[1]:
                        print('Contraseña correcta')
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
