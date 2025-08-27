"""
MÉTODOS Y OPERACIONES CON SETS EN PYTHON

Los sets son colecciones desordenadas de elementos únicos.
No permiten duplicados y son mutables (excepto frozenset).
"""

print("=== CREACIÓN DE SETS ===")

# Set vacío
set_vacio = set()
print(f"Set vacío: {set_vacio}")

# Set con elementos
set_numeros = {1, 2, 3, 4, 5}
print(f"Set con números: {set_numeros}")

# Set desde una lista (elimina duplicados)
lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 5]
set_desde_lista = set(lista_con_duplicados)
print(f"Set desde lista: {set_desde_lista}")

# Set con diferentes tipos de datos
set_mixto = {1, "hola", 3.14, True}
print(f"Set mixto: {set_mixto}")

print("\n=== MÉTODOS DE AGREGADO ===")

mi_set = {1, 2, 3}

# add() - Agrega un elemento
mi_set.add(4)
print(f"add(4): {mi_set}")

# update() - Agrega múltiples elementos
mi_set.update([5, 6, 7])
print(f"update([5, 6, 7]): {mi_set}")

mi_set.update({8, 9}, {10, 11})
print(f"update({{8, 9}}, {{10, 11}}): {mi_set}")

print("\n=== MÉTODOS DE ELIMINACIÓN ===")

mi_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# remove() - Elimina elemento (error si no existe)
mi_set.remove(5)
print(f"remove(5): {mi_set}")

# discard() - Elimina elemento (no error si no existe)
mi_set.discard(15)  # No existe, pero no da error
print(f"discard(15): {mi_set}")

# pop() - Elimina y retorna un elemento aleatorio
elemento = mi_set.pop()
print(f"pop(): elemento={elemento}, set={mi_set}")

# clear() - Vacía el set
mi_set.clear()
print(f"clear(): {mi_set}")

print("\n=== MÉTODOS DE CONSULTA ===")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# union() - Unión de sets
union = set_a.union(set_b)
print(f"union(): {union}")

# intersection() - Intersección
interseccion = set_a.intersection(set_b)
print(f"intersection(): {interseccion}")

# difference() - Diferencia
diferencia = set_a.difference(set_b)
print(f"difference(): {diferencia}")

# symmetric_difference() - Diferencia simétrica
diff_simetrica = set_a.symmetric_difference(set_b)
print(f"symmetric_difference(): {diff_simetrica}")

print("\n=== MÉTODOS BOOLEANOS ===")

set_x = {1, 2, 3}
set_y = {1, 2}
set_z = {4, 5}

# issubset() - Verifica si es subconjunto
print(f"issubset(): {set_y.issubset(set_x)}")  # True

# issuperset() - Verifica si es superconjunto
print(f"issuperset(): {set_x.issuperset(set_y)}")  # True

# isdisjoint() - Verifica si no hay elementos en común
print(f"isdisjoint(): {set_x.isdisjoint(set_z)}")  # True

print("\n=== OPERADORES DE SETS ===")

a = {1, 2, 3}
b = {3, 4, 5}

# Unión con |
print(f"Unión (|): {a | b}")

# Intersección con &
print(f"Intersección (&): {a & b}")

# Diferencia con -
print(f"Diferencia (-): {a - b}")

# Diferencia simétrica con ^
print(f"Diferencia simétrica (^): {a ^ b}")

print("\n=== MÉTODOS DE COPIA ===")

original = {1, 2, 3}

# copy() - Copia superficial
copia = original.copy()
print(f"copy(): {copia}")

print("\n=== FROZENSET (SET INMUTABLE) ===")

# frozenset - Set inmutable
frozen = frozenset([1, 2, 3, 4, 5])
print(f"frozenset: {frozen}")
print(f"Tipo: {type(frozen)}")

print("\n=== MÉTODOS DE ITERACIÓN ===")

mi_set = {'a', 'b', 'c', 'd'}

# Iteración básica
print("Iteración:")
for elemento in mi_set:
    print(f"  {elemento}")

# Verificar existencia
print(f"'a' in mi_set: {'a' in mi_set}")

print("\n=== FUNCIONES INTEGRADAS ===")

numeros = {5, 2, 8, 1, 9}

print(f"len(numeros): {len(numeros)}")
print(f"max(numeros): {max(numeros)}")
print(f"min(numeros): {min(numeros)}")
print(f"sum(numeros): {sum(numeros)}")
print(f"sorted(numeros): {sorted(numeros)}")

print("\n=== COMPREHENSION DE SETS ===")

# Set comprehension
cuadrados = {x**2 for x in range(1, 6)}
print(f"Cuadrados: {cuadrados}")

pares = {x for x in range(10) if x % 2 == 0}
print(f"Pares: {pares}")