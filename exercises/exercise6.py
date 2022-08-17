
print(len(lista_01))
# COMPLETAR - FIN
assert len(lista_01) == 4




"""
Extraer el cuarto elemento de la lista
Restricción: Utilizar el método pop
"""

lista = ["ho", "la", 81, 6, 42, "como", "estas?"]

# COMPLETAR - INICIO

elemento_extraido = lista.pop(3)
print("ejercicio2")
print(elemento_extraido)
# COMPLETAR - FIN

assert elemento_extraido == 6


"""
Concatenar las siguientes listas
Restricción: Utilizar el método extend
"""

lista_a = [1, 2, 3]
lista_b = ["4", "5", "6"]
lista_c = ["siete", "ocho", "nueve"]

# COMPLETAR - INICIO
lista_a.extend(lista_b)
lista_a.extend(lista_c)
listas_concatenadas_01 = lista_a
print("ejercicio3")
print(listas_concatenadas_01)

print()

# COMPLETAR - FIN

assert listas_concatenadas_01 == [1, 2, 3, "4", "5", "6", "siete", "ocho", "nueve"]


"""
Agregar la variable variable_01 en la tercer posición de la lista lista_nueva
Restricción: Utilizar el método insert
"""

variable_01 = 2
lista_nueva = [0, 1, 3, 4]

# COMPLETAR - INICIO
lista_nueva.insert(variable_01,2)
print("ejercicio4")
print(lista_nueva)
# COMPLETAR - FIN

assert lista_nueva == [0, 1, 2, 3, 4]


"""
Armar una lista que contenga el primer y el último elemento de la siguiente lista
Restricción: Utilizar el método append junto al indexado simple
"""

lista = ["ho", 3.1416, 42, 81, 6, "la"]

# COMPLETAR - INICIO

print("ejercicio5")
lista_primero_y_ultimo = lista[0:5]
print(lista_primero_y_ultimo)
# COMPLETAR - FIN

assert lista_primero_y_ultimo == ["ho", "la"]


"""
Armar una lista que contenga los primeros 3 elementos de la siguiente lista
Restricción: Utilizar el método append junto al indexado simple
"""

lista = ["ho", 3.1416, "la", 81, 6, 42]

# COMPLETAR - INICIO
print("ejercicio6")
lista_primeros = lista[3:]
print(lista_primeros)
# COMPLETAR - FIN

assert lista_primeros == ["ho", 3.1416, "la"]


"""
Armar una lista que contenga los primeros 3 elementos de la siguiente lista
Restricción: Utilizar indexado múltiple
"""

lista = ["ho", 3.1416, "la", 81, 6, 42]

# COMPLETAR - INICIO
