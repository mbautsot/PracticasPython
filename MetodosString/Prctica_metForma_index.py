# =============================================
# EJEMPLOS DE LOS MÉTODOS format() E index()
# EN PYTHON - ARCHIVO DE ESTUDIO
# =============================================

print("=" * 60)
print("MÉTODO format() - FORMATEO DE CADENAS")
print("=" * 60)

# ---------------------------------------------------
# 1. FORMATO BÁSICO CON format()
# ---------------------------------------------------
print("\n1. FORMATO BÁSICO:")

# Sustitución por posición
nombre = "Ana"
edad = 25
mensaje1 = "Hola, me llamo {} y tengo {} años".format(nombre, edad)
print("Por posición:", mensaje1)

# Sustitución por nombre de variables
mensaje2 = "Hola, me llamo {nombre} y tengo {edad} años".format(nombre="Carlos", edad=30)
print("Por nombre:", mensaje2)

# ---------------------------------------------------
# 2. FORMATO CON INDICES NUMÉRICOS
# ---------------------------------------------------
print("\n2. FORMATO CON ÍNDICES:")

# Reutilizando el mismo valor múltiples veces
producto = "manzana"
precio = 2.5
mensaje3 = "El producto {0} cuesta ${1}. ¡Compre {0} hoy!".format(producto, precio)
print("Reutilización:", mensaje3)

# Cambiando el orden
mensaje4 = "Precio: ${1} - Producto: {0}".format(producto, precio)
print("Orden diferente:", mensaje4)

# ---------------------------------------------------
# 3. FORMATEO NUMÉRICO
# ---------------------------------------------------
print("\n3. FORMATEO NUMÉRICO:")

# Decimales
pi = 3.14159265
print("Pi con 2 decimales: {:.2f}".format(pi))
print("Pi con 4 decimales: {:.4f}".format(pi))

# Números grandes con separadores
numero_grande = 1000000
print("Número con separadores: {:,}".format(numero_grande))

# Porcentajes
tasa = 0.856
print("Porcentaje: {:.1%}".format(tasa))
print("Porcentaje: {:.2%}".format(tasa))

# Relleno y alineación
numero = 42
print("Relleno con ceros: {:05d}".format(numero))
print("Alineación derecha: {:>10}".format("Hola"))
print("Alineación izquierda: {:<10}".format("Hola"))
print("Centrado: {:^10}".format("Hola"))

# ---------------------------------------------------
# 4. FORMATEO CON F-STRINGS (Python 3.6+)
# ---------------------------------------------------
print("\n4. F-STRINGS (alternativa moderna):")

# Directamente con variables
ciudad = "Madrid"
temperatura = 22.5
print(f"La temperatura en {ciudad} es de {temperatura}°C")
print(f"Pi con 3 decimales: {pi:.3f}")

# ---------------------------------------------------
# 5. EJEMPLOS PRÁCTICOS COMBINADOS
# ---------------------------------------------------
print("\n5. EJEMPLOS PRÁCTICOS:")

# Factura
productos = [
    {"nombre": "Laptop", "precio": 899.99, "cantidad": 1},
    {"nombre": "Mouse", "precio": 25.50, "cantidad": 2},
    {"nombre": "Teclado", "precio": 45.75, "cantidad": 1}
]

print("FACTURA:")
print("-" * 30)
for producto in productos:
    total = producto["precio"] * producto["cantidad"]
    print("{:<15} {:<2} x ${:<6.2f} = ${:<7.2f}".format(
        producto["nombre"],
        producto["cantidad"],
        producto["precio"],
        total
    ))

print("=" * 60)
print("MÉTODO index() - BÚSQUEDA EN CADENAS")
print("=" * 60)

# ---------------------------------------------------
# 1. index() BÁSICO
# ---------------------------------------------------
print("\n1. index() BÁSICO:")

texto = "Python es un lenguaje de programación poderoso"

# Buscar la posición de una subcadena
posicion = texto.index("lenguaje")
print(f"Posición de 'lenguaje': {posicion}")

# Buscar desde una posición específica
posicion2 = texto.index("a", 15)  # Buscar "a" a partir del índice 15
print(f"Posición de 'a' desde índice 15: {posicion2}")

# ---------------------------------------------------
# 2. index() CON RANGO DE BÚSQUEDA
# ---------------------------------------------------
print("\n2. index() CON RANGO:")

# Buscar entre dos índices
frase = "programación en Python y programación en Java"
try:
    pos = frase.index("programación", 15, 30)  # Buscar entre índice 15 y 30
    print(f"'programación' entre 15-30: {pos}")
except ValueError:
    print("No encontrado en el rango especificado")

# ---------------------------------------------------
# 3. DIFERENCIA ENTRE index() Y find()
# ---------------------------------------------------
print("\n3. index() VS find():")

# index() lanza excepción si no encuentra
# find() devuelve -1 si no encuentra

texto_ejemplo = "Hola mundo"

try:
    resultado_index = texto_ejemplo.index("x")
    print(f"index() encontró: {resultado_index}")
except ValueError as e:
    print(f"index() no encontró: {e}")

resultado_find = texto_ejemplo.find("x")
print(f"find() devolvió: {resultado_find}")

# ---------------------------------------------------
# 4. MANEJO DE ERRORES CON index()
# ---------------------------------------------------
print("\n4. MANEJO DE ERRORES:")

palabras = ["Python", "Java", "JavaScript", "C++"]

for palabra in palabras:
    try:
        posicion = palabra.index("a")
        print(f"En '{palabra}', la 'a' está en posición: {posicion}")
    except ValueError:
        print(f"'{palabra}' no contiene la letra 'a'")

# ---------------------------------------------------
# 5. EJEMPLOS PRÁCTICOS CON index()
# ---------------------------------------------------
print("\n5. EJEMPLOS PRÁCTICOS:")

# Extraer dominio de email
email = "usuario@example.com"
try:
    pos_arroba = email.index("@")
    dominio = email[pos_arroba + 1:]
    print(f"Email: {email}")
    print(f"Dominio: {dominio}")
except ValueError:
    print("Email no válido")

# Buscar todas las ocurrencias
texto_largo = "Python es genial. Python es fácil. Python es poderoso."
palabra_buscar = "Python"
inicio = 0
ocurrencias = []

while True:
    try:
        pos = texto_largo.index(palabra_buscar, inicio)
        ocurrencias.append(pos)
        inicio = pos + 1
    except ValueError:
        break

print(f"'{palabra_buscar}' encontrada en posiciones: {ocurrencias}")

# ---------------------------------------------------
# 6. EJERCICIOS PRÁCTICOS
# ---------------------------------------------------
print("\n6. EJERCICIOS PRÁCTICOS:")

# Ejercicio 1: Formatear fecha
dia = 15
mes = 8
anio = 2024
fecha = "{:02d}/{:02d}/{}".format(dia, mes, anio)
print(f"Fecha formateada: {fecha}")

# Ejercicio 2: Buscar en lista
lenguajes = "Python, Java, C++, JavaScript, HTML, CSS"
try:
    pos_css = lenguajes.index("CSS")
    print(f"CSS encontrado en posición: {pos_css}")
except ValueError:
    print("CSS no encontrado")

print("\n" + "=" * 60)
print("¡FIN DEL ARCHIVO DE ESTUDIO!")
print("=" * 60)