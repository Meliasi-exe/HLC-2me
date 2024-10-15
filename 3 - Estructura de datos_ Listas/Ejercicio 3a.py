#TUPLAS

nDias = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo") #0 el primero y 6 el ultimo en este caso

n = int(input("Introduce el numero del dia de la semana: "))

print(f"El dia es {nDias[n - 1]}") 

# -1, porque las tuplas empieza en 0, hasta el 6, y queremos que sea entre el 1 y el 7