"""
GUÍA COMPLETA DE BOOLEANOS EN PYTHON

Los booleanos representan valores de verdad: True (Verdadero) y False (Falso)
Son esenciales para el control de flujo en programas.
"""

print("=== FUNDAMENTOS DE BOOLEANOS ===")

# Valores booleanos básicos
verdadero = True
falso = False

print(f"True: {verdadero}")
print(f"False: {falso}")
print(f"Tipo de True: {type(verdadero)}")
print(f"Tipo de False: {type(falso)}")

print("\n=== CONVERSIÓN A BOOLEANO (TRUTHY/FALSY) ===")

# Valores que se evalúan como False (falsy)
falsy_values = [False, None, 0, 0.0, "", [], (), {}, set()]

print("Valores Falsy (se evalúan como False):")
for valor in falsy_values:
    print(f"  bool({repr(valor)}) = {bool(valor)}")

# Valores que se evalúan como True (truthy)
truthy_values = [True, 1, 1.5, "hola", [1, 2], (1, 2), {"a": 1}, {1, 2}]

print("\nValores Truthy (se evalúan como True):")
for valor in truthy_values:
    print(f"  bool({repr(valor)}) = {bool(valor)}")

print("\n=== OPERADORES DE COMPARACIÓN ===")

a, b = 10, 5

print(f"{a} == {b}: {a == b}")  # Igualdad
print(f"{a} != {b}: {a != b}")  # Desigualdad
print(f"{a} > {b}: {a > b}")    # Mayor que
print(f"{a} < {b}: {a < b}")    # Menor que
print(f"{a} >= {b}: {a >= b}")  # Mayor o igual que
print(f"{a} <= {b}: {a <= b}")  # Menor o igual que

print("\n=== OPERADORES LÓGICOS ===")

x, y = True, False

# AND (y) - True solo si ambos son True
print(f"AND: {x} and {y} = {x and y}")

# OR (o) - True si al menos uno es True
print(f"OR: {x} or {y} = {x or y}")

# NOT (no) - Invierte el valor
print(f"NOT: not {x} = {not x}")
print(f"NOT: not {y} = {not y}")

print("\n=== TABLAS DE VERDAD ===")

print("TABLA AND:")
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"False and True = {False and True}")
print(f"False and False = {False and False}")

print("\nTABLA OR:")
print(f"True or True = {True or True}")
print(f"True or False = {True or False}")
print(f"False or True = {False or True}")
print(f"False or False = {False or False}")

print("\nTABLA NOT:")
print(f"not True = {not True}")
print(f"not False = {not False}")

print("\n=== OPERADORES DE IDENTIDAD ===")

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(f"lista1 is lista2: {lista1 is lista2}")  # False (objetos diferentes)
print(f"lista1 is lista3: {lista1 is lista3}")  # True (mismo objeto)
print(f"lista1 is not lista2: {lista1 is not lista2}")  # True

print("\n=== OPERADORES DE PERTENENCIA ===")

fruta = "manzana"
lista_frutas = ["manzana", "naranja", "plátano"]

print(f"'a' in {fruta}: {'a' in fruta}")  # True
print(f"'z' in {fruta}: {'z' in fruta}")  # False
print(f"'manzana' in {lista_frutas}: {'manzana' in lista_frutas}")  # True
print(f"'uva' not in {lista_frutas}: {'uva' not in lista_frutas}")  # True

print("\n=== EVALUACIÓN DE CORTO CIRCUITO ===")

# AND: Si el primero es False, no evalúa el segundo
def funcion_lenta():
    print("  Esta función se ejecutó")
    return True

print("Corto circuito con AND (False and ...):")
resultado = False and funcion_lenta()  # No se ejecuta funcion_lenta

print("Corto circuito con OR (True or ...):")
resultado = True or funcion_lenta()  # No se ejecuta funcion_lenta

print("\n=== FUNCIÓN BOOL() ===")

print("Conversiones con bool():")
print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f"bool(''): {bool('')}")
print(f"bool('hola'): {bool('hola')}")
print(f"bool([]): {bool([])}")
print(f"bool([1, 2]): {bool([1, 2])}")

print("\n=== OPERADORES A NIVEL DE BITS ===")

# Aunque no son estrictamente booleanos, trabajan con bits
a, b = 5, 3  # 5 = 101, 3 = 011 en binario

print(f"{a} & {b} (AND bit a bit): {a & b}")  # 101 & 011 = 001 (1)
print(f"{a} | {b} (OR bit a bit): {a | b}")   # 101 | 011 = 111 (7)
print(f"{a} ^ {b} (XOR bit a bit): {a ^ b}")  # 101 ^ 011 = 110 (6)
print(f"~{a} (NOT bit a bit): {~a}")          # ~00000101 = 11111010 (-6)

print("\n=== BOOLEANOS EN ESTRUCTURAS DE CONTROL ===")

edad = 18
tiene_licencia = True

# IF statement
if edad >= 18 and tiene_licencia:
    print("Puede conducir")
else:
    print("No puede conducir")

# While loop
contador = 3
print("Cuenta regresiva:")
while contador > 0:
    print(f"  {contador}")
    contador -= 1

print("\n=== EXPRESIONES CONDICIONALES (TERNARIAS) ===")

numero = 10
resultado = "par" if numero % 2 == 0 else "impar"
print(f"El número {numero} es {resultado}")

print("\n=== FUNCIONES ALL() Y ANY() ===")

lista_numeros = [1, 2, 3, 0, 5]
print(f"Lista: {lista_numeros}")
print(f"all(): {all(lista_numeros)}")  # False (por el 0)
print(f"any(): {any(lista_numeros)}")  # True (hay elementos truthy)

lista_vacia = []
print(f"\nLista vacía: {lista_vacia}")
print(f"all([]): {all(lista_vacia)}")  # True (caso especial)
print(f"any([]): {any(lista_vacia)}")  # False

print("\n=== PRECEDENCIA DE OPERADORES ===")

# Orden de evaluación: not -> and -> or
resultado1 = True or False and not True
resultado2 = (True or False) and (not True)

print(f"True or False and not True = {resultado1}")
print(f"(True or False) and (not True) = {resultado2}")

print("\n=== BOOLEANOS CON STRINGS ===")

texto = "Python"
print(f"bool('{texto}'): {bool(texto)}")
print(f"'{texto}'.isalpha(): {texto.isalpha()}")
print(f"'{texto}'.isdigit(): {texto.isdigit()}")
print(f"'{texto}'.startswith('P'): {texto.startswith('P')}")
print(f"'{texto}'.endswith('n'): {texto.endswith('n')}")