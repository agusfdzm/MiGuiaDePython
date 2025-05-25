'''
El usuario debe adivinar un numero entre 0 y 10.
El programa deberá pedir que el usuario introduzca un número y debe decir si ha acertado, si el número a adivinar es menor o mayor que el que ya ha introducido
'''

numero = 6
intento = input("Intenta adivinar el numero: ")
intento = int(intento)

while (intento != numero):
    if (intento > numero):
        print("El numero que tienes que adivinar es mas pequeño")
    elif (intento < numero):
        print("El numero que tienes que adivinar es mas grande")
    intento = input("Intenta adivinar el numero: ")
    intento = int(intento)
else:
    print("Enhorabuena! Has adivinado el numero")