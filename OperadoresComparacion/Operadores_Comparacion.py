"""
GUÍA COMPLETA DE OPERADORES DE COMPARACIÓN EN PYTHON
"""

print("=" * 60)
print("GUÍA DE OPERADORES DE COMPARACIÓN EN PYTHON")
print("=" * 60)

print("\n" + "=" * 40)
print("1. OPERADORES BÁSICOS")
print("=" * 40)

# Igualdad (==)
print("👉 IGUALDAD (==)")
print(f"5 == 5: {5 == 5}")          # True
print(f"5 == 3: {5 == 3}")          # False
print(f"'a' == 'a': {'a' == 'a'}")  # True
print(f"'a' == 'A': {'a' == 'A'}")  # False (case sensitive)

# Desigualdad (!=)
print("\n👉 DESIGUALDAD (!=)")
print(f"5 != 3: {5 != 3}")          # True
print(f"5 != 5: {5 != 5}")          # False
print(f"'a' != 'b': {'a' != 'b'}")  # True

# Mayor que (>)
print("\n👉 MAYOR QUE (>)")
print(f"10 > 5: {10 > 5}")          # True
print(f"5 > 10: {5 > 10}")          # False
print(f"5 > 5: {5 > 5}")            # False

# Menor que (<)
print("\n👉 MENOR QUE (<)")
print(f"5 < 10: {5 < 10}")          # True
print(f"10 < 5: {10 < 5}")          # False
print(f"5 < 5: {5 < 5}")            # False

# Mayor o igual que (>=)
print("\n👉 MAYOR O IGUAL QUE (>=)")
print(f"10 >= 5: {10 >= 5}")        # True
print(f"5 >= 10: {5 >= 10}")        # False
print(f"5 >= 5: {5 >= 5}")          # True

# Menor o igual que (<=)
print("\n👉 MENOR O IGUAL QUE (<=)")
print(f"5 <= 10: {5 <= 10}")        # True
print(f"10 <= 5: {10 <= 5}")        # False
print(f"5 <= 5: {5 <= 5}")          # True

print("\n" + "=" * 40)
print("2. COMPARACIONES CON DIFERENTES TIPOS DE DATOS")
print("=" * 40)

# Con strings (orden lexicográfico)
print("👉 COMPARACIÓN DE STRINGS:")
print(f"'abc' < 'def': {'abc' < 'def'}")    # True
print(f"'apple' < 'banana': {'apple' < 'banana'}")  # True
print(f"'Z' < 'a': {'Z' < 'a'}")            # True (ASCII: Z=90, a=97)

# Con listas
print("\n👉 COMPARACIÓN DE LISTAS:")
print(f"[1, 2, 3] == [1, 2, 3]: {[1, 2, 3] == [1, 2, 3]}")  # True
print(f"[1, 2, 3] == [1, 3, 2]: {[1, 2, 3] == [1, 3, 2]}")  # False

# Con diferentes tipos (generalmente False)
print("\n👉 COMPARACIÓN ENTRE DIFERENTES TIPOS:")
print(f"5 == '5': {5 == '5'}")              # False
print(f"5.0 == 5: {5.0 == 5}")              # True (coerción numérica)

print("\n" + "=" * 40)
print("3. OPERADORES DE IDENTIDAD (is, is not)")
print("=" * 40)

# is (mismo objeto en memoria)
print("👉 OPERADOR IS (mismo objeto):")
a = [1, 2, 3]
b = [1, 2, 3]  # Objeto diferente con mismo contenido
c = a          # Mismo objeto

print(f"a is b: {a is b}")      # False (objetos diferentes)
print(f"a is c: {a is c}")      # True (mismo objeto)
print(f"a == b: {a == b}")      # True (contenido igual)

# is not (diferente objeto)
print("\n👉 OPERADOR IS NOT (diferente objeto):")
print(f"a is not b: {a is not b}")  # True
print(f"a is not c: {a is not c}")  # False

# None comparisons
print("\n👉 COMPARACIONES CON NONE:")
x = None
print(f"x is None: {x is None}")        # True (SIEMPRE usar is con None)
print(f"x == None: {x == None}")        # True (pero no recomendado)

print("\n" + "=" * 40)
print("4. OPERADORES DE PERTENENCIA (in, not in)")
print("=" * 40)

# in (está contenido en)
print("👉 OPERADOR IN (pertenencia):")
texto = "Python programming"
print(f"'Python' in texto: {'Python' in texto}")        # True
print(f"'python' in texto: {'python' in texto}")        # False (case sensitive)
print(f"'z' in texto: {'z' in texto}")                  # False

lista = [1, 2, 3, 4, 5]
print(f"3 in lista: {3 in lista}")                      # True
print(f"10 in lista: {10 in lista}")                    # False

# not in (no está contenido en)
print("\n👉 OPERADOR NOT IN (no pertenencia):")
print(f"'Java' not in texto: {'Java' not in texto}")    # True
print(f"'Python' not in texto: {'Python' not in texto}") # False
print(f"10 not in lista: {10 not in lista}")            # True

