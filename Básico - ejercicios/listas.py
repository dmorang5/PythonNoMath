# Listas: corchetes -> [obj, obj2, obj3]

array = ["futbol", "PC", 18.6, 18, [6,7,10.4], True, False, "PC"]
print(array)

print(array[-1])

"append: añadir al final"

array.append(66)
print(array)

#insert: añadir en un lugar/indice

array.insert(1, 88) # lugar y que dato insertar
print(array)

#extend: añadir varios pero al final
array.extend([12, 8, 1])
print(array)


# concatenar listas
array2 = [100, 150, "hola"]
array3 = array + array2
print(array3)


# buscar
print("PC" in array) # responde true o false

# saber ubicacion 
print(array.index("PC"))

# la cantidad de veces que se repite un dato
print(array.count("PC"))

#remove: eliminar datos

array.remove("PC")
print(array)

#reverse: cambiar posi de datos

array.reverse()
print(array)

# sort: ordena de menor a mayor
arrayor = [2, 5, 1, -1]
arrayor.sort()
print(arrayor)

# sort: ordena de mayor a menor
arrayor = [2, 5, 1, -1]
arrayor.sort(reverse=True)
print(arrayor)
