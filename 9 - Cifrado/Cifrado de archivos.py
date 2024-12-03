
from cryptography.fernet import Fernet

# generammos una clave simetrica.

def write_key():

    clave = Fernet.generate_key() #Genera la clave

    with open("./Cifrado/Clave.key", "wb") as key_file:
        key_file.write(clave)

def load_key():

    return open("./Cifrado/Clave.key", "rb").read()

def cifrar(nombreArchivo, clave):
    
    """Funcion que dado el nombreArchivo y la clase, cifra el archivo y lo guarda en disco"""
    
    f = Fernet(clave) #Inicializamos objeto fernet

    with open(nombreArchivo, "rb") as archivo: #leemos contenido del archivo
        datosArchivo = archivo.read()

    datosCifrados = f.encrypt(datosArchivo) #ciframos el contenido del archivo

    with open(nombreArchivo + ".cifrado", "wb") as archivo:
        archivo.write(datosCifrados) #Guarda en disco el archivo, con datos cifrados (sobreescrito al original)

# Programa principal

#write_key() # Se debe ejecutar solo la primera vez para generar la clase, luego comentarlo

clave = load_key()

nombreArchivo = input("Teclea el nombre del archivo a cifrar: ")

nombreArchivo = "./Cifrado/" + nombreArchivo #añade la ruta donde buscar

cifrar(nombreArchivo, clave)

print(f"El archivo {nombreArchivo} ha sido cifrado correctamente -> {nombreArchivo}.cifrado")