"""
EJERCICIOS PRÁCTICOS DE CONTROL DE FLUJO
"""

print("=" * 50)
print("EJERCICIOS PRÁCTICOS")
print("=" * 50)


# Ejercicio 1: Verificador de número primo
def es_primo(numero):
    """Determina si un número es primo"""
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


print("1. VERIFICADOR DE NÚMEROS PRIMOS:")
numeros = [2, 7, 10, 13, 20]
for num in numeros:
    print(f"{num} es primo: {es_primo(num)}")


# Ejercicio 2: Calculadora de factorial
def factorial(n):
    """Calcula el factorial de un número"""
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


print("\n2. CÁLCULO DE FACTORIAL:")
for i in range(1, 6):
    print(f"Factorial de {i}: {factorial(i)}")


# Ejercicio 3: Contador de palabras
def contar_palabras(texto):
    """Cuenta las palabras en un texto"""
    palabras = texto.split()
    return len(palabras)


print("\n3. CONTADOR DE PALABRAS:")
textos = ["Hola mundo", "Python es genial", " "]
for texto in textos:
    print(f"'{texto}' tiene {contar_palabras(texto)} palabras")


# Ejercicio 4: Generador de secuencia Fibonacci
def fibonacci(n):
    """Genera los primeros n números de Fibonacci"""
    secuencia = [0, 1]
    for i in range(2, n):
        siguiente = secuencia[i - 1] + secuencia[i - 2]
        secuencia.append(siguiente)
    return secuencia[:n]


print("\n4. SECUENCIA FIBONACCI:")
print(f"Primeros 10 números: {fibonacci(10)}")


# Ejercicio 5: Validador de email
def validar_email(email):
    """Valida si un email tiene formato correcto"""
    if '@' not in email or '.' not in email:
        return False
    if email.count('@') != 1:
        return False
    if email.startswith('@') or email.endswith('@'):
        return False
    return True


print("\n5. VALIDADOR DE EMAIL:")
emails = ["user@example.com", "invalid", "user@", "@domain.com"]
for email in emails:
    print(f"{email}: {'Válido' if validar_email(email) else 'Inválido'}")


# Ejercicio 6: Juego de adivinanza
def juego_adivinanza():
    """Juego para adivinar un número"""
    import random
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("\n6. JUEGO DE ADIVINANZA:")
    print("Adivina el número entre 1 y 100")

    while True:
        try:
            guess = int(input("Tu guess: "))
            intentos += 1

            if guess < numero_secreto:
                print("Más alto!")
            elif guess > numero_secreto:
                print("Más bajo!")
            else:
                print(f"¡Correcto! Lo adivinaste en {intentos} intentos")
                break

        except ValueError:
            print("Por favor ingresa un número válido")


# Descomenta para jugar:
# juego_adivinanza()

# Ejercicio 7: Conversor de temperatura
def conversor_temperatura():
    """Convierte entre Celsius y Fahrenheit"""
    print("\n7. CONVERSOR DE TEMPERATURA:")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")

    try:
        opcion = int(input("Selecciona opción (1-2): "))
        temperatura = float(input("Ingresa temperatura: "))

        if opcion == 1:
            resultado = (temperatura * 9 / 5) + 32
            print(f"{temperatura}°C = {resultado:.2f}°F")
        elif opcion == 2:
            resultado = (temperatura - 32) * 5 / 9
            print(f"{temperatura}°F = {resultado:.2f}°C")
        else:
            print("Opción no válida")

    except ValueError:
        print("Ingresa valores numéricos válidos")


# Descomenta para probar:
# conversor_temperatura()

# Ejercicio 8: Gestor de contactos
def gestor_contactos():
    """Sistema simple de gestión de contactos"""
    contactos = []

    while True:
        print("\n--- GESTOR DE CONTACTOS ---")
        print("1. Agregar contacto")
        print("2. Ver contactos")
        print("3. Buscar contacto")
        print("4. Salir")

        try:
            opcion = int(input("Selecciona opción: "))

            if opcion == 1:
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
                print("Contacto agregado!")

            elif opcion == 2:
                if not contactos:
                    print("No hay contactos")
                else:
                    print("\nLista de contactos:")
                    for i, contacto in enumerate(contactos, 1):
                        print(f"{i}. {contacto['nombre']} - {contacto['telefono']} - {contacto['email']}")

            elif opcion == 3:
                busqueda = input("Buscar por nombre: ").lower()
                encontrados = [c for c in contactos if busqueda in c['nombre'].lower()]
                if encontrados:
                    print("Contactos encontrados:")
                    for contacto in encontrados:
                        print(f"{contacto['nombre']} - {contacto['telefono']} - {contacto['email']}")
                else:
                    print("No se encontraron contactos")

            elif opcion == 4:
                print("Adiós!")
                break

            else:
                print("Opción no válida")

        except ValueError:
            print("Ingresa un número válido")


# Descomenta para probar:
# gestor_contactos()

# Ejercicio 9: Análisis de texto
def analizar_texto():
    """Analiza un texto y muestra estadísticas"""
    texto = input("Ingresa un texto: ")

    # Estadísticas
    palabras = texto.split()
    caracteres = len(texto)
    palabras_count = len(palabras)
    oraciones = texto.count('.') + texto.count('!') + texto.count('?')

    print(f"\nESTADÍSTICAS DEL TEXTO:")
    print(f"Caracteres: {caracteres}")
    print(f"Palabras: {palabras_count}")
    print(f"Oraciones: {oraciones}")
    print(f"Palabra más larga: {max(palabras, key=len) if palabras else 'N/A'}")


# Descomenta para probar:
# analizar_texto()

# Ejercicio 10: Simulador de cajero automático
def cajero_automatico():
    """Simula un cajero automático simple"""
    saldo = 1000

    while True:
        print(f"\n--- CAJERO AUTOMÁTICO ---")
        print(f"Saldo actual: ${saldo}")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Salir")

        try:
            opcion = int(input("Selecciona opción: "))

            if opcion == 1:
                monto = float(input("Monto a depositar: "))
                if monto > 0:
                    saldo += monto
                    print(f"Depósito exitoso. Nuevo saldo: ${saldo}")
                else:
                    print("Monto debe ser positivo")

            elif opcion == 2:
                monto = float(input("Monto a retirar: "))
                if 0 < monto <= saldo:
                    saldo -= monto
                    print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
                else:
                    print("Monto inválido o fondos insuficientes")

            elif opcion == 3:
                print("Gracias por usar nuestro cajero")
                break

            else:
                print("Opción no válida")

        except ValueError:
            print("Ingresa un valor numérico válido")


# Descomenta para probar:
# cajero_automatico()

print("\n" + "=" * 50)
print("¡EJERCICIOS COMPLETADOS!")
print("=" * 50)