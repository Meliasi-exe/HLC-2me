import math

modo = input("1 para dBv a V, 2 para V a dBv: ")

unidad = 1

if modo == "1":

    while unidad != 0 :

        unidad = float(input(f"introduce los dBv para combertir a V: "))

        if unidad == 0:

            break

        result = float(10**(unidad / 20))

        print(f"{unidad}dBv son {result}V")

elif modo == "2":

    while unidad != 0:

        unidad = float(input(f"introduce los V para combertir a dBv: "))

        if unidad == 0:

            break

        result = float(20*math.log10(unidad )) 

        print(f"{unidad}V son {result}dBv")