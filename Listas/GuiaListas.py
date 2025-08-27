# =============================================
# LISTAS EN PYTHON - GUÍA COMPLETA
# =============================================

print("=" * 60)
print("LISTAS EN PYTHON - MÉTODOS Y OPERACIONES")
print("=" * 60)

# =============================================
# 1. ¿QUÉ SON LAS LISTAS?
# =============================================

print("\n" + "=" * 30)
print("1. ¿QUÉ SON LAS LISTAS?")
print("=" * 30)

"""
Las listas son:
- Colecciones ordenadas y mutables de elementos
- Pueden contener diferentes tipos de datos
- Se definen con corchetes []
- Los elementos se separan por comas
"""

# Creación de listas
lista_vacia = []
lista_numeros = [1, 2, 3, 4, 5]
lista_mixta = [1, "hola", 3.14, True, [1, 2, 3]]
lista_frutas = ["manzana", "banana", "naranja", "uva"]

print("📦 Lista vacía:", lista_vacia)
print("🔢 Lista de números:", lista_numeros)
print("🎭 Lista mixta:", lista_mixta)
print("🍎 Lista de frutas:", lista_frutas)

# =============================================
# 2. ACCESO A ELEMENTOS
# =============================================

print("\n" + "=" * 30)
print("2. ACCESO A ELEMENTOS")
print("=" * 30)

# Indexación positiva (0-based)
print("Primer elemento:", lista_frutas[0])      # manzana
print("Segundo elemento:", lista_frutas[1])     # banana
print("Tercer elemento:", lista_frutas[2])      # naranja

# Indexación negativa (desde el final)
print("Último elemento:", lista_frutas[-1])     # uva
print("Penúltimo elemento:", lista_frutas[-2])  # naranja

# Slicing (rebanado)
print("Primeros 2 elementos:", lista_frutas[0:2])    # ['manzana', 'banana']
print("Desde índice 1:", lista_frutas[1:])           # ['banana', 'naranja', 'uva']
print("Últimos 2 elementos:", lista_frutas[-2:])     # ['naranja', 'uva']
print("Copia de lista:", lista_frutas[:])            # Copia completa

# =============================================
# 3. MÉTODOS DE MODIFICACIÓN
# =============================================

print("\n" + "=" * 30)
print("3. MÉTODOS DE MODIFICACIÓN")
print("=" * 30)

# ---------------------------------------------------
# 3.1 append() - Agrega elemento al final
# ---------------------------------------------------
print("\n3.1 append() - Agrega al final:")
frutas = ["manzana", "banana"]
print("Antes:", frutas)
frutas.append("naranja")
print("Después de append('naranja'):", frutas)

# ---------------------------------------------------
# 3.2 extend() - Extiende con otra lista
# ---------------------------------------------------
print("\n3.2 extend() - Extiende lista:")
verduras = ["zanahoria", "espinaca"]
print("Lista 1:", frutas)
print("Lista 2:", verduras)
frutas.extend(verduras)
print("Después de extend(verduras):", frutas)

# ---------------------------------------------------
# 3.3 insert() - Inserta en posición específica
# ---------------------------------------------------
print("\n3.3 insert() - Inserta en posición:")
print("Antes:", frutas)
frutas.insert(1, "uva")  # Inserta en índice 1
print("Después de insert(1, 'uva'):", frutas)

# ---------------------------------------------------
# 3.4 remove() - Remueve primera ocurrencia
# ---------------------------------------------------
print("\n3.4 remove() - Remueve elemento:")
print("Antes:", frutas)
frutas.remove("banana")  # Remueve 'banana'
print("Después de remove('banana'):", frutas)

# ---------------------------------------------------
# 3.5 pop() - Remueve y retorna elemento
# ---------------------------------------------------
print("\n3.5 pop() - Remueve y retorna:")
print("Antes:", frutas)
elemento_eliminado = frutas.pop()  # Remueve el último
print("Elemento eliminado:", elemento_eliminado)
print("Después de pop():", frutas)

