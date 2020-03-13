""" Realice un algoritmo que lea un número binario de 8 bits 
y muestre en pantalla su equivalente
en hexadecimal, octal y decimal."""

""" Binario a hexadecimal """
print("Calculadora de numero binario a Hexadecimal, octal y decimal")
while True:
    binario = input("Ingrese el numero binario (de 8 bits): ")
    binarioV = True
    for index in list(binario):
        if index != "1" and index != "0":
            binarioV =False
            break
    if (len(list(binario)) == 8) and binarioV == True:
        break
    else:
        print("Ingrese un numero de 8 bit válido (0 o 1)")

campo1="nada"

arrayBinario = list(binario)
arrayBinario.insert(4, " ")
strBinario = "".join(arrayBinario)
arrayBinario2 = strBinario.split()


if arrayBinario2[0] == "0000":
    campo0 = "0"
elif arrayBinario2[0] == "0001":
    campo0 = "1"
elif arrayBinario2[0] == "0010":
    campo0 = "2"
elif arrayBinario2[0] == "0011":
    campo0 = "3"
elif arrayBinario2[0] == "0100":
    campo0 = "4"
elif arrayBinario2[0] == "0101":
    campo0 = "5"
elif arrayBinario2[0] == "0110":
    campo0 = "6"
elif arrayBinario2[0] == "0111":
    campo0 = "7"
elif arrayBinario2[0] == "1000":
    campo0 = "8"
elif arrayBinario2[0] == "1001":
    campo0 = "9"
elif arrayBinario2[0] == "1010":
    campo0 = "A"
elif arrayBinario2[0] == "1011":
    campo0 = "B"
elif arrayBinario2[0] == "1100":
    campo0 = "C"
elif arrayBinario2[0] == "1101":
    campo0 = "D"
elif arrayBinario2[0] == "1110":
    campo0 = "E"
elif arrayBinario2[0] == "1111":
    campo0 = "F"
 
if arrayBinario2[1] == "0000":
    campo1 = "0"
elif arrayBinario2[1] == "0001":
    campo1 = "1"
elif arrayBinario2[1] == "0010":
    campo1 = "2"
elif arrayBinario2[1] == "0011":
    campo1 = "3"
elif arrayBinario2[1] == "0100":
    campo1 = "4"
elif arrayBinario2[1] == "0101":
    campo1 = "5"
elif arrayBinario2[1] == "0110":
    campo1 = "6"
elif arrayBinario2[1] == "0111":
    campo1 = "7"
elif arrayBinario2[1] == "1000":
    campo1 = "8"
elif arrayBinario2[1] == "1001":
    campo1 = "9"
elif arrayBinario2[1] == "1010":
    campo1 = "A"
elif arrayBinario2[1] == "1011":
    campo1 = "B"
elif arrayBinario2[1] == "1100":
    campo1 = "C"
elif arrayBinario2[1] == "1101":
    campo1 = "D"
elif arrayBinario2[1] == "1110":
    campo1 = "E"
elif arrayBinario2[1] == "1111":
    campo1 = "F"

print("el número en hexadecimal es: " + campo0+campo1)

""" Binario a decimal """
j=len(list(binario))-1
decimal=0
for i in list(binario):
    n = int(i) * (2**j)
    decimal += n
    j -= 1
print("El decimal es {0}".format(decimal))

""" Binario a Octal """

arrayBinario3 = list(binario)
arrayBinario3.insert(0, "0")
arrayBinario3.insert(3, " ")
arrayBinario3.insert(7, " ")
strBinario2 = "".join(arrayBinario3)
arrayBinario4 = strBinario2.split()

octal = ""
for k in arrayBinario4:
    if k == "000":
        campoOctal = "0"
    elif k == "001":
        campoOctal = "1"
    elif k == "010":
        campoOctal = "2"
    elif k == "011":
        campoOctal = "3"
    elif k == "100":
        campoOctal = "4"
    elif k == "101":
        campoOctal = "5"
    elif k == "110":
        campoOctal = "6"
    elif k == "111":
        campoOctal = "7"
    octal += campoOctal
print("El octal es {0}".format(octal))