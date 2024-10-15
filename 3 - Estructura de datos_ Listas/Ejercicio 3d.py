
from os import system

system ("cls")

indice = 0 #usada para saber que comparamos 

palind = True #boleana, indica si es un palindromo o no

pal = input("Introduzca la palabra a analizar: ") #pide la palabra

longPal = len(pal) - 1 #mido la palabra, y se le resta uno (te da un numero, pero luego se muestrea desde el 0 al ...)

while indice < longPal - indice and palind == True: #para que se reproduzca mientras sea >= el indice que la longitud - indice
    if pal[indice] != pal[longPal - indice]: #pal[2] te da la letra 3 de la palabra (0 - 1 - 2) 
        palin = False
        print("comprobando")
    indice = indice + 1

if palind == True:
    print(f"La palabra {pal}, es un palindromo")
else:
    print(f"La palabra {pal}, NO es un palindromo")