"""Diccionario llamado inventario tiene que estar creado para su funcionamiento"""

def agregarProducto(inventario): #1
    nombre = input("¿Qué producto quieres añadir al inventario? ")
    nombre =  nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre in inventario:
        print(f"El producto '{nombre}' ya está dentro del inventario.")
        print("")
        input("Pulsa una tecla para continuar...")
    else:
        try:
            precio = float(input("Precio del artículo: "))
            cantidad = int(input("Cantidad de artículos: "))
        except ValueError:
            print("Alguno de los dos valores indicados no son valores numericos.")
            print(f"{nombre}, no se añadio correctamente.")
        else:
            inventario[nombre] = {"precio": precio, "cantidad": cantidad}
            print(f"El producto '{nombre}' ha sido añadido a la lista.")

        print("")
        input("Pulsa una tecla para continuar...")

def buscarProducto(inventario): #2
    nombre = input("¿De que producto quieres ver detalles? ")
    nombre =  nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre not in inventario:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")
        print("")
        input("Pulsa una tecla para continuar...")
    else:
        print(f"Producto: {nombre}, Cantidad: {inventario[nombre]["cantidad"]}, Precio: {inventario[nombre]["precio"]}")
        input("Pulsa una tecla para continuar...")

def listadoProductos(inventario): #5
    print("Listado de los elementos...")
    for nombre, valor in inventario.items(): # Recorro todo el diccionario principal.
        print(f"Producto: {nombre}, Precio: {valor["precio"]}, Cantidad: {valor["cantidad"]}.")

    print("")
    input("Pulsa una tecla para continuar...")     

def eliminarProducto(inventario): #4
    nombre = input("¿Qué producto quieres eliminar del inventario? ")
    nombre =  nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre not in inventario:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")
        print("")
        input("Pulsa una tecla para continuar...")
    else:
        del[inventario[nombre]]
        input(f"{nombre} fue eliminado. Pulsa una tecla para continuar...")

def actualizarCantidad(inventario): #3
    nombre = input("¿De qué producto quieres modificar el stock? ")
    nombre =  nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre not in inventario:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")
        print("")
        input("Pulsa una tecla para continuar...")
    else:
        try:
            cantidad = int(input("Introduce la nueva cantidad en stock: "))
        except ValueError:
            print("El valor no es de tipo numerico.")
            print("La cantidad no fue modificada.")
        else:
            inventario[nombre]["cantidad"] = cantidad
            print(f"El producto '{nombre}' ha actualizado correctamente su stock a {cantidad} unidades.")

        print("")
        input("Pulsa una tecla para continuar...")

