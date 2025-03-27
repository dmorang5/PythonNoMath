"""data = [6, 8, 9, 4, 7]
for i in data:
    print(f"objeto: {i}")"""


#Ejercicio 
# Crear un programa que muestre la sumatoria de todos lo números entre el 0 y el 100
total = 0
for i in range(101):
    #print(f" El valor de i es: {i}")
    total += i
    #print(f" El total medio es: {total}")

# range = (n-1) -> 0, 1, 2, ..... 100, 101
print(F"La sumatoria final es: {total}")