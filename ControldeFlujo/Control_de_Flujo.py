"""
GUÍA COMPLETA DE CONTROL DE FLUJO EN PYTHON
Ejercicios prácticos y reales
"""

print("=" * 60)
print("GUÍA DE CONTROL DE FLUJO EN PYTHON")
print("=" * 60)

print("\n" + "=" * 40)
print("1. ESTRUCTURAS IF, ELIF, ELSE")
print("=" * 40)

# Ejemplo 1: Validación de edad para votar
print("👉 VALIDACIÓN DE EDAD PARA VOTAR:")
edad = 20
if edad >= 18:
    print("Puede votar")
else:
    print("No puede votar")

# Ejemplo 2: Sistema de calificaciones
print("\n👉 SISTEMA DE CALIFICACIONES:")
calificacion = 85
if calificacion >= 90:
    print("Calificación: A")
elif calificacion >= 80:
    print("Calificación: B")
elif calificacion >= 70:
    print("Calificación: C")
elif calificacion >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")

# Ejemplo 3: Verificación de número positivo/negativo/cero
print("\n👉 VERIFICACIÓN DE NÚMERO:")
numero = -5
if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Cero")

print("\n" + "=" * 40)
print("2. BUCLES WHILE")
print("=" * 40)

# Ejemplo 1: Contador regresivo
print("👉 CONTADOR REGRESIVO:")
contador = 5
while contador > 0:
    print(f"Cuenta regresiva: {contador}")
    contador -= 1
print("¡Despegue!")

# Ejemplo 2: Validación de entrada de usuario
print("\n👉 VALIDACIÓN DE ENTRADA:")
intentos = 3
while intentos > 0:
    password = input("Ingrese password: ")
    if password == "secreto":
        print("Acceso concedido")
        break
    else:
        intentos -= 1
        print(f"Password incorrecto. Intentos restantes: {intentos}")
else:
    print("Cuenta bloqueada")

# Ejemplo 3: Suma acumulativa
print("\n👉 SUMA ACUMULATIVA:")
suma = 0
numero = 1
while numero <= 10:
    suma += numero
    numero += 1
print(f"Suma de 1 a 10: {suma}")

print("\n" + "=" * 40)
print("3. BUCLES FOR")
print("=" * 40)

