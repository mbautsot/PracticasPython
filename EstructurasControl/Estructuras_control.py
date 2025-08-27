# =============================================
# ESTRUCTURAS DE CONTROL EN PYTHON - GUÍA COMPLETA
# =============================================

print("=" * 60)
print("ESTRUCTURAS DE CONTROL EN PYTHON")
print("=" * 60)

# =============================================
# 1. ESTRUCTURAS CONDICIONALES
# =============================================

print("\n" + "=" * 30)
print("1. ESTRUCTURAS CONDICIONALES")
print("=" * 30)

# ---------------------------------------------------
# 1.1 if BÁSICO
# ---------------------------------------------------
print("\n1.1 if BÁSICO:")
edad = 18

if edad >= 18:
    print("✅ Eres mayor de edad")
    print("Puedes votar en las elecciones")

# ---------------------------------------------------
# 1.2 if-else
# ---------------------------------------------------
print("\n1.2 if-else:")
temperatura = 25

if temperatura > 30:
    print("🔥 Hace calor")
else:
    print("🌤️ Temperatura agradable")

# ---------------------------------------------------
# 1.3 if-elif-else (Múltiples condiciones)
# ---------------------------------------------------
print("\n1.3 if-elif-else:")
nota = 85

if nota >= 90:
    print("🎉 Excelente (A)")
elif nota >= 80:
    print("👍 Muy bien (B)")
elif nota >= 70:
    print("✅ Bien (C)")
elif nota >= 60:
    print("⚠️ Aprobado (D)")
else:
    print("❌ Reprobado (F)")

# ---------------------------------------------------
# 1.4 if ANIDADOS
# ---------------------------------------------------
print("\n1.4 if ANIDADOS:")
usuario_autenticado = True
es_admin = False

if usuario_autenticado:
    if es_admin:
        print("👑 Acceso de administrador concedido")
    else:
        print("👤 Acceso de usuario regular")
else:
    print("🔒 Por favor inicia sesión")

# ---------------------------------------------------
# 1.5 OPERADORES TERNARIOS
# ---------------------------------------------------
print("\n1.5 OPERADOR TERNARIO:")
edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(f"Edad {edad}: {mensaje}")

# Operador ternario con múltiples condiciones
calificacion = "Aprobado" if nota >= 60 else "Reprobado"
print(f"Nota {nota}: {calificacion}")

# =============================================
# 2. ESTRUCTURAS DE REPETICIÓN (BUCLES)
# =============================================

print("\n" + "=" * 30)
print("2. ESTRUCTURAS DE REPETICIÓN")
print("=" * 30)

# ---------------------------------------------------
# 2.1 for LOOP BÁSICO
# ---------------------------------------------------
print("\n2.1 for LOOP BÁSICO:")

print("Iterando sobre una lista:")
frutas = ["manzana", "banana", "naranja", "uva"]
for fruta in frutas:
    print(f"🍎 {fruta}")

print("\nIterando sobre un string:")
palabra = "Python"
for letra in palabra:
    print(f"🔤 {letra}")

# ---------------------------------------------------
# 2.2 for con range()
# ---------------------------------------------------
print("\n2.2 for con range():")

print("Range con un parámetro (0 a 4):")
for i in range(5):
    print(f"➡️ Número: {i}")

print("\nRange con dos parámetros (5 a 9):")
for i in range(5, 10):
    print(f"➡️ Número: {i}")

print("\nRange con tres parámetros (0 a 10, paso 2):")
for i in range(0, 11, 2):
    print(f"➡️ Número par: {i}")

# ---------------------------------------------------
# 2.3 for con enumerate()
# ---------------------------------------------------
print("\n2.3 for con enumerate():")
print("Iterando con índice y valor:")

for indice, fruta in enumerate(frutas):
    print(f"📌 Índice {indice}: {fruta}")

# ---------------------------------------------------
# 2.4 for con zip()
# ---------------------------------------------------
print("\n2.4 for con zip():")
nombres = ["Ana", "Juan", "María"]
edades = [25, 30, 28]

print("Iterando sobre múltiples listas:")
for nombre, edad in zip(nombres, edades):
    print(f"👤 {nombre} tiene {edad} años")

# ---------------------------------------------------
# 2.5 while LOOP
# ---------------------------------------------------
print("\n2.5 while LOOP:")

