n = int(input("Introduce un numero: ")) #pide un numero, para decir que dia de la semana es ese numero del 1 al 7

if n == 1:
    print("Lunes")

elif n == 2:
    print("Martes")

elif n == 3:
    print("Miercoles")

elif n == 4:
    print("Jueves")

elif n == 5:
    print("Viernes")

elif n == 6:
    print("Sabado")

elif n == 7:
    print("Domingo")

else:
    print(f"Tu numero no concuerda con ningun dia de la semana...")