print("\n" + "=" * 40)
print("5. COMPARACIONES EN CADENA (CHAINED COMPARISONS)")
print("=" * 40)

# Comparaciones encadenadas
print("👉 COMPARACIONES ENCADENADAS:")
edad = 25
print(f"18 <= edad <= 65: {18 <= edad <= 65}")          # True

x = 5
print(f"1 < x < 10: {1 < x < 10}")                      # True
print(f"0 < x < 3: {0 < x < 3}")                        # False

# Equivalente a and
print("\n👉 EQUIVALENTE CON AND:")
print(f"1 < x and x < 10: {1 < x and x < 10}")          # True

print("\n" + "=" * 40)
print("6. PRECEDENCIA DE OPERADORES")
print("=" * 40)

print("👉 ORDEN DE PRECEDENCIA (de mayor a menor):")
print("1. ** (exponenciación)")
print("2. * / // % (multiplicación, división)")
print("3. + - (suma, resta)")
print("4. < <= > >= (comparaciones)")
print("5. == != (igualdad)")
print("6. is, is not, in, not in (identidad, pertenencia)")
print("7. not (lógico NOT)")
print("8. and (lógico AND)")
print("9. or (lógico OR)")

print("\n👉 EJEMPLOS DE PRECEDENCIA:")
resultado = 5 + 3 * 2 > 10 and 4 == 4
print(f"5 + 3 * 2 > 10 and 4 == 4: {resultado}")
# Paso a paso: 3*2=6, 5+6=11, 11>10=True, 4==4=True, True and True=True

print("\n" + "=" * 40)
print("7. COMPARACIONES CON BOOLEANOS")
print("=" * 40)

# Booleanos son subclases de enteros (True=1, False=0)
print("👉 COMPARACIONES BOOLEANAS:")
print(f"True == 1: {True == 1}")            # True
print(f"False == 0: {False == 0}")          # True
print(f"True > False: {True > False}")      # True (1 > 0)

print(f"True + True: {True + True}")        # 2
print(f"True * 5: {True * 5}")              # 5

print("\n" + "=" * 40)
print("8. COMPARACIONES CON FLOAT E INT")
print("=" * 40)

print("👉 COMPARACIONES NUMÉRICAS MIXTAS:")
print(f"5 == 5.0: {5 == 5.0}")              # True
print(f"5.5 > 5: {5.5 > 5}")                # True
print(f"5.0 < 6: {5.0 < 6}")                # True

print("\n👉 PRECISIÓN DECIMAL:")
print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")  # False (¡sorpresa!)
print(f"0.1 + 0.2: {0.1 + 0.2}")                # 0.30000000000000004

# Solución para comparaciones float
print(f"abs((0.1 + 0.2) - 0.3) < 1e-10: {abs((0.1 + 0.2) - 0.3) < 1e-10}")  # True

print("\n" + "=" * 40)
print("9. EJEMPLOS PRÁCTICOS")
print("=" * 40)

# Validación de rango
def validar_edad(edad):
    return 0 <= edad <= 120

print(f"Edad 25 válida: {validar_edad(25)}")
print(f"Edad 150 válida: {validar_edad(150)}")

# Validación de string
def validar_email(email):
    return '@' in email and '.' in email and len(email) > 5

print(f"Email 'a@b.com' válido: {validar_email('a@b.com')}")
print(f"Email 'invalid' válido: {validar_email('invalid')}")

# Comparación de listas
def son_iguales(lista1, lista2):
    return lista1 == lista2

print(f"Listas iguales: {son_iguales([1, 2], [1, 2])}")
print(f"Listas diferentes: {son_iguales([1, 2], [2, 1])}")

print("\n" + "=" * 40)
print("10. TRUCOS Y CONSEJOS")
print("=" * 40)

print("👉 USAR PARÉNTESIS PARA CLARIDAD:")
resultado = (5 + 3) * 2 > (10 - 4) and (4 == 4)
print(f"(5 + 3) * 2 > (10 - 4) and (4 == 4): {resultado}")

print("\n👉 EVITAR COMPARACIONES COMPLEJAS EN UNA LÍNEA:")
# Mejor dividir en varias líneas
condicion1 = (5 + 3) * 2 > (10 - 4)
condicion2 = 4 == 4
resultado = condicion1 and condicion2

print("\n👉 USAR is SOLO PARA None, True, False:")
x = None
print(f"x is None: {x is None}")  # ✅ Correcto
print(f"x == None: {x == None}")  # ❌ No recomendado

print("\n👉 CUIDADO CON COMPARACIONES DE OBJETOS MUTABLES:")
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
print(f"lista1 == lista2: {lista1 == lista2}")  # True (contenido)
print(f"lista1 is lista2: {lista1 is lista2}")  # False (objetos diferentes)