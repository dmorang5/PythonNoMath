num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

if num1 %2 == 0 and num2 % 2 == 0:
    print("Ambos par")
elif num1 %2 == 0 and num2 % 2 != 0:
    print(f"{num1} es par")
elif num1 %2 != 0 and num2 % 2 == 0:
    print(f"{num2} es par")
else: 
    print("Ambos impar")
