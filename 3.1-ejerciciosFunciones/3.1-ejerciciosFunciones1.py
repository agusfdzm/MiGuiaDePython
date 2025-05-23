def nums():
    a = input("Introduce un numero: ")
    b = input("Introduce otro numero: ")

    if (a.isnumeric() == True and b.isnumeric() == True):
        a = int(a)
        b = int(b)

        if (a > b):
            print(f"{a} es mas grande que {b}")
        elif(b > a):
            print(f"{b} es mas grande que {a}")
        else:
            print("Los numeros son iguales")
    else:
        print("Introduce un numero, anda")

nums()

'''
Fallos que he tenido:
    1. No he convertido a y b a int
    2. He puesto a, b en la función y además estaba pidiendo parametros con input.
'''