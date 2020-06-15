
import mysql.connector
# Datos de inicio de sesión
SERVER = 'localhost'
USER = 'root'
PASSWORD = ''
DB = 'taller3ej1'


def get_user_information(user):
    """ Recoje la info del usuario. Parámetro: Nombre de usuario (string). Retorna una lista """
    try:
        #establece  conexión
        cnx = mysql.connector.connect(
        user=USER, password=PASSWORD, host=SERVER, database=DB)
        connection = cnx.cursor()
        #query
        sql = "SELECT user.user_name, user.password FROM user WHERE user.user_name='%s'" % user
        connection.execute(sql)
        result = connection.fetchall()
        #Si no hay dicho ususario retorna una lista vacía.
        if result == []:
            return ['']
        else:
            return result[0]
        #Cierra conexión
        cnx.commit()
        cnx.close()
    except: 
        print('Ocurrió un error')

def change_password(user_name, new_password):
    """ Cambia la contraseña de un usuario. Parámetros: Nombre de usuario (Str), nueva password (string). No retorna"""
    try:
        #Conexión
        cnx = mysql.connector.connect(
        user=USER, password=PASSWORD, host=SERVER, database=DB)
        connection = cnx.cursor()
        #query
        sql = "UPDATE user SET password=" + new_password + \
            " WHERE user_name='%s'" % user_name
        connection.execute(sql)
        #Cierra conexión
        cnx.commit()
        cnx.close()
    except:
        print('Ocurrió un error')