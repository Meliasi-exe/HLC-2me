
from os import system 

def modulo3D(coordx, coordy, coordz):

    """Devuelve el modulo del vector de 3 dimensiones. formato; modulo3D(coord x, coord y, coord z)"""

    return (coordx**2 + coordy**2 + coordz**2)**0.5

system("cls")    

coordX = float(input("Introduce la coordenada X del vector: "))

coordY = float(input("Introduce la coordenada Y del vector: "))

coordZ = float(input("Introduce la coordenada Z del vector: "))

print(f"El modulo del vector ({coordX}, {coordY}, {coordZ}) es {modulo3D(coordX,coordY,coordZ)}.")