elemento_eliminado2 = frutas.pop(1)  # Remueve índice 1
print("Elemento eliminado (índice 1):", elemento_eliminado2)
print("Después de pop(1):", frutas)

# ---------------------------------------------------
# 3.6 clear() - Limpia toda la lista
# ---------------------------------------------------
print("\n3.6 clear() - Limpia lista:")
lista_temporal = [1, 2, 3, 4, 5]
print("Antes:", lista_temporal)
lista_temporal.clear()
print("Después de clear():", lista_temporal)

# ---------------------------------------------------
# 3.7 del - Elimina por índice
# ---------------------------------------------------
print("\n3.7 del - Elimina por índice:")
numeros = [10, 20, 30, 40, 50]
print("Antes:", numeros)
del numeros[2]  # Elimina índice 2 (30)
print("Después de del numeros[2]:", numeros)

# =============================================
# 4. MÉTODOS DE BÚSQUEDA
# =============================================

print("\n" + "=" * 30)
print("4. MÉTODOS DE BÚSQUEDA")
print("=" * 30)

lista_busqueda = ["a", "b", "c", "a", "d", "b", "e"]

# ---------------------------------------------------
# 4.1 index() - Encuentra índice de elemento
# ---------------------------------------------------
print("\n4.1 index() - Encuentra índice:")
print("Lista:", lista_busqueda)
print("Índice de 'c':", lista_busqueda.index("c"))
print("Índice de 'a' (después de índice 1):", lista_busqueda.index("a", 1))

# ---------------------------------------------------
# 4.2 count() - Cuenta ocurrencias
# ---------------------------------------------------
print("\n4.2 count() - Cuenta ocurrencias:")
print("Lista:", lista_busqueda)
print("Count de 'a':", lista_busqueda.count("a"))
print("Count de 'b':", lista_busqueda.count("b"))
print("Count de 'x':", lista_busqueda.count("x"))  # No existe

# ---------------------------------------------------
# 4.3 in - Verifica existencia
# ---------------------------------------------------
print("\n4.3 in - Verifica existencia:")
print("'c' está en lista:", "c" in lista_busqueda)
print("'z' está en lista:", "z" in lista_busqueda)

# =============================================
# 5. MÉTODOS DE ORDENAMIENTO
# =============================================

print("\n" + "=" * 30)
print("5. MÉTODOS DE ORDENAMIENTO")
print("=" * 30)

# ---------------------------------------------------
# 5.1 sort() - Ordena la lista
# ---------------------------------------------------
print("\n5.1 sort() - Ordena lista:")
numeros_desordenados = [3, 1, 4, 1, 5, 9, 2, 6]
print("Antes:", numeros_desordenados)
numeros_desordenados.sort()
print("Después de sort():", numeros_desordenados)

# Sort descendente
numeros_desordenados.sort(reverse=True)
print("Sort reverse=True:", numeros_desordenados)

# Sort con strings
frutas_desordenadas = ["naranja", "manzana", "banana", "uva"]
frutas_desordenadas.sort()
print("Frutas ordenadas:", frutas_desordenadas)

# ---------------------------------------------------
# 5.2 reverse() - Invierte la lista
# ---------------------------------------------------
print("\n5.2 reverse() - Invierte lista:")
lista_normal = [1, 2, 3, 4, 5]
print("Antes:", lista_normal)
lista_normal.reverse()
print("Después de reverse():", lista_normal)

# ---------------------------------------------------
# 5.3 sorted() - Función que retorna lista ordenada
# ---------------------------------------------------
print("\n5.3 sorted() - Retorna lista ordenada:")
original = [3, 1, 4, 2]
ordenada = sorted(original)
print("Original:", original)
print("Ordenada:", ordenada)
print("Original no modificada:", original)

# =============================================
# 6. MÉTODOS DE COPIA
# =============================================

print("\n" + "=" * 30)
print("6. MÉTODOS DE COPIA")
print("=" * 30)

# ---------------------------------------------------
# 6.1 copy() - Copia superficial
# ---------------------------------------------------
print("\n6.1 copy() - Copia superficial:")
original = [1, 2, 3, [4, 5]]
copia = original.copy()
print("Original:", original)
print("Copia:", copia)

