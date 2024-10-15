
n = int(input("Introduce un numero: "))

while n <= 0 or n >= 11: #Te pedira numeros hasta que le des uno entre 1 y 10
      
    print("Tu numero es erroneo, introduzca otro...")

    n = int(input("Introduce un numero: "))

print("Tu numero esta entre 1 y 10, marcaste el numero:", n)