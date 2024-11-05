
from os import system 

def rango(valor, limiteInferior, limiteSuperior):

    """Devuelve true o false, si un valor esta entre otros dos valores. Formato; rango(valor, limiteInferior, limiteSuperior) -> booleam"""
    
    if valor >= limiteInferior and valor <= limiteSuperior:

        return True
    
    else:

        return False
    
system("cls")

valor = input("Numero a comprobar; ")

limiteInferior = input("Teclea el limite inferior del intervalo; ")

limiteSuperior = input("Teclea el limite superior del intervalo; ")

if rango(valor, limiteInferior,limiteSuperior):

    print("Esta dentro del intervalo")

else:

    print("No esta dentro del intervalo")
