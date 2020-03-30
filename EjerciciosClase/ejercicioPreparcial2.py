print("Clínica veterinaria")

print("Menú principal")

pacientes = []

t = True
while t == True:
    op = input("Ingrese:\n     1- Ingresar nuevo paciente\n     2- Mostrar cantidad de pacientes\n     3- Buscar paciente por ID\n     4- Salir\n          : ")
    if op == "1":
        paciente = []
        nombre = input("Ingrese el nombre del paciente animal: ")
        paciente.append(nombre)
        idcion = input("Ingrese el código ID del paciente animal: ")
        paciente.append(idcion)
        ta = True
        while ta == True:
            tipoAnimal = input("Ingrese el tipo de animal\n     1- Perro\n     2- Gato\n         : ")
            if tipoAnimal == "1":
                ta = False
            elif tipoAnimal == "2":
                ta = False
            else:
                print("Seleccione un tipo de animal válido")
                tipoAnimal = ""
        paciente.append(tipoAnimal)
        edad = input("Ingrese edad del paciente animal: ")
        paciente.append(edad)
        print(paciente)
        pacientes.append(paciente)
    elif op == "2":
        print("El total de pacientes es {0}".format(len(pacientes)))
        contadorP = 0
        contadorG = 0
        for p in pacientes:
            if p[2] == "1":
                contadorP = contadorP + 1
            elif p[2] == "2":
                contadorG = contadorG + 1
        print("La cantidad de pacientes perro es {0} y la cantidad de pacientes gato es {1}".format(contadorP, contadorG))
    elif op == "3":
        buscar = input("Ingrese el ID del paciente a buscar: ")
        buscarTF = False
        for b in pacientes:
            if b[1] == buscar:
                print("   Nombre: {0}\n   ID: {1}\n   Tipo de Animal: {2}\n   Edad: {3}".format(b[0], b[1], b[2], b[3]))
                buscarTF = True
                break
        if buscarTF == False:
            print("El paciente no está en la BD")
    elif op == "4":
        t = False
        print(pacientes)
    else:
        print("Por favor selecciones una opción válida")
