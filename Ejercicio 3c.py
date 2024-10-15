matrizN = [[0,0],
           [0,0]]

for fila in range(0,2): #Bucle de filas
    for columna in range(0,2): #Bucle de columnas
        matrizN[fila][columna] = int(input(f"Introduce el valor ({fila},{columna}) de la matriz: "))

determinante = matrizN[0][0] * matrizN[1][1] - matrizN[0][1] * matrizN[1][0] #operacion del determinante

print(f"El determinante vale: {determinante}")