print("Contador con while:")
contador = 0
while contador < 5:
    print(f"🔢 Contador: {contador}")
    contador += 1

print("\nWhile con condición externa:")
import random

intentos = 0
numero_secreto = random.randint(1, 10)

while intentos < 3:
    intentos += 1
    print(f"🎯 Intento {intentos}/3 - Adivina el número (1-10)")
    # En un caso real aquí iría input()

# ---------------------------------------------------
# 2.6 while con break
# ---------------------------------------------------
print("\n2.6 while con break:")
print("Búsqueda con break:")

numeros = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
objetivo = 4

for num in numeros:
    print(f"Revisando número: {num}")
    if num == objetivo:
        print(f"🎯 ¡Número {objetivo} encontrado!")
        break

# ---------------------------------------------------
# 2.7 while con continue
# ---------------------------------------------------
print("\n2.7 while con continue:")
print("Saltando números pares:")

for num in range(1, 11):
    if num % 2 == 0:  # Si es par
        continue  # Saltar a la siguiente iteración
    print(f"➡️ Número impar: {num}")

# ---------------------------------------------------
# 2.8 while con else
# ---------------------------------------------------
print("\n2.8 while/for con else:")
print("Búsqueda con else:")

busqueda = 15
for num in range(1, 11):
    if num == busqueda:
        print(f"✅ {busqueda} encontrado")
        break
else:
    print(f"❌ {busqueda} no encontrado en el rango")

# =============================================
# 3. ESTRUCTURAS DE CONTROL AVANZADAS
# =============================================

print("\n" + "=" * 30)
print("3. ESTRUCTURAS AVANZADAS")
print("=" * 30)

# ---------------------------------------------------
# 3.1 match-case (Python 3.10+)
# ---------------------------------------------------
print("\n3.1 match-case (Switch moderno):")


def describir_color(color):
    match color:
        case "rojo":
            return "🔴 Color de pasión y energía"
        case "azul":
            return "🔵 Color de calma y confianza"
        case "verde":
            return "🟢 Color de naturaleza y crecimiento"
        case _:
            return "⚫ Color no reconocido"


print(describir_color("rojo"))
print(describir_color("amarillo"))

# ---------------------------------------------------
# 3.2 COMPRENSIÓN DE LISTAS
# ---------------------------------------------------
print("\n3.2 COMPRENSIÓN DE LISTAS:")

# Equivalente a for loop
print("Números al cuadrado:")
cuadrados = [x ** 2 for x in range(1, 6)]
print(f"Cuadrados: {cuadrados}")

print("\nFiltrando números pares:")
pares = [x for x in range(1, 11) if x % 2 == 0]
print(f"Pares: {pares}")

print("\nTransformando strings:")
nombres_mayusculas = [nombre.upper() for nombre in nombres]
print(f"Nombres en mayúsculas: {nombres_mayusculas}")

# ---------------------------------------------------
# 3.3 COMPRENSIÓN DE DICCIONARIOS
# ---------------------------------------------------
print("\n3.3 COMPRENSIÓN DE DICCIONARIOS:")

print("Creando diccionario con números y sus cuadrados:")
cuadrados_dict = {x: x ** 2 for x in range(1, 6)}
print(f"Cuadrados dict: {cuadrados_dict}")

print("\nFiltrando diccionario:")
edades_filtradas = {nombre: edad for nombre, edad in zip(nombres, edades) if edad > 26}
print(f"Edades > 26: {edades_filtradas}")

# =============================================
# 4. EJEMPLOS PRÁCTICOS Y COMBINADOS
# =============================================

print("\n" + "=" * 30)
print("4. EJEMPLOS PRÁCTICOS")
print("=" * 30)

# ---------------------------------------------------
# 4.1 VALIDACIÓN DE USUARIO
# ---------------------------------------------------
print("\n4.1 VALIDACIÓN DE USUARIO:")


def validar_usuario(usuario, contraseña):
    # Simulando base de datos
    usuarios_validos = {
        "admin": "admin123",
        "usuario1": "clave123",
        "invitado": "guest123"
    }

    if usuario in usuarios_validos:
        if usuarios_validos[usuario] == contraseña:
            return "✅ Acceso concedido"
        else:
            return "❌ Contraseña incorrecta"
    else:
        return "❌ Usuario no existe"


