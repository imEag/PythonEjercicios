
def validar_numerico(valor_a_validar):
    try:
        e=int(valor_a_validar)
        e=e
        return False
    except:
        print('ERROR - Ingrese únicamente datos numericos enteros')
        return True

from mysql.connector import connect

#Variables para conexion con el servidos BD
servidor='localhost'
usuario='root'
contrasena=''
bd='proveedores'

#configurar la conexion para enviar al servidor
cnx= connect(user=usuario,password=contrasena,host=servidor,database=bd)


def anadir_proveedor(id_proveedor,nom_proveedor,ape_proveedor, empresa_proveedor,contacto_proveedor,
                         email_proveedor):
    """Añade datos a la tabla proveedores en la bd. Parametros: id -> int, nombres -> str, apellidos -> str,empresa -> str, contacto -> int, email-> str """
    #Establecer la conexion con el servidor
    conexion = cnx.cursor()
    
    while True:
        #query
        sql=("""INSERT INTO proveedores (id,nombres,apellidos,empresa,contacto,email)
        VALUES ('%s','%s','%s','%s','%s','%s');"""%(id_proveedor,nom_proveedor,ape_proveedor, empresa_proveedor,contacto_proveedor,
                         email_proveedor))    
        
        try:
            conexion.execute(sql)
            break
            
        except:
            print("\n\nNumero de identidad repetido")
            return

    #cierra conexion
    cnx.commit()
    conexion.close()
    
def select_proveedor():
    """ Muestra todos los proveedores de la bd """
    #abre conexión
    conexion = cnx.cursor()
    #realiza busqueda e imprime resultados
    sql="SELECT * FROM proveedores "
    conexion.execute(sql)
    cont=0
    result=conexion.fetchall()
    for i in result:
        cont+=1
        print('\n')
        print('Proveedor: #'+str(cont))
        print("IDE: ",i[0])
        print("NOMBRE: ",i[1])
        print("APELLIDO: ",i[2])
        print("EMPRESA: ",i[3])
        print("CONTACTO: ",i[4])
        print("EMAIL: ",i[5])
        print('\n')
        
    #cierra conexion
    cnx.commit()
    conexion.close()
    