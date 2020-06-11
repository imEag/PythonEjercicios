### MODULE NOT WORKING RN
import mysql.connector

SERVER = 'localhost'
USER = 'root'
PASSWORD = ''
DB = 'taller3ej1'
cnx = mysql.connector.connect(
    user=USER, password=PASSWORD, host=SERVER, database=DB)


def get_user_information(user):
    try:
        connection = cnx.cursor()
        sql = "SELECT user.user_name, user.password FROM user WHERE user.user_name='%s'" % user
        connection.execute(sql)
        result = connection.fetchall()

        if result == []:
            return ['']
        else:
            return result[0]

    except:
        print('Ocurrió un error')
    finally:
        cnx.commit()
        cnx.close()




def change_password(user_name, new_password):
    connection = cnx.cursor()
    sql = "UPDATE user SET password=" + new_password + \
        " WHERE user_name='%s'" % user_name
    connection.execute(sql)
    print('Ocurrió un error')
    cnx.commit()
    cnx.close()

""" def change_password(user_name, new_password):
    try:
        connection = cnx.cursor()
        sql = "UPDATE user SET password=" + new_password + " WHERE user_name='%s'" % user_name
        connection.execute(sql)
    except:
        print('Ocurrió un error')
    else:
        cnx.commit()
        cnx.close()
 """