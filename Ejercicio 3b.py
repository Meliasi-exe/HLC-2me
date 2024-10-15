#Listas

nloteria = [0, 0, 0, 0, 0, 0, 0] #lista del 0 al 6 (7 cosas)

for c in range(0,7):
    nloteria[c] = int(input(f"Introduce el dia de la loteria del {c + 1}º dia: ")) #pide que le ingreses los 7 numeros

nloteria.sort() #Ordenar la lista de menor a mayor

print(f"La lista ordenada de menor a mayor: {nloteria}")

nloteria.sort(reverse = True ) #Ordenar la lista de mayor a menor

print(f"La lista ordenada de mayor a menor: {nloteria}")