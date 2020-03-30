print("Historia clínica pacientes")
print("debberá ingresar Nombre, identificación, edad y eps del paciente")
print("en caso de que desee salir presione 0 antes de ingresar el sgnte. (se le preguntará)")


pacientes=[]
paciente=[]

for i in list(range(1000)):
    continuar = input("desee salir del programa 1-Continuar 0-Salir : ")
    if continuar == "0":
        break
    print("ingrese los datos del paciente {0}: ".format(i+1))

    paciente=[]
    
    nombre = input("Ingrese el nombre completo del paciente: ")
    paciente.append(nombre)
    id = input("Ingrese el número de ID del paciente: ")
    paciente.append(id)
    edad = input("Ingrese la edad del paciente: ")
    paciente.append(edad)
    eps = input("Ingrese la EPS del paciente: ")
    paciente.append(eps)

    print(paciente)
    pacientes.append(paciente)

print(pacientes)
print("datos de los pacientes: ")
k=0
for j in pacientes:
    print("paciente {0}: {1}".format(k+1, pacientes[k]))
    k=k+1