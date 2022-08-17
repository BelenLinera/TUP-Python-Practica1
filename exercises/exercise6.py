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

assert listas_concatenadas_01 == [1, 2, 3, "4", "5", "6", "siete", …