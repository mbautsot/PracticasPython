"""
GUÍA COMPLETA DEL BUCLE FOR EN PYTHON
"""

print("=" * 60)
print("GUÍA COMPLETA DEL BUCLE FOR EN PYTHON")
print("=" * 60)

print("\n" + "=" * 40)
print("1. SINTAXIS BÁSICA DEL FOR")
print("=" * 40)

# Sintaxis básica
print("👉 ITERACIÓN SOBRE LISTA:")
frutas = ["manzana", "banana", "naranja", "uva"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")

print("\n👉 ITERACIÓN SOBRE STRING:")
palabra = "Python"
for letra in palabra:
    print(letra)

print("\n👉 ITERACIÓN SOBRE TUPLA:")
coordenadas = (10, 20, 30)
for coord in coordenadas:
    print(f"Coordenada: {coord}")

print("\n" + "=" * 40)
print("2. FUNCIÓN RANGE()")
print("=" * 40)

# Range con un argumento (0 a n-1)
print("👉 RANGE(5):")
for i in range(5):
    print(i)

# Range con dos argumentos (start, stop)
print("\n👉 RANGE(2, 7):")
for i in range(2, 7):
    print(i)

# Range con tres argumentos (start, stop, step)
print("\n👉 RANGE(1, 10, 2):")
for i in range(1, 10, 2):
    print(i)

# Range descendente
print("\n👉 RANGE(10, 0, -1):")
for i in range(10, 0, -1):
    print(i)

print("\n" + "=" * 40)
print("3. ENUMERATE() - OBTENER ÍNDICE Y VALOR")
print("=" * 40)

# Enumerate básico
print("👉 ENUMERATE BÁSICO:")
frutas = ["manzana", "banana", "naranja"]
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")

# Enumerate con start personalizado
print("\n👉 ENUMERATE CON START:")
for indice, fruta in enumerate(frutas, start=1):
    print(f"Fruta #{indice}: {fruta}")

print("\n" + "=" * 40)
print("4. ZIP() - ITERAR MÚLTIPLES ITERABLES")
print("=" * 40)

# Zip básico
print("👉 ZIP BÁSICO:")
nombres = ["Ana", "Juan", "María"]
edades = [25, 30, 28]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

# Zip con tres iterables
print("\n👉 ZIP CON TRES ITERABLES:")
ciudades = ["Madrid", "Barcelona", "Valencia"]
for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"{nombre} ({edad} años) vive en {ciudad}")

print("\n" + "=" * 40)
print("5. ITERACIÓN SOBRE DICCIONARIOS")
print("=" * 40)

persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

print("👉 ITERAR SOBRE KEYS:")
for key in persona:
    print(f"Key: {key}")

print("\n👉 ITERAR SOBRE VALUES:")
for value in persona.values():
    print(f"Value: {value}")

print("\n👉 ITERAR SOBRE ITEMS (KEY-VALUE):")
for key, value in persona.items():
    print(f"{key}: {value}")

print("\n" + "=" * 40)
print("6. BREAK, CONTINUE Y PASS")
print("=" * 40)

# Break - salir del bucle
print("👉 BREAK - SALIR DEL BUCLE:")
for i in range(10):
    if i == 5:
        print("Encontrado 5, saliendo...")
        break
    print(i)

# Continue - saltar iteración
print("\n👉 CONTINUE - SALTAR ITERACIÓN:")
for i in range(10):
    if i % 2 == 0:
        continue  # Saltar números pares
    print(i)

# Pass - placeholder
print("\n👉 PASS - PLACEHOLDER:")
for i in range(5):
    if i == 2:
        pass  # Para implementar después
    else:
        print(i)

print("\n" + "=" * 40)
print("7. ELSE EN BUCLES FOR")
print("=" * 40)

# Else se ejecuta si no hubo break
print("👉 ELSE SIN BREAK:")
for i in range(3):
    print(i)
else:
    print("Bucle completado sin break")

print("\n👉 ELSE CON BREAK:")
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("Esto no se ejecutará por el break")

print("\n" + "=" * 40)
print("8. BUCLES FOR ANIDADOS")
print("=" * 40)

# Tablas de multiplicar
print("👉 TABLAS DE MULTIPLICAR:")
for i in range(1, 4):
    print(f"\nTabla del {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

# Patrones
print("\n👉 PATRÓN DE ASTERISCOS:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n" + "=" * 40)
print("9. COMPREHENSION DE LISTAS")
print("=" * 40)

# List comprehension básica
print("👉 LIST COMPREHENSION BÁSICA:")
cuadrados = [x**2 for x in range(1, 6)]
print(f"Cuadrados: {cuadrados}")

# Con condición
print("\n👉 CON CONDICIÓN:")
pares = [x for x in range(1, 11) if x % 2 == 0]
print(f"Pares: {pares}")

# Con if-else
print("\n👉 CON IF-ELSE:")
clasificacion = ["Par" if x % 2 == 0 else "Impar" for x in range(1, 6)]
print(f"Clasificación: {clasificacion}")

print("\n" + "=" * 40)
print("10. EJEMPLOS PRÁCTICOS")
print("=" * 40)

# Contador de vocales
print("👉 CONTADOR DE VOCALES:")
texto = "Python programming"
vocales = "aeiouAEIOU"
contador = 0

for letra in texto:
    if letra in vocales:
        contador += 1

print(f"El texto tiene {contador} vocales")

# Buscar elemento
print("\n👉 BUSCAR ELEMENTO:")
numeros = [1, 3, 5, 7, 9, 2, 4, 6, 8]
encontrado = False

for num in numeros:
    if num % 2 == 0:
        print(f"Primer número par encontrado: {num}")
        encontrado = True
        break

if not encontrado:
    print("No se encontraron números pares")

# Suma de elementos
print("\n👉 SUMA DE ELEMENTOS:")
numeros = [1, 2, 3, 4, 5]
suma = 0

for num in numeros:
    suma += num

print(f"Suma: {suma}")

print("\n" + "=" * 40)
print("11. ITERACIÓN SOBRE ARCHIVOS")
print("=" * 40)

# Leer archivo línea por línea
print("👉 LEER ARCHIVO (ejemplo simulado):")
lineas = ["Línea 1: Hola", "Línea 2: Mundo", "Línea 3: Python"]

for numero_linea, linea in enumerate(lineas, 1):
    print(f"Línea {numero_linea}: {linea}")

print("\n" + "=" * 40)
print("12. TÉCNICAS AVANZADAS")
print("=" * 40)

# Iteración reversa
print("👉 ITERACIÓN REVERSA:")
for i in reversed(range(5)):
    print(i)

# Iteración ordenada
print("\n👉 ITERACIÓN ORDENADA:")
numeros = [3, 1, 4, 1, 5, 9, 2]
for num in sorted(numeros):
    print(num)

# Iteración sobre conjunto único
print("\n👉 ITERACIÓN SOBRE VALORES ÚNICOS:")
for num in sorted(set(numeros)):
    print(num)