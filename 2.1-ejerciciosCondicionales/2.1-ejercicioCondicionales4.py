numero = input("Introduce un numero: ")

if (numero.isnumeric() == True):
    numero = int(numero)
    if (numero % 2 == 0):
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} no es par")
else:
    print("No has introducido un numero")