# Ejemplo 1: Iteración sobre lista
print("👉 ITERACIÓN SOBRE LISTA:")
frutas = ["manzana", "banana", "naranja", "uva"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")

# Ejemplo 2: Iteración con range
print("\n👉 TABLA DE MULTIPLICAR:")
numero = 5
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Ejemplo 3: Iteración sobre string
print("\n👉 CONTADOR DE VOCALES:")
texto = "Python programming"
vocales = 0
for letra in texto:
    if letra.lower() in "aeiou":
        vocales += 1
print(f"El texto tiene {vocales} vocales")

print("\n" + "=" * 40)
print("4. BREAK, CONTINUE Y PASS")
print("=" * 40)

# Ejemplo 1: Break - Salir del bucle
print("👉 BREAK - BUSCAR ELEMENTO:")
numeros = [1, 3, 5, 7, 9, 2, 4, 6, 8]
for num in numeros:
    if num % 2 == 0:
        print(f"Primer número par encontrado: {num}")
        break

# Ejemplo 2: Continue - Saltar iteración
print("\n👉 CONTINUE - NÚMEROS IMPARES:")
print("Números impares del 1 al 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# Ejemplo 3: Pass - placeholder
print("\n👉 PASS - PLACEHOLDER:")
for i in range(5):
    if i == 3:
        pass  # Para implementar después
    else:
        print(i)

print("\n" + "=" * 40)
print("5. BUCLES ANIDADOS")
print("=" * 40)

# Ejemplo 1: Tablas de multiplicar
print("👉 TABLAS DE MULTIPLICAR:")
for i in range(1, 4):  # Tablas del 1 al 3
    print(f"\nTabla del {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

# Ejemplo 2: Patrón de asteriscos
print("\n👉 PATRÓN DE ASTERISCOS:")
filas = 5
for i in range(1, filas + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n" + "=" * 40)
print("6. COMPREHENSION DE LISTAS")
print("=" * 40)

# Ejemplo 1: Lista de cuadrados
print("👉 LISTA DE CUADRADOS:")
cuadrados = [x ** 2 for x in range(1, 6)]
print(f"Cuadrados: {cuadrados}")

# Ejemplo 2: Filtrado con condición
print("\n👉 NÚMEROS PARES:")
pares = [x for x in range(1, 11) if x % 2 == 0]
print(f"Números pares: {pares}")

# Ejemplo 3: Transformación de strings
print("\n👉 LONGITUD DE PALABRAS:")
palabras = ["python", "java", "javascript", "c++"]
longitudes = [len(palabra) for palabra in palabras]
print(f"Longitudes: {longitudes}")

print("\n" + "=" * 40)
print("7. MANEJO DE EXCEPCIONES (TRY/EXCEPT)")
print("=" * 40)

# Ejemplo 1: División segura
print("👉 DIVISIÓN SEGURA:")
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")

# Ejemplo 2: Conversión segura a número
print("\n👉 CONVERSIÓN SEGURA:")
entrada = "abc"
try:
    numero = int(entrada)
    print(f"Número convertido: {numero}")
except ValueError:
    print("Error: No se puede convertir a número")

# Ejemplo 3: Múltiples excepciones
print("\n👉 MÚLTIPLES EXCEPCIONES:")
try:
    # Código que puede fallar
    lista = [1, 2, 3]
    print(lista[5])
except IndexError:
    print("Error: Índice fuera de rango")
except Exception as e:
    print(f"Error inesperado: {e}")

print("\n" + "=" * 40)
print("8. EJEMPLOS DEL MUNDO REAL")
print("=" * 40)

# Ejemplo 1: Sistema de login
print("👉 SISTEMA DE LOGIN:")


def sistema_login():
    usuarios = {"admin": "1234", "user": "password"}
    intentos = 3

    while intentos > 0:
        usuario = input("Usuario: ")
        password = input("Password: ")

        if usuario in usuarios and usuarios[usuario] == password:
            print("Login exitoso!")
            return True
        else:
            intentos -= 1
            print(f"Credenciales incorrectas. Intentos restantes: {intentos}")

    print("Sistema bloqueado")
    return False


# Descomenta para probar:
# sistema_login()

# Ejemplo 2: Calculadora simple
print("\n👉 CALCULADORA SIMPLE:")


def calculadora():
    while True:
        print("\nOperaciones: +, -, *, /, salir")
        operacion = input("Seleccione operación: ")

        if operacion == "salir":
            print("Adiós!")
            break

        try:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))

            if operacion == "+":
                resultado = num1 + num2
            elif operacion == "-":
                resultado = num1 - num2
            elif operacion == "*":
                resultado = num1 * num2
            elif operacion == "/":
                resultado = num1 / num2
            else:
                print("Operación no válida")
                continue

            print(f"Resultado: {resultado}")

        except ValueError:
            print("Error: Ingrese números válidos")
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero")


# Descomenta para probar:
# calculadora()

# Ejemplo 3: Gestor de tareas
print("\n👉 GESTOR DE TAREAS:")


def gestor_tareas():
    tareas = []

    while True:
        print("\n1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar como completada")
        print("4. Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            tarea = input("Ingrese tarea: ")
            tareas.append({"tarea": tarea, "completada": False})
            print("Tarea agregada!")

        elif opcion == "2":
            if not tareas:
                print("No hay tareas")
            else:
                print("\nLista de tareas:")
                for i, tarea in enumerate(tareas, 1):
                    estado = "✓" if tarea["completada"] else "✗"
                    print(f"{i}. [{estado}] {tarea['tarea']}")

        elif opcion == "3":
            try:
                indice = int(input("Número de tarea a completar: ")) - 1
                if 0 <= indice < len(tareas):
                    tareas[indice]["completada"] = True
                    print("Tarea marcada como completada!")
                else:
                    print("Número de tarea inválido")
            except ValueError:
                print("Ingrese un número válido")

        elif opcion == "4":
            print("Adiós!")
            break

        else:
            print("Opción no válida")

# Descomenta para probar:
# gestor_tareas()