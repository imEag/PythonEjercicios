""" from db_connect import get_user_information, change_password
 """
#--------------------------

import mysql.connector

SERVER = 'localhost'
USER = 'root'
PASSWORD = ''
DB = 'taller3ej1'
cnx = mysql.connector.connect(
    user=USER, password=PASSWORD, host=SERVER, database=DB)


def get_user_information(user):
        connection = cnx.cursor()
        sql = "SELECT user.user_name, user.password FROM user WHERE user.user_name='%s'" % user
        connection.execute(sql)
        result = connection.fetchall()

        if result == []:
            return ['']
        else:
            return result[0]
        cnx.commit()
        cnx.close()

def change_password(user_name, new_password):
    connection = cnx.cursor()
    sql = "UPDATE user SET password=" + new_password + \
        " WHERE user_name='%s'" % user_name
    connection.execute(sql)
    cnx.commit()
    cnx.close()


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
