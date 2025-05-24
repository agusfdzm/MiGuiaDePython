#   Listas. Las posiciones de las listas van desde el 0 hasta la posición LONGITUD -1   
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros[4]

#   La función len() sirve para ver cuantos elementos hay en una lista
print(len(numeros))


#   Bucles: For
for i in range(11):
    print(i)

#   Para especificar el incremento en cada iteración tendremos que hacer esto. Ejemplo iteración de +2
for i in range(1, 101, 2):
    print(i)

#   Imprimir solo las vocales de una palabra con for
#   Siempre iteremos una variable que sea una palabra recorreremos todos los caracteres de esta
palabra = "cocodrilo"
for letra in palabra:
    if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        print(letra)

digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


for numero in digitos:
    if (numero % 2 == 0):
        print(numero)
    else:
        print("impar")

#   Bucles: while
contador = 0

while (contador <= 10):
    print (contador)
    contador += 1

lista = ["juan", "pepe", "manolo", "francisco", "paco"]

count = 0

while (count < len(lista)):
    print(lista[count])
    count += 1