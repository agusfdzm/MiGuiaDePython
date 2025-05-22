#   Pedir al usuario que introduzca un dato. Como read -p de bash. Para poder manejar este dato lo quer haremos será meterlo en una variable. 
nombre= input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")

#   Si ahora queremos mostrar un mensaje que diga el nombre y la edad del usuario lo tendremos que hacer de esta manera con un fstring.
print(f"Tu nombre es {nombre} y tienes {edad} años")


#   Para ver el tipo de dato de una variable usaremos la siguiente función.
tipoDeEdad = type(edad)
print(tipoDeEdad)

#   IFs y BOOLEANOS
verdadero = True
falso = False 
#   Solo hay 2 tipos de booleanos.

if (verdadero == True):
    print("Es verdadero")

if (verdadero == False):
    print ("Es verdadero (?")
else:
    print("Es falso!!")

#   Para pasar a entero un valor string usaremos la función int() de esta manera
edad = int(edad)
print(type(edad))