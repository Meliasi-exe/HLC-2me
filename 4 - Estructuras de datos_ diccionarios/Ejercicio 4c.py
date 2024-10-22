
from os import system 

nombreArticulo = " " #contiene el nombre del articulo a comprar

precioArticulo = "" #precio del articulo

dicArticulos = {} #{"nombre articulos": precio del mismo}

sumaCompra = 0 #valor total de la suma de la compra

system("cls")

while nombreArticulo != "" :

    nombreArticulo = input("Introduce el nombre del articulo a añadir a la cesta (ENTER finalizar): ")

    if nombreArticulo != "":

        precioArticulo = float(input("Introduce su precio: "))

        dicArticulos[nombreArticulo] = precioArticulo #añadir elementos al diccionario
    
    print("") #salto de linea

for nombreArticulo, precioArticulo in dicArticulos.items():

    print(f"Articulo: {nombreArticulo},   precio: {precioArticulo}€")

    sumaCompra += precioArticulo #== sumacompra = sumacompra + precioarticulo

print(f"Importe total de la compra es {sumaCompra}€.")
