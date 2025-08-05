edad = int(input("Ingrese una edad (-1 para terminar): "))
mayor = None

while edad != -1:
    if mayor is None or edad > mayor:
        mayor = edad
    edad = int(input("Ingrese una edad (-1 para terminar): "))

if mayor is not None:
    print("La edad mayor ingresada es:", mayor)
else:
    print("No se ingresaron edades válidas.")
