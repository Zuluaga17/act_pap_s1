import random

numero = random.randint(1, 10)
adivina = int(input("Adivina el número del 1 al 10: "))
while adivina != numero:
    adivina = int(input("Incorrecto, intenta otra vez: "))
print("¡Felicidades! Adivinaste el número.")
