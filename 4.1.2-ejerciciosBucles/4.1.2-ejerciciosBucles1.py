#   Contador de letras y uso de continue

frase = "ana ama a amanda, la dama catalana que nada en agua salada"
buscador = input("Introduce la letra que quieres buscar: ")

contador = 0

for letra in frase:
    if (letra == buscador):
        contador = contador + 1
        print (f"Has encontrado {contador} letra/s")
        continue #  Vuelve a empezar el bucle y no se ejecuta el código restante
    else:
        print ("Buscando...")