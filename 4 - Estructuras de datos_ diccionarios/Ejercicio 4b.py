from os import system

frase = " " #contendra la frase a analizar

dicLetras = {} #definimos el diccionario {"letra": n apariciones}

system("cls")

frase = input("Teclea la frase a escanear: ")

for letra in frase: #recorre la frase letra por letra
    
    if letra in dicLetras: #busca en el disc la letra, si ya miremos esa letra, le suma 1 

        dicLetras[letra] += 1

    else: #si no teniamos esa letra, la añade con un 1 

        dicLetras[letra] = 1

for letra, numVeces in dicLetras.items():

    if letra != " ":

        print(f"La letra {letra} esta {numVeces} veces")

    else:

        print(f"El espacio esta {numVeces} veces")