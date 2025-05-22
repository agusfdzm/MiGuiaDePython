nota = float(input("Introduce tu nota (0-10): "))

if nota < 0 or nota > 10:
    print("Nota no válida. Debe estar entre 0 y 10.")
elif nota < 5:
    print("Suspenso")
elif nota < 7:
    print("Aprobado")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")