""" Parcial #1 """
""" Análisis del problema: el programa será un algoritmo que da un diagnóstico 
sobre la viabilidad de entrar a cirugía un paciente de acuerdo a su PT, PTT y Fibrinógeno
Los datos que debo pedir al usuario son: Nombre, ID, PT, PTT y Fibrinógeno (en g/L y 
luego convertirlo a mg/dL). El diagnóstico se hace revisando que los valores suministrados 
estén dentro de los rangos establecidos por si el paciente tomó anticuagulante o no.
Además de esto debo almacenar los valores en listas anidadas (una lista con todos los 
pacientes y cada paciente es una lista). 

La solución que planteo a nivel de código es: 
Declarar la lista vacía de pacientes e  iniciar el ciclo for.
dentro del ciclo declaro una  lista de un solo paciente que va a llevar sus datos
Pido todos los datos, los almaceno en la lista y le hago todos los procesos de condicionales
para determinar si es un paciente apto o no(basandome en las condiciones que pide el 
ejercicio.).Para eso utilizo algo conocido como una "bandera", que en este caso es una variable
booleana declarada como true. Si ningún valor se sale del rango establecido entonces
la variable se conserva como True y el paciente será apto para cirugía.
En caso de que haya un valor que se  salga de los límites se cambiará el valor de la variable
a False, y se dará el diagnóstico de que no puede ser entrado a cirugía y se necesitan mas
estudios complementarios.
Al final, se mete la lista del paciente en la lista grande y se pregunta al usuario si 
quiere ingresar otro paciente o ver los resultados.
para mostrar los resultados se recorre la lista con un for y se le da formato y se imprime
la informacion de los pacientes.
"""

print("Diagnostico de viabilidad para cirugía según pruebas de coagulación")
pacientes = []
for i in range(10000):
    paciente = []

    nombre = input("Ingrese el nombre del paciente: ")
    paciente.append(nombre)
    idcion = input("Ingrese el ID del paciente: ")
    paciente.append(idcion)
    aC = input("¿El paciente esta tomando anticoagulante?\n     1 - Si\n     2 - No\n          : ")
    aCEstado = False
    if aC == "1":
        aCEstado = True
    pt = input("Ingrese los valores del PT del paciente (en IIN): ")
    paciente.append(pt)
    ptt = input("Ingrese el PTT (en seg): ")
    paciente.append(ptt)
    fn = input("Ingrese Fibrinógeno (en g/L): ")
    fnFinal = float(fn)*100
    paciente.append(str(fnFinal))

    apto = True
    if aCEstado == True:
        if float(pt) < 2 or float(pt) > 3:
            apto = False
        if float(ptt) < 62 or float(ptt) > 88:
            apto = False
    else:
        if float(pt) < 0.8 or float(pt) > 1.1:
            apto = False
        if float(ptt) < 25 or float(ptt) > 35:
            apto = False
    if float(fnFinal) < 200 or float(fnFinal) > 400:
        apto = False
    
    if apto == True:
        dx = "Paciente apto para cirugía"
    else:
        dx = "Paciente no apto para cirugía, se requieren estudios complementarios"
    paciente.append(dx)
    print(dx)
    pacientes.append(paciente)

    salir = input("¿Desea ingresar mas pacientes?\n     1 - Ingresar otro paciente\n     2 - Salir y ver los datos de todos los pacientes\n          : ")
    if salir == "2":
        break

j = 1
for p in pacientes:
    print("\n")
    print("Paciente número {0}".format(j))
    print("Nombre: {0}\nID: {1}\nPT: {2}IIN\nPTT: {3}s\nFibrinógeno: {4}mg/dL\nDiagnóstico: {5}".format(p[0], p[1], p[2], p[3], p[4], p[5]))
    j += 1