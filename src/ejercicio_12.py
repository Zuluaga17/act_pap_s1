n = int(input("Ingrese un número entero: "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(f"Factorial de {n} es {factorial}")
