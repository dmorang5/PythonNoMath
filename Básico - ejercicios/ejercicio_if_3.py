nombre1 = input("Nombre 1: ")
nombre2 = input("Nombre 2: ")

if nombre1[0] == nombre2[0] and nombre1[-1] == nombre2[-1]:
    print("Son similares")
elif nombre1[0] == nombre2[0] and nombre1[-1] != nombre2[-1]:
    print("Son similares por la primera letra, mas no por la final")
elif nombre1[0] != nombre2[0] and nombre1[-1] == nombre2[-1]:
    print("Son similares por la última letra, mas no por la primera")
else: 
    print("No coinciden")
   