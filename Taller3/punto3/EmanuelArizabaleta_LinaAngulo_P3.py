from manejo_bd_p3 import anadir_proveedor,validar_numerico,select_proveedor

while True:
    print("Seleccione una de las opciones ")
    op=input("Menu: \n 1-Ingresar nuevo proveedor \n 2-Ver todos los proveedores \n 3-Salir \n : ")
    
    #Menú
    if op=="1":
        #Recoger datos
        id_proveedor= input(' Numero de identidad del proveedor: ')
        while validar_numerico(id_proveedor):
            id_proveedor= input(' Numero de identidad del proveedor:')
        nom_proveedor = input(' Nombre del proveedor: ')
        ape_proveedor = input(' Apellido del proveedor: ')
        empresa_proveedor = input(' Nombre de la empresa: ') 
        contacto_proveedor = input(' Numero de contacto: ')
        while validar_numerico(contacto_proveedor):
            contacto_proveedor = input(' Numero de contacto: ')
        email_proveedor = input(' Email del proveedor: ')
        
       
        #Ingresa el proveedor a la bd.
        anadir_proveedor(id_proveedor,nom_proveedor,ape_proveedor, empresa_proveedor ,contacto_proveedor,
                         email_proveedor) 
    
    elif op=="2":
        #Llamado de función
        select_proveedor()
        
    elif op=="3":
        break
    
    else:
        print("ERROR-Ingreso una opcion no valida-INTENTE DE NUEVO")
        
        
        
    

    
    
    