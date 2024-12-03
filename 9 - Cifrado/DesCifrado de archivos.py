
from cryptography.fernet import Fernet

# generammos una clave simetrica.

def write_key():

    clave = Fernet.generate_key() #Genera la clave

    with open("./Cifrado/Clave.key", "wb") as key_file:
        key_file.write(clave)

def load_key():

    return open("./Cifrado/Clave.key", "rb").read()

def descifrar(nombreArchivo, clave):
    
    """Funcion que dado el nombreArchivo y la clase, descifra el archivo y lo guarda en disco"""
    
    f = Fernet(clave) #Inicializamos objeto fernet

    with open(nombreArchivo, "rb") as archivo: #leemos contenido del archivo
        datosCifrados = archivo.read()

    datos = f.decrypt(datosCifrados)

    if ".cifrado" in nombreArchivo:
        nombreArchivo = nombreArchivo.split('.')[:-1] #eliminar la extension .cifrado
        nombreArchivo = ".".join(nombreArchivo)

    with open(nombreArchivo, "wb") as archivo:
        archivo.write(datos) #Guarda en disco el archivo, con datos cifrados (sobreescrito al original)

# Programa principal

#write_key() # Se debe ejecutar solo la primera vez para generar la clase, luego comentarlo

clave = load_key()

nombreArchivo = input("Teclea el nombre del archivo a descifrar: ")

nombreArchivo = "./Cifrado/" + nombreArchivo #añade la ruta donde buscar

descifrar(nombreArchivo, clave)

print(f"El archivo {nombreArchivo} ha sido descifrado correctamente.")
