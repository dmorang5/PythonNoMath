"""numero = 0
while numero < 20:
    print(numero)
    numero += 1"""


import math

numero = int(input("Escriba un número: "))

while numero < 0:
    print("Por favor ingrese un número positivo")
    numero = int(input("Vuelva a ingresar un número positivo: "))

print(f"El resultado de la raíz cuadrada es: {math.sqrt(numero)}")