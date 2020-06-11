import mysql.connector

SERVER = 'localhost'
USER = 'root'
PASSWORD = ''
DB = ''
cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=SERVER, database=DB)


