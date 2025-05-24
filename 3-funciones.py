#   Definir una función. 
def saludar():
    print("Hola, ¿qué tal?")

#   Para llamar a la función previamente definida la tenemos que llamar de esta forma
saludar()

#   Funciones con argumentos
nombre = input("Introduce tu nombre: ")

def saludarDos(nombre):
    print(f"Hola {nombre}, ¿como estás?")

saludarDos(nombre)

#   Funciones con retorno
def suma(a, b):
    resultado = a + b
    return resultado

print(suma(10, 15))

#   Funciones que retornan varios valores

def sumaYResta(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

print(sumaYResta(15, 5))
#   La respuesta a este código será (20, 10), ya que en el return tenemos suma, resta.