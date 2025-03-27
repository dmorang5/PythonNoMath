num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("ingrese un tercer número: "))

if num1 >= num2 and num1 >= 3:
    print(f"El primer número {num1} es mayor que {num2} y {num3}")
elif num2 >= num1 and num2 >= num3:
    print(f"El segundo número {num2} es mayor que {num1} y {num3}")
else:
    print(f"El tercer número {num3} es mayor que {num2} y {num1}")


    