s = 0

m = 1

n = int(input("Introduce un numero: "))

while n != 0: # te pide numero hasta que le metas un 0, y va sumando y multiplicando esos numeros

    s = s + n

    m = m * n

    print(f"suma va por {s}, multiplicacion va por {m}")

    n = int(input("Introduce un numero: "))

print(f"La suma es: {s}, y el producto es: {m}")


