def calculadora():
    print("1. Sumar" )
    print("2. Restar" )
    print("3. Multiplicar" )

    operacion = int(input("Introduce un número: "))

    if (operacion == 1):
        n1 = input("Introduce el primer numero de la suma: ")
        n2 = input("Ahora el segundo: ")

        if (n1.isnumeric == False or n2.isnumeric == False):
            print("Introduce un numero, patán")
        else:
            suma = int(n1) + int(n2)
            print(suma)
    elif (operacion == 2):
        n1 = input("Introduce el primer numero de la resta: ")
        n2 = input("Ahora el segundo: ")

        if (n1.isnumeric == False or n2.isnumeric == False):
            print("Introduce un numero, patán")
        else:
            resta = int(n1) - int (n2)
            print(resta)
    elif (operacion == 3):
        n1 = input("Introduce el primer numero de la multiplicación: ")
        n2 = input("Ahora el segundo: ")

        if (n1.isnumeric == False or n2.isnumeric == False):
            print("Introduce un numero, patán")
        else:
            mult = int(n1) * int(n2)
            print(mult)
    else:
        print("Opción no valida")

calculadora()