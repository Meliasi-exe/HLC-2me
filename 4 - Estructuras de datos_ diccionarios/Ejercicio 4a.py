
from os import system 

asignatura = " " #contendra nombre de asignaturas (cadena)

calificacion = 0 #nota de las anignaturas (float) 

DiccionarioAsig = {} #Dicionario para los nombre y las calificaciones {"Nombre asignatura": calificacion}

sumaCalif = 0

system("cls")

while asignatura != "" :
    asignatura = input("Introduce el nombre de la asignatura (ENTER finalizar): ")

    if asignatura != "":
        calificacion = float(input("Introduce la calificacion de dicha asignatura: "))
        DiccionarioAsig[asignatura] = calificacion #añadir elementos al diccionario
    
    print("") #salto de linea

for asignatura, calificacion in DiccionarioAsig.items():
    if calificacion >= 5:
        print(f"La asignatura {asignatura}, esta aprobada con un {calificacion}")
    sumaCalif = sumaCalif + calificacion

print(f"La media aritmetica de las calificaciones es {sumaCalif/len(DiccionarioAsig)}")
