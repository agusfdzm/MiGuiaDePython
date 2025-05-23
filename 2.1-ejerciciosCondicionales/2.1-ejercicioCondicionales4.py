"""
Comprobar si el usuario introduce un numero, si no es un numero indicar que debe introducir un entero. Si es un numero, deberemos comprobar si es o no PAR y notificarlo al usuario.
"""

numero = input("Introduce un numero: ")

if (numero.isnumeric() == True):
    numero = int(numero)
    if (numero % 2 == 0):
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} no es par")
else:
    print("No has introducido un numero")