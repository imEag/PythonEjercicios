print("Bienvenido a la calculadora de LPA")

idcion = ""
p2i = ""
f2 = ""

historico = []

""" -------------- """

pacienteN = 1

while True:
    print("Paciente número {0}".format(pacienteN))

    """ ------------- """
    paciente = []
    dxp2 = ""
    dxlpa = ""

    idcion = input("ingrese el ID del usuario: ")
    paciente.append(idcion)
    p2i = float(input("Ingrese el valor del Pa02(en kPa): "))
    f2 = input("Ingrese el tipo de escenario del paciente\n     1 - Aire ambiente\n     2 - Cánula nasal\n     3 - Mascarilla facial\n     4 - Ventilación mecánica\nIngrese el número índice del escenario: ")
    f2n = 0
    p2m = p2i*7.5
    paciente.append(str(p2m))
    print("La PaO2 del paciente es {0}mmHg".format(p2m))
    if 80 <= p2m <= 100:
        print("DxPaO2: normal")
        dxp2 = "Normal"
    elif p2m < 80:
        print("DXPaO2: baja")
        dxp2 = "Baja"
    elif p2m > 100:
        print("DxPaO2: alta")
        dxp2 = "Alta"

    if f2 == "1":
        f2n = 0.21
    elif f2 == "2":
        f2n = 0.30
    elif f2 == "3":
        f2n = 0.41
    elif f2 == "4":
        f2n = 0.60

    paciente.append(str(f2n))
    paciente.append(dxp2)

    lpa = p2m/f2n

    paciente.append(str(lpa))

    print("El LPA es: {0}".format(lpa))
    if lpa <= 200:
        print("DxLPA: SDRA presente")
        dxlpa = "SDRA presente"
    elif 200 < lpa <= 300:
        print("DxLPA: Lesión pulmonar (ALI)")
        dxlpa = "Lesión pulmonar"
    elif lpa > 300:
        print("DxLPA: Paciente normal")
        dxlpa = "Paciente normal"

    paciente.append(dxlpa)

    historico.append(paciente)

    """ ------------- """

    pacienteN = pacienteN + 1
    salir = input("¿Desea continuar?\n     1 - Continuar ingresando datos de otros pacientes\n     0 - Salir y ver la información de todos los pacientes\n :")

    if salir == "0":
        break


j = 1
print("Histórico de pacientes: ")
for p in historico:
    print("Paciente numero {0}".format(j))
    print("ID: {0}".format(p[0]))
    print("PaO2: {0} mmHg".format(p[1]))
    print("FiO2: {0}".format(p[2]))
    print("DxPaO2: {0}".format(p[3]))
    print("LPA: {0}".format(p[4]))
    print("DxLPA: {0}".format(p[5]))
    print("\n")

    j = j+1