# Simulando inputs
print(validar_usuario("admin", "admin123"))
print(validar_usuario("admin", "wrongpass"))

# ---------------------------------------------------
# 4.2 CONTADOR DE PALABRAS
# ---------------------------------------------------
print("\n4.2 CONTADOR DE PALABRAS:")


def contar_palabras(texto):
    palabras = texto.split()
    contador = {}

    for palabra in palabras:
        palabra = palabra.lower().strip('.,!?')
        if palabra:
            contador[palabra] = contador.get(palabra, 0) + 1

    return contador


texto_ejemplo = "Python es genial. Python es fácil. Python es poderoso."
resultado = contar_palabras(texto_ejemplo)
print("Conteo de palabras:", resultado)

# ---------------------------------------------------
# 4.3 GENERADOR DE TABLA DE MULTIPLICAR
# ---------------------------------------------------
print("\n4.3 TABLA DE MULTIPLICAR:")


def generar_tabla(numero):
    print(f"\nTabla del {numero}:")
    print("-" * 15)
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i:2} = {resultado:2}")


generar_tabla(5)

# ---------------------------------------------------
# 4.4 JUEGO DE ADIVINANZAS
# ---------------------------------------------------
print("\n4.4 JUEGO DE ADIVINANZAS (simulado):")


def juego_adivinanza():
    numero_secreto = 7
    intentos = 3
    adivinado = False

    print("🎮 Adivina el número entre 1-10")

    for intento in range(1, intentos + 1):
        print(f"Intento {intento}/{intentos}")
        # Simulando input: numero = int(input("Tu número: "))
        numero = 3 if intento == 1 else 8 if intento == 2 else 7

        if numero == numero_secreto:
            print("🎉 ¡Correcto! ¡Ganaste!")
            adivinado = True
            break
        elif numero < numero_secreto:
            print("⬆️ Más alto")
        else:
            print("⬇️ Más bajo")

    if not adivinado:
        print(f"😢 Perdiste. El número era {numero_secreto}")


juego_adivinanza()

# ---------------------------------------------------
# 4.5 FILTRO DE NÚMEROS PRIMOS
# ---------------------------------------------------
print("\n4.5 FILTRO DE NÚMEROS PRIMOS:")


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


print("Números primos del 1 al 20:")
primos = [num for num in range(1, 21) if es_primo(num)]
print(primos)

# =============================================
# 5. BUENAS PRÁCTICAS Y RECOMENDACIONES
# =============================================

print("\n" + "=" * 30)
print("5. BUENAS PRÁCTICAS")
print("=" * 30)

print("""
✅ Use nombres descriptivos para variables
✅ Mantenga la indentación consistente (4 espacios)
✅ Use break y continue con moderación
✅ Prefiera for sobre while cuando sea posible
✅ Use funciones para organizar código complejo
✅ Comente el código cuando la lógica no sea obvia
✅ Use match-case para múltiples condiciones simples
✅ Prefiera comprensiones de listas para transformaciones simples
""")

# =============================================
# 6. EJERCICIOS PRÁCTICOS
# =============================================

print("\n" + "=" * 30)
print("6. EJERCICIOS PRÁCTICOS")
print("=" * 30)

print("""
1. Crea un programa que clasifique números en:
   - Negativos
   - Cero
   - Positivos pequeños (1-10)
   - Positivos grandes (>10)

2. Escribe un programa que muestre la serie Fibonacci
   hasta un número dado

3. Crea un validador de contraseñas que verifique:
   - Mínimo 8 caracteres
   - Al menos 1 mayúscula
   - Al menos 1 número
   - Al menos 1 carácter especial

4. Implementa un sistema de menú simple usando while
   con opciones para el usuario

5. Crea un traductor simple que convierta números
   a su representación en palabras (1 -> "uno")
""")

print("\n" + "=" * 60)
print("¡FIN DE LA GUÍA DE ESTRUCTURAS DE CONTROL!")
print("=" * 60)

# Información adicional
print(f"\n💡 Tip: Practica modificando estos ejemplos")
print("🚀 Ejecuta: python nombre_archivo.py para probar")
print("📚 Documentación: https://docs.python.org/3/tutorial/controlflow.html")