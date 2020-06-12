
import mysql.connector

SERVER = 'localhost'
USER = 'root'
PASSWORD = ''
DB = 'taller3ej1'


def get_user_information(user):
    try:
        cnx = mysql.connector.connect(
        user=USER, password=PASSWORD, host=SERVER, database=DB)
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
    except: 
        print('Ocurrió un error')

def change_password(user_name, new_password):
    try:
        cnx = mysql.connector.connect(
        user=USER, password=PASSWORD, host=SERVER, database=DB)
        connection = cnx.cursor()
        sql = "UPDATE user SET password=" + new_password + \
            " WHERE user_name='%s'" % user_name
        connection.execute(sql)
        cnx.commit()
        cnx.close()
    except:
        print('Ocurrió un error')