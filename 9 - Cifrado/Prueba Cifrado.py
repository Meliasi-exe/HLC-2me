
from cryptography.fernet import Fernet

# generammos una clave simetrica.

def write_key():

    clave = Fernet.generate_key() #Genera la clave

    with open("./Cifrado/Clave.key", "wb") as key_file:
        key_file.write(clave)

def load_key():

    return open("./Cifrado/Clave.key", "rb").read()

# Programa principal

#write_key() # Se debe ejecutar solo la primera vez para generar la clase, luego comentarlo

Clave = load_key()

frase = input("Teclea la frase a esconder: ")

frase = frase.encode() #Codigo a binario en UTF - 8

f = Fernet(Clave)

fraseCifrada = f.encrypt(frase)

print(fraseCifrada)