# Modificamos la copia
copia[0] = 99
copia[3][0] = 88  # Esto afecta a ambas listas
print("Después de modificar copia:")
print("Original:", original)  # [1, 2, 3, [88, 5]]
print("Copia:", copia)        # [99, 2, 3, [88, 5]]

# ---------------------------------------------------
# 6.2 copy.deepcopy() - Copia profunda
# ---------------------------------------------------
print("\n6.2 copy.deepcopy() - Copia profunda:")
import copy
original = [1, 2, 3, [4, 5]]
copia_profunda = copy.deepcopy(original)

copia_profunda[3][0] = 888
print("Original:", original)       # [1, 2, 3, [4, 5]]
print("Copia profunda:", copia_profunda)  # [1, 2, 3, [888, 5]]

# =============================================
# 7. OPERACIONES CON LISTAS
# =============================================

print("\n" + "=" * 30)
print("7. OPERACIONES CON LISTAS")
print("=" * 30)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# ---------------------------------------------------
# 7.1 Concatenación (+)
# ---------------------------------------------------
print("\n7.1 Concatenación (+):")
concatenada = lista1 + lista2
print(f"{lista1} + {lista2} = {concatenada}")

# ---------------------------------------------------
# 7.2 Repetición (*)
# ---------------------------------------------------
print("\n7.2 Repetición (*):")
repetida = lista1 * 3
print(f"{lista1} * 3 = {repetida}")

# ---------------------------------------------------
# 7.3 Longitud (len())
# ---------------------------------------------------
print("\n7.3 Longitud (len()):")
print(f"Longitud de {lista1}: {len(lista1)}")
print(f"Longitud de {concatenada}: {len(concatenada)}")

# ---------------------------------------------------
# 7.4 Mínimo y máximo
# ---------------------------------------------------
print("\n7.4 Mínimo y máximo:")
numeros = [10, 5, 20, 3, 15]
print(f"Lista: {numeros}")
print(f"Mínimo: {min(numeros)}")
print(f"Máximo: {max(numeros)}")

# ---------------------------------------------------
# 7.5 Suma
# ---------------------------------------------------
print("\n7.5 Suma:")
print(f"Suma de {numeros}: {sum(numeros)}")

# =============================================
# 8. LISTAS POR COMPRENSIÓN
# =============================================

print("\n" + "=" * 30)
print("8. LISTAS POR COMPRENSIÓN")
print("=" * 30)

# ---------------------------------------------------
# 8.1 Comprensión básica
# ---------------------------------------------------
print("\n8.1 Comprensión básica:")
cuadrados = [x**2 for x in range(1, 6)]
print(f"Cuadrados del 1-5: {cuadrados}")

# ---------------------------------------------------
# 8.2 Comprensión con condición
# ---------------------------------------------------
print("\n8.2 Comprensión con condición:")
pares = [x for x in range(10) if x % 2 == 0]
print(f"Números pares del 0-9: {pares}")

# ---------------------------------------------------
# 8.3 Comprensión con if-else
# ---------------------------------------------------
print("\n8.3 Comprensión con if-else:")
clasificacion = ["Par" if x % 2 == 0 else "Impar" for x in range(5)]
print(f"Par/Impar 0-4: {clasificacion}")

# ---------------------------------------------------
# 8.4 Comprensión anidada
# ---------------------------------------------------
print("\n8.4 Comprensión anidada:")
combinaciones = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6]]
print(f"Combinaciones: {combinaciones}")

# =============================================
# 9. MÉTODOS ADICIONALES
# =============================================

print("\n" + "=" * 30)
print("9. MÉTODOS ADICIONALES")
print("=" * 30)

# ---------------------------------------------------
# 9.1 any() - Verifica si algún elemento es True
# ---------------------------------------------------
print("\n9.1 any() - Algún elemento True:")
lista_falsa = [False, 0, "", None]
lista_verdadera = [False, 0, "hola", None]
print(f"any({lista_falsa}): {any(lista_falsa)}")
print(f"any({lista_verdadera}): {any(lista_verdadera)}")

