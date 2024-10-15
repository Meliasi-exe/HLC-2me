
n = 0 #numero al que le sumo hasta que supere los 1000
c = 0 #cuento los numeros que sume
s = 0 #suma

while n <= 1000: #Suma los primeros numeros pares hasta 1000 y te muestra cuentos sumo

    print(n)

    s = s + 2 #va sumando dos para luego sumarlo al numero que tenemos 

    n = s + n #suma el numero actual con el proximo par

    c = c + 1 #suma 1 por cada numero para ver cuantos se sumaron

print("Numero final:", n)

print("Se sumaron", c, "Numeros pares")
