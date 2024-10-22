
usuarios = { #dicionario con los datos de los usuarios inventados
	"aexposito":
		{"nombre": "Antonio",
		"apellidos": "Expósito",
		"password": "123456"},
	"fgonzalez":
		{"nombre": "Francisco",
		"apellidos": "González",
		"password": "jejejaja"},
	"lcastillo":
		{"nombre" : "Lourdes" ,
		"apellidos": "Castillo",
		"password": "6789"}
	        }


from os import system

numIntentos = 0 #Nº intentos de login

numMaxIntentos = 3 #Nº max de intentos

usuario = "" #para pedir por teclado

contrasena = "" #contraseña a pedir por teclado

system("cls")

#mientras usuario no este en el dicc o la contraseña no este en el dicc, o superaste el numero de intentos
while (usuario not in usuarios.keys() or contrasena not in usuarios[usuario]["password"]) and numIntentos < numMaxIntentos:

    usuario =  input(f"Introduce usuario: ")

    if usuario in usuarios.keys(): #si usuario esta dentro de usuarios
      
        contrasena = input(f"Introduce contraseña: ")

        if contrasena != usuarios[usuario]["password"]: #si contraseña es incorrecta

            numIntentos += 1
            
            print(f"La contraseña es incorrecta. Te quedan {numMaxIntentos-numIntentos} intentos.")

    else: #si usuario no esta dentro de usuarios
      
        numIntentos += 1

        print(f"Usuario no encontrado. Te quedan {numMaxIntentos-numIntentos} intentos.")

if numIntentos == numMaxIntentos: #superaste los intentos

    print("Superaste el numero de intentos...")

else: #saliste con buenas credenciale sin superar el numero de intentos 

    print(f"Acceso conseguido, WELLCOME {usuarios[usuario]["nombre"]}.")


    