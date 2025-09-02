"""
SOLUCIONES DE LOS EJERCICIOS
"""

# Solución Ejercicio 1: Verificador de número primo
def es_primo_solucion(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Solución Ejercicio 2: Calculadora de factorial
def factorial_solucion(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Solución Ejercicio 3: Contador de palabras
def contar_palabras_solucion(texto):
    return len(texto.split())

# Solución Ejercicio 4: Generador de secuencia Fibonacci
def fibonacci_solucion(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    secuencia = [0, 1]
    for i in range(2, n):
        secuencia.append(secuencia[i-1] + secuencia[i-2])
    return secuencia

# Solución Ejercicio 5: Validador de email
def validar_email_solucion(email):
    return ('@' in email and
            '.' in email and
            email.count('@') == 1 and
            not email.startswith('@') and
            not email.endswith('@'))

print("SOLUCIONES EJERCICIO 1:")
print(f"2 es primo: {es_primo_solucion(2)}")
print(f"10 es primo: {es_primo_solucion(10)}")

print("\nSOLUCIONES EJERCICIO 2:")
print(f"Factorial de 5: {factorial_solucion(5)}")

print("\nSOLUCIONES EJERCICIO 3:")
print(f"Palabras en 'Hola mundo': {contar_palabras_solucion('Hola mundo')}")

print("\nSOLUCIONES EJERCICIO 4:")
print(f"Fibonacci de 5: {fibonacci_solucion(5)}")

print("\nSOLUCIONES EJERCICIO 5:")
print(f"user@example.com válido: {validar_email_solucion('user@example.com')}")