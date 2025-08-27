"""
MÉTODOS Y OPERACIONES CON TUPLES EN PYTHON

Los tuples son estructuras de datos inmutables y ordenadas.
Ventajas: más rápidos que las listas, seguros para datos constantes.
"""

# ========== CREACIÓN DE TUPLES ==========
print("=== CREACIÓN DE TUPLES ===")

# Tuple vacío
tuple_vacio = ()
print(f"Tuple vacío: {tuple_vacio}")

# Tuple con un elemento (necesita coma)
tuple_un_elemento = (42,)
print(f"Tuple con un elemento: {tuple_un_elemento}")

# Tuple múltiple
tuple_multiple = (1, 2, 3, 4, 5)
print(f"Tuple múltiple: {tuple_multiple}")

# Tuple sin paréntesis (tuple packing)
tuple_sin_parentesis = 1, 2, 3, 4, 5
print(f"Tuple sin paréntesis: {tuple_sin_parentesis}")

# Tuple desde una lista
lista = [1, 2, 3]
tuple_desde_lista = tuple(lista)
print(f"Tuple desde lista: {tuple_desde_lista}")

# ========== MÉTODOS PRINCIPALES ==========
print("\n=== MÉTODOS PRINCIPALES ===")

mi_tuple = (1, 2, 3, 2, 4, 2, 5)

# 1. count() - Cuenta ocurrencias de un elemento
print(f"count(2): {mi_tuple.count(2)}")  # Output: 3

# 2. index() - Devuelve el índice de la primera ocurrencia
print(f"index(4): {mi_tuple.index(4)}")  # Output: 4

# ========== OPERACIONES COMUNES ==========
print("\n=== OPERACIONES COMUNES ===")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenación
concatenado = tuple1 + tuple2
print(f"Concatenación: {concatenado}")

# Repetición
repetido = tuple1 * 3
print(f"Repetición: {repetido}")

# Acceso por índice
print(f"tuple1[0]: {tuple1[0]}")  # Primer elemento
print(f"tuple1[-1]: {tuple1[-1]}")  # Último elemento

# Slicing
print(f"tuple1[1:3]: {tuple1[1:3]}")  # Elementos 1 y 2

# ========== MÉTODOS DE CONVERSIÓN ==========
print("\n=== MÉTODOS DE CONVERSIÓN ===")

# Tuple a lista
tuple_original = (1, 2, 3)
lista_desde_tuple = list(tuple_original)
print(f"Tuple a lista: {lista_desde_tuple}")

# Tuple a string (si todos son strings)
tuple_strings = ('H', 'o', 'l', 'a')
string_desde_tuple = ''.join(tuple_strings)
print(f"Tuple a string: {string_desde_tuple}")

# ========== OPERADORES DE COMPARACIÓN ==========
print("\n=== OPERADORES DE COMPARACIÓN ===")

a = (1, 2, 3)
b = (1, 2, 4)
c = (1, 2, 3)

print(f"a == c: {a == c}")  # True
print(f"a != b: {a != b}")  # True
print(f"a < b: {a < b}")    # True (comparación lexicográfica)

# ========== MÉTODOS DE ITERACIÓN ==========
print("\n=== MÉTODOS DE ITERACIÓN ===")

# Iteración básica
print("Iteración:")
for elemento in tuple1:
    print(f"  {elemento}")

# Iteración con enumerate
print("Iteración con índice:")
for indice, elemento in enumerate(tuple1):
    print(f"  Índice {indice}: {elemento}")

# ========== UNPACKING ==========
print("\n=== UNPACKING ===")

coordenadas = (10, 20, 30)
x, y, z = coordenadas
print(f"Unpacking: x={x}, y={y}, z={z}")

# Unpacking parcial
primero, *resto = (1, 2, 3, 4, 5)
print(f"Unpacking parcial: primero={primero}, resto={resto}")

# ========== FUNCIONES INTEGRADAS ==========
print("\n=== FUNCIONES INTEGRADAS ===")

numeros = (5, 2, 8, 1, 9)

print(f"len(numeros): {len(numeros)}")
print(f"max(numeros): {max(numeros)}")
print(f"min(numeros): {min(numeros)}")
print(f"sum(numeros): {sum(numeros)}")
print(f"sorted(numeros): {sorted(numeros)}")

# ========== TUPLES ANIDADOS ==========
print("\n=== TUPLES ANIDADOS ===")

matriz = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(f"Matriz: {matriz}")
print(f"Elemento [1][2]: {matriz[1][2]}")  # Output: 6

# ========== MÉTODOS AVANZADOS ==========
print("\n=== MÉTODOS AVANZADOS ===")

# any() - True si algún elemento es True
print(f"any((False, False, True)): {any((False, False, True))}")

# all() - True si todos los elementos son True
print(f"all((True, True, False)): {all((True, True, False))}")

# zip() - Combinar múltiples tuples
nombres = ('Ana', 'Juan', 'María')
edades = (25, 30, 28)
combinado = tuple(zip(nombres, edades))
print(f"Combinado: {combinado}")