
"""Version del ejer 6 de Excepciones, con modulos y paquetes"""

# Importación de librerías:
from os import system

from FuncionesInventario import *

# Declaración de variables:
inventario = {} # Diccionario que contendrá toda la estructura.

def menu(): #Menu principal con "Todo"
    opcion = 0
    while opcion != 6:
        system("cls")
        print("") # Salto de línea para dejar una línea en blanco.
        print("***************   MENÚ PRINCIPAL  ****************")
        print("1.- Agregar un producto al inventario.")
        print("2.- Buscar un producto en el inventario.")
        print("3.- Actualizar la cantidad de un producto del inventario.")
        print("4.- Eliminar un producto al inventario.")
        print("5.- Mostar todos los productos del inventario.")
        print("6.- Salir del programa")
        print("")

        try:
            opcion = int(input("Elige la opción correspondiente... "))
        except ValueError:
            continue #se vuelve al principio del bucle.

        if opcion == 1: # Agregar un producto al inventario.
            agregarProducto(inventario)

        elif opcion == 2: # Buscar un producto en el inventario..
           buscarProducto(inventario)
        
        elif opcion == 3: #  Actualizar la cantidad de un producto del inventario.
            actualizarCantidad(inventario)

        elif opcion == 4: #  Eliminar un producto al inventario.
            eliminarProducto(inventario)

        elif opcion == 5: #  Mostar todos los productos del inventario..
            listadoProductos(inventario)

# Programa principal:

menu()