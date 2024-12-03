
from cryptography.fernet import Fernet

# generammos una clave simetrica.

def load_key():

    return open("./Cifrado/Clave.key", "rb").read()

# Programa principal

#write_key() # Se debe ejecutar solo la primera vez para generar la clase, luego comentarlo

Clave = load_key()

fraseCifrada = input("Teclea la frase cifrada: ") #introducir sin la primera b y sin las comillas ' '

f = Fernet(Clave)

frase = f.decrypt(fraseCifrada)

frase = frase.decode() #Decodifica desde binario UTF - 8 a cadena str

print(frase)


