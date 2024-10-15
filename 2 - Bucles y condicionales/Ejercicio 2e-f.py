
n1= int(input("Introduce el primer numero: ")) #pide un numero para compararlo con el siguiente y decir cual es mayor o menor

n2 = int(input("Introduce el segundo numero: "))

if n1 == n2:

    print(n1, " ", n2, " Son iguales")

else:    

    if n1 > n2:

        print("El numero mas grande es: ", n1,",", "Y el mas pequeño es: ", n2)

    else:
        
        print("El numero mas grande es: ", n2, "Y el mas pequeño es: ", n1)