# ---------------------------------------------------
# 9.2 all() - Verifica si todos son True
# ---------------------------------------------------
print("\n9.2 all() - Todos True:")
lista_todos_true = [1, "hola", True, [1]]
lista_no_todos_true = [1, "hola", False, [1]]
print(f"all({lista_todos_true}): {all(lista_todos_true)}")
print(f"all({lista_no_todos_true}): {all(lista_no_todos_true)}")

# =============================================
# 10. EJEMPLOS PRÁCTICOS
# =============================================

print("\n" + "=" * 30)
print("10. EJEMPLOS PRÁCTICOS")
print("=" * 30)

# ---------------------------------------------------
# 10.1 Gestión de tareas
# ---------------------------------------------------
print("\n10.1 Gestión de tareas:")

tareas = ["Estudiar Python", "Hacer ejercicio", "Leer libro"]
print("Tareas iniciales:", tareas)

# Agregar nueva tarea
tareas.append("Preparar cena")
print("Después de agregar:", tareas)

# Marcar tarea como completada
tarea_completada = tareas.pop(1)
print(f"Tarea completada: {tarea_completada}")
print("Tareas pendientes:", tareas)

# ---------------------------------------------------
# 10.2 Análisis de datos
# ---------------------------------------------------
print("\n10.2 Análisis de datos:")

ventas = [150, 200, 175, 300, 225, 250, 400]
print("Ventas diarias:", ventas)

# Estadísticas básicas
print(f"Total ventas: {sum(ventas)}")
print(f"Promedio ventas: {sum(ventas)/len(ventas):.2f}")
print(f"Venta máxima: {max(ventas)}")
print(f"Venta mínima: {min(ventas)}")

# Ventas sobre 200
ventas_altas = [venta for venta in ventas if venta > 200]
print("Ventas sobre 200:", ventas_altas)

# ---------------------------------------------------
# 10.3 Procesamiento de texto
# ---------------------------------------------------
print("\n10.3 Procesamiento de texto:")

texto = "Python es un lenguaje de programación poderoso y versátil"
palabras = texto.split()
print("Palabras:", palabras)

# Palabras con más de 5 letras
palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]
print("Palabras con más de 5 letras:", palabras_largas)

# =============================================
# 11. RESUMEN DE MÉTODOS
# =============================================

print("\n" + "=" * 30)
print("11. RESUMEN DE MÉTODOS")
print("=" * 30)

metodos = [
    "append(x) - Agrega x al final",
    "extend(iterable) - Extiende la lista",
    "insert(i, x) - Inserta x en posición i",
    "remove(x) - Remueve primera ocurrencia de x",
    "pop([i]) - Remueve y retorna elemento en posición i",
    "clear() - Remueve todos los elementos",
    "index(x) - Retorna índice de x",
    "count(x) - Cuenta ocurrencias de x",
    "sort() - Ordena la lista",
    "reverse() - Invierte la lista",
    "copy() - Retorna copia superficial"
]

for i, metodo in enumerate(metodos, 1):
    print(f"{i:2d}. {metodo}")

# =============================================
# 12. EJERCICIOS PRÁCTICOS
# =============================================

print("\n" + "=" * 30)
print("12. EJERCICIOS PRÁCTICOS")
print("=" * 30)

print("""
1. Crea una lista con 10 números y calcula:
   - Suma total
   - Promedio
   - Números pares
   - Números mayores al promedio

2. Implementa una función que elimine duplicados
   de una lista manteniendo el orden

3. Crea un sistema de gestión de inventario
   usando listas con operaciones CRUD

4. Escribe una función que encuentre el
   segundo número más grande en una lista

5. Crea una lista de compras interactiva
   que permita agregar, remover y listar items
""")

print("\n" + "=" * 60)
print("¡FIN DE LA GUÍA DE LISTAS!")
print("=" * 60)

# Información adicional
print(f"\n💡 Tip: Practica con los ejercicios propuestos")
print("🚀 Ejecuta: python listas.py para ver todos los ejemplos")
print("📚 Documentación: https://docs.python.org/3/tutorial/datastructures.html")