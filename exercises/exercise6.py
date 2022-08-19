
"""Listas"""

"""
Inicializar una lista vacía y luego agregarle 4 elementos cualquiera
Restricción: Utilizar el método append
"""

# COMPLETAR - INICIO
lista_01 = []
lista_01.append(1)
lista_01.append(1)
lista_01.append(1)
lista_01.append(1)
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
lista_primero_y_ultimo = []
lista_primero_y_ultimo.append(lista[0])
lista_primero_y_ultimo.append(lista[-1])
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
lista_primeros = []
lista_primeros.append(lista[0])
lista_primeros.append(lista[1])
lista_primeros.append(lista[2])
# COMPLETAR - FIN

assert lista_primeros == ["ho", 3.1416, "la"]


"""
Armar una lista que contenga los primeros 3 elementos de la siguiente lista
Restricción: Utilizar indexado múltiple
"""

lista = ["ho", 3.1416, "la", 81, 6, 42]
print("Ejercicio7: ")
lista_primeros = lista[0:3]
print(lista_primeros)
assert lista_primeros == ["ho", 3.1416, "la"]
# COMPLETAR - INICIO

"""
Armar una lista que contenga los primeros 2 y los últimos 2 elementos de la
siguiente lista
Restricción: Utilizar el método extend junto al indexado múltiple
"""

lista = ["ho", "la", 81, 6, 42, "como", "estas?"]

# COMPLETAR - INICIO
lista_a = lista[0:2]
lista_a.extend(lista[5:])
lista_primeros_y_ultimos = lista_a
print("Ejercicio8: ")
print(lista_primeros_y_ultimos)
# COMPLETAR - FIN

assert lista_primeros_y_ultimos == ["ho", "la", "como", "estas?"]


"""
Concatenar las siguientes 2 listas
Restricción: Utiliar el operador +
"""

lista_01 = [0, 1, 2, 3]
lista_02 = [5, 6]

# COMPLETAR - INICIO
lista_concatenada = lista_01 + lista_02
print("Ejercicio9: ")
print(lista_concatenada)
# COMPLETAR - FIN

assert lista_concatenada == [0, 1, 2, 3, 5, 6]


"""
Concatenar 3 veces la siguiente lista consigo misma
Restricción: Utiliar el operador *
"""

lista_01 = [0, 1, 0, 1, 0, 1]

# COMPLETAR - INICIO
lista_duplicada = lista_01 *3
print("Ejercicio10: ")
print(lista_duplicada)
# COMPLETAR - FIN

assert lista_duplicada == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]


"""
Verificar si el siguiente elemento pertenece a la lista
Restricción: Utiliar el operador in
"""

elemento = 1.0
lista = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1.0, 1, 0, 1, 0, 1]

# COMPLETAR - INICIO
variable_booleana = elemento in lista
print("Ejercicio11: ")
print(variable_booleana)
# COMPLETAR - FIN

assert variable_booleana


"""
Verificar si las siguientes listas son iguales
Restricción: Utilizar el operador ==
"""

lista_01 = [1, 2, 3, 4.5, 6, 7]
lista_02 = [1, 3, 2, 4, 5, 6, 7]

# COMPLETAR - INICIO
son_iguales = lista_01 == lista_02
print("Ejercicio12: ")
print(son_iguales)
# COMPLETAR - FIN

assert not son_iguales


"""
Se cuenta con una lista de elementos booleanos que corresponden a las notas de los exámenes
cuatrimestrales de un alumno (True si está aprobado y False en caso contrario)
Determinar si el alumno no tiene examenes aprobados.
Restricción: Utilizar el método any
"""

notas = [False, False, False, False, False, False, False, False, False]

# COMPLETAR - INICIO
no_tiene_examenes_aprobados = not any(notas)
print("Ejercicio13: ")
print(no_tiene_examenes_aprobados)
# COMPLETAR - FIN

assert no_tiene_examenes_aprobados


"""
Se cuenta con una lista de elementos booleanos que corresponden a las notas de los exámenes
cuatrimestrales de un alumno (True si está aprobado y False en caso contrario)
Determinar si el alumno ha aprobado todos sus exámenes.
Restricción: Utilizar el método all
"""

notas = [True, True, False, True, True, True, True, True, True, True, True, True]

# COMPLETAR - INICIO
print("Ejercicio14: ")
tiene_todo_aprobado = all(notas)

# COMPLETAR - FIN
