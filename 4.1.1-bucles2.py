#   Uso de break, continue y pass

count = 0
frase = "Esta es una frase de prueba que estaremos usando para el bucle de esta parte"
letraABuscar = input("Introduce que letra quieres buscar: ")

for letra in frase:
    count = count + 1    
    if (letra == letraABuscar):
        print(f"Letra encontrada en la posición {count}")
        break #    Cuando se llegue a esta parte del código el bucle se parará. 
    else:
        print("Buscando...")