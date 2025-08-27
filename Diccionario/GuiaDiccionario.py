"""
==============================================
DICCIONARIOS EN PYTHON - GUÍA COMPLETA
==============================================
"""

# ==========================================================================
# ¿QUÉ ES UN DICCIONARIO?
# ==========================================================================
"""
Un diccionario es una estructura de datos que almacena pares 
clave-valor. Es mutable, no ordenado (hasta Python 3.6) y 
no permite claves duplicadas.

Sintaxis: {clave1: valor1, clave2: valor2, ...}
"""

print("=" * 60)
print("CREACIÓN DE DICCIONARIOS")
print("=" * 60)

# Método 1: Literal
persona = {
    "nombre": "María",
    "edad": 25,
    "ciudad": "Madrid"
}
print("1. Diccionario literal:", persona)

# Método 2: Constructor dict()
estudiante = dict(nombre="Carlos", nota=8.5, aprobado=True)
print("2. Con constructor:", estudiante)

# Método 3: Desde lista de tuplas
pares = [("a", 1), ("b", 2), ("c", 3)]
diccionario = dict(pares)
print("3. Desde tuplas:", diccionario)

print("\n" + "=" * 60)
print("ACCESO A ELEMENTOS")
print("=" * 60)

# Acceso con []
print("1. Acceso con []:", persona["nombre"])

# Acceso con get() (recomendado)
print("2. Acceso con get():", persona.get("edad"))
print("3. Get con valor por defecto:", persona.get("país", "España"))

# Verificar existencia
print("4. ¿Tiene clave 'edad'?", "edad" in persona)

print("\n" + "=" * 60)
print("MÉTODOS PRINCIPALES")
print("=" * 60)

# keys() - Obtener todas las claves
print("1. keys():", list(persona.keys()))

# values() - Obtener todos los valores
print("2. values():", list(persona.values()))

# items() - Obtener pares clave-valor
print("3. items():", list(persona.items()))

# update() - Actualizar con otro diccionario
persona.update({"edad": 26, "país": "España"})
print("4. después de update():", persona)

# pop() - Eliminar y obtener valor
edad = persona.pop("edad")
print("5. pop('edad'):", edad, "| Diccionario:", persona)

# popitem() - Eliminar último elemento
ultimo = persona.popitem()
print("6. popitem():", ultimo, "| Diccionario:", persona)

# clear() - Vaciar diccionario
copia = persona.copy()
copia.clear()
print("7. clear():", copia)

print("\n" + "=" * 60)
print("MÉTODOS AVANZADOS")
print("=" * 60)

# setdefault() - Obtener valor o establecer si no existe
valor = persona.setdefault("nombre", "Anónimo")
print("1. setdefault() existente:", valor)

valor = persona.setdefault("ocupación", "Estudiante")
print("2. setdefault() nuevo:", valor, "| Diccionario:", persona)

# fromkeys() - Crear diccionario con claves y valor por defecto
claves = ["nombre", "edad", "ciudad"]
nuevo = dict.fromkeys(claves, "desconocido")
print("3. fromkeys():", nuevo)

print("\n" + "=" * 60)
print("ITERACIÓN SOBRE DICCIONARIOS")
print("=" * 60)

# Iterar por claves
print("Iterar por claves:")
for clave in persona:
    print(f"  {clave}: {persona[clave]}")

# Iterar por items
print("\nIterar por items:")
for clave, valor in persona.items():
    print(f"  {clave}: {valor}")

print("\n" + "=" * 60)
print("COMPRENSIÓN DE DICCIONARIOS")
print("=" * 60)

# Crear diccionario a partir de otro
numeros = {"a": 1, "b": 2, "c": 3, "d": 4}
cuadrados = {k: v**2 for k, v in numeros.items() if v % 2 == 0}
print("Comprensión:", cuadrados)

print("\n" + "=" * 60)
print("DICCIONARIOS ANIDADOS")
print("=" * 60)

# Diccionarios dentro de diccionarios
empresa = {
    "empleado1": {"nombre": "Ana", "salario": 30000},
    "empleado2": {"nombre": "Luis", "salario": 35000}
}
print("Diccionario anidado:", empresa)
print("Acceso anidado:", empresa["empleado1"]["nombre"])

print("\n" + "=" * 60)
print("CASOS DE USO COMUNES")
print("=" * 60)

# 1. Contador de elementos
palabra = "python"
contador = {}
for letra in palabra:
    contador[letra] = contador.get(letra, 0) + 1
print("1. Contador de letras:", contador)

# 2. Agrupación de datos
estudiantes = [
    {"nombre": "Ana", "curso": "Matemáticas"},
    {"nombre": "Luis", "curso": "Historia"},
    {"nombre": "Ana", "curso": "Física"}
]

grupos = {}
for estudiante in estudiantes:
    nombre = estudiante["nombre"]
    if nombre not in grupos:
        grupos[nombre] = []
    grupos[nombre].append(estudiante["curso"])

print("2. Agrupación:", grupos)

print("\n" + "=" * 60)
print("BUENAS PRÁCTICAS")
print("=" * 60)
print("1. Usar get() en lugar de [] para evitar KeyError")
print("2. Usar items() para iterar eficientemente")
print("3. Usar comprensiones para transformaciones")
print("4. Usar diccionarios para datos estructurados")
print("5. Validar existencia de claves con 'in'")

# Ejecutar este archivo para ver todos los ejemplos
if __name__ == "__main__":
    print("¡Ejecuta el archivo para ver los ejemplos en acción!")