"""Una incubadora neonatal realiza las funciones de sensado de temperatura,
ruido ambiental y humedad  con  el  finde  advertir, por  medio  de  alarmas,
al  personal  médico  cuando  las condiciones en las que se encuentra
el paciente no son las adecuadas.El funcionamiento de los sensores
se basa en dos estados, expresados por los valores de 1 y 0,
de tal forma que la incubadora genera alarmas de acuerdo a la 
informaciónsuministrada en la tabla 1: 

Temp, humedad, ruido -> estado alarma

000 - apag
001 - enc
010 - enc
011 - enc
100 - apag
101 - enc
110 - enc
111 - enc

Realiceun  algoritmo  queapartir  de  la  información  entregada
por  cada  sensor  permita determinar si hay alarma o no.

"""

print("Bienvenido al sistema de alarma de la incubadora neonatal")
print("Escriba 0 o 1 de acuerdo al estado de temperatura, humedad o ruido")
print("de acuerdo a eso se activará o se mantendrá apagada la alarma")

while True:
    temp = input("Ingrese el estado de temperatura (1 o 0): ")
    hum = input("Ingrese el estado de Humedad (1 o 0): ")
    ruido = input("Ingrese el estado del ruido (1 o 0): ")
    if (temp == "0" or temp == "1") and (hum == "0" or hum == "1") and (ruido == "0" or ruido == "1"):
        break
    else: 
        print("Ingrese valores válidos(0 o 1)")

estado = temp + hum + ruido

alarma = False

if estado == "000":
    alarma = False
elif estado == "001":
    alarma = True
elif estado == "010":
    alarma = True
elif estado == "011":
    alarma = True
elif estado == "100":
    alarma = False
elif estado == "101":
    alarma = True
elif estado == "110":
    alarma = True
elif estado == "111":
    alarma = True

if alarma:
    print("ALARMA ENCENDIDA")
else:
    print("Alarma apagada")
