""" Realice un algoritmo que lea un número binario de 8 bits 
y muestre en pantalla su equivalente
en hexadecimal, octal y decimal."""

""" BINARIO A HEXADECIMAL
 0000 -> 0
 0001 -> 1
 0010 -> 2
 0011 -> 3
 0100 -> 4
 0101 -> 5
 0110 -> 6
 0111 -> 7
 1000 -> 8
 1001 -> 9
 1010 -> A
 1011 -> B
 1100 -> C
 1101 -> D
 1110 -> E
 1111 -> F
"""
print("Calculadora de numero binario a Hexadecimal, octal y decimal")

binario = input("Ingrese el numero binario (de 8 bits): ")
campo1="nada"

arrayBinario = list(binario)
arrayBinario.insert(4, " ")
strBinario = "".join(arrayBinario)
arrayBinario2 = strBinario.split()
print(arrayBinario2)

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