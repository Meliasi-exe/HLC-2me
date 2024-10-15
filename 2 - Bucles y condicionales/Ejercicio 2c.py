resu = 0

par = int(input("Introduce la cantidad de numeros pares a sumar: "))

npares = (par * 2) + 1

for numero in range(2,npares,2): #suma los n numeros pares5
   
    print(numero)
    
    resu = numero + resu

print("El resultado es =", resu)