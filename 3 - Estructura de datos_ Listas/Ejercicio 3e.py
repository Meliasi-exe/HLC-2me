
from os import system 

asignatura = " " #contendra nombre de asignaturas (cadena)

calificacion = 0 #nota de las anignaturas (float) 

listaAsig = [] #matriz para los nombre y las calificaciones

sumaCalif = 0

system("cls")

while asignatura != "" :
    asignatura = input("Introduce el nombre de la asignatura (ENTER finalizar): ")

    if asignatura != "":
        calificacion = float(input("Introduce la calificacion de dicha asignatura: "))
        listaAsig.append([asignatura, calificacion]) #añade dos valores a la matriz
    
    print("") #salto de linea

for asignatura, calificacion in listaAsig:
    if calificacion >= 5:
        print(f"La asignatura {asignatura}, esta aprobada con un {calificacion}")
    sumaCalif = sumaCalif + calificacion

print(f"La media aritmetica de las calificaciones es {sumaCalif/len(listaAsig)}")
