"""
GUÍA COMPLETA DE OPERADORES LÓGICOS EN PYTHON
"""

print("=" * 60)
print("GUÍA DE OPERADORES LÓGICOS EN PYTHON")
print("=" * 60)

print("\n" + "=" * 40)
print("1. OPERADORES LÓGICOS BÁSICOS")
print("=" * 40)

# Operador AND
print("👉 OPERADOR AND (y):")
print(f"True and True: {True and True}")    # True
print(f"True and False: {True and False}")  # False
print(f"False and True: {False and True}")  # False
print(f"False and False: {False and False}") # False

# Operador OR
print("\n👉 OPERADOR OR (o):")
print(f"True or True: {True or True}")      # True
print(f"True or False: {True or False}")    # True
print(f"False or True: {False or True}")    # True
print(f"False or False: {False or False}")  # False

# Operador NOT
print("\n👉 OPERADOR NOT (no):")
print(f"not True: {not True}")              # False
print(f"not False: {not False}")            # True

print("\n" + "=" * 40)
print("2. TABLAS DE VERDAD COMPLETAS")
print("=" * 40)

print("TABLA DE VERDAD AND:")
print("A\tB\tA and B")
print("True\tTrue\t", True and True)
print("True\tFalse\t", True and False)
print("False\tTrue\t", False and True)
print("False\tFalse\t", False and False)

print("\nTABLA DE VERDAD OR:")
print("A\tB\tA or B")
print("True\tTrue\t", True or True)
print("True\tFalse\t", True or False)
print("False\tTrue\t", False or True)
print("False\tFalse\t", False or False)

print("\nTABLA DE VERDAD NOT:")
print("A\tnot A")
print("True\t", not True)
print("False\t", not False)

print("\n" + "=" * 40)
print("3. OPERADORES LÓGICOS CON VALORES NO BOOLEANOS")
print("=" * 40)

print("👉 AND DEVUELVE EL ÚLTIMO VALOR 'TRUTHY' O EL PRIMER 'FALSY':")
print(f"10 and 20: {10 and 20}")            # 20 (ambos truthy, devuelve el último)
print(f"0 and 20: {0 and 20}")              # 0 (primer falsy)
print(f"10 and 0: {10 and 0}")              # 0 (segundo falsy)
print(f"'hola' and 'mundo': {'hola' and 'mundo'}")  # 'mundo'

print("\n👉 OR DEVUELVE EL PRIMER VALOR 'TRUTHY' O EL ÚLTIMO 'FALSY':")
print(f"10 or 20: {10 or 20}")              # 10 (primer truthy)
print(f"0 or 20: {0 or 20}")                # 20 (segundo truthy)
print(f"0 or 0.0: {0 or 0.0}")              # 0.0 (ambos falsy, devuelve el último)
print(f"None or 'valor': {None or 'valor'}") # 'valor'

print("\n👉 NOT SIEMPRE DEVUELVE BOOLEANO:")
print(f"not 10: {not 10}")                  # False (10 es truthy)
print(f"not 0: {not 0}")                    # True (0 es falsy)
print(f"not 'hola': {not 'hola'}")          # False
print(f"not '': {not ''}")                  # True

print("\n" + "=" * 40)
print("4. PRECEDENCIA DE OPERADORES LÓGICOS")
print("=" * 40)

print("ORDEN DE PRECEDENCIA (de mayor a menor):")
print("1. ** (exponenciación)")
print("2. * / // % (multiplicación, división)")
print("3. + - (suma, resta)")
print("4. < <= > >= (comparaciones)")
print("5. == != (igualdad)")
print("6. not (lógico NOT)")
print("7. and (lógico AND)")
print("8. or (lógico OR)")

print("\n👉 EJEMPLOS DE PRECEDENCIA:")
resultado1 = not True and False or True
print(f"not True and False or True: {resultado1}")
# not True = False, False and False = False, False or True = True

resultado2 = 5 > 3 and 10 < 20 or not 1 == 0
print(f"5 > 3 and 10 < 20 or not 1 == 0: {resultado2}")
# 5>3=True, 10<20=True, 1==0=False, not False=True, True and True=True, True or True=True

print("\n" + "=" * 40)
print("5. USO DE PARÉNTESIS PARA CONTROLAR PRECEDENCIA")
print("=" * 40)

print("👉 SIN PARÉNTESIS:")
resultado = not True and False or True
print(f"not True and False or True: {resultado}")  # True

print("👉 CON PARÉNTESIS:")
resultado1 = not (True and False) or True
print(f"not (True and False) or True: {resultado1}")  # True

resultado2 = not True and (False or True)
print(f"not True and (False or True): {resultado2}")  # False

resultado3 = (not True) and (False or True)
print(f"(not True) and (False or True): {resultado3}")  # False

print("\n" + "=" * 40)
print("6. CORTO CIRCUITO (SHORT-CIRCUIT EVALUATION)")
print("=" * 40)

print("👉 AND: Se detiene en el primer Falsy")
def funcion_lenta():
    print("   Esta función se ejecutó")
    return True

print("Corto circuito con AND:")
resultado = False and funcion_lenta()  # No ejecuta funcion_lenta
print(f"Resultado: {resultado}")

print("\n👉 OR: Se detiene en el primer Truthy")
print("Corto circuito con OR:")
resultado = True or funcion_lenta()  # No ejecuta funcion_lenta
print(f"Resultado: {resultado}")

print("\n👉 EJEMPLO PRÁCTICO DE CORTO CIRCUITO:")
lista = []
# Evita error porque 0 < len(lista) no se evalúa si lista es None
if lista is not None and 0 < len(lista):
    print("Lista tiene elementos")
else:
    print("Lista vacía o None")

print("\n" + "=" * 40)
print("7. COMBINACIÓN CON OPERADORES DE COMPARACIÓN")
print("=" * 40)

# Validaciones complejas
edad = 25
tiene_licencia = True
tiene_seguro = False

print("👉 VALIDACIÓN MÚLTIPLE:")
puede_conducir = edad >= 18 and tiene_licencia and tiene_seguro
print(f"Puede conducir: {puede_conducir}")  # False (por el seguro)

# Validación con OR
tiene_permiso = True
tiene_pasaporte = True
tiene_cedula = False
puede_viajar = tiene_pasaporte or tiene_cedula
print(f"Puede viajar: {puede_viajar}")  # True

# Combinación AND/OR
es_adulto = edad >= 18
puede_entrar = es_adulto or (edad >= 16 and tiene_permiso)  # tiene_permiso no definido, pero muestra estructura

print("\n" + "=" * 40)
print("8. OPERADORES LÓGICOS EN EXPRESIONES CONDICIONALES")
print("=" * 40)

# En if statements
numero = 15
if numero > 10 and numero % 2 == 0:
    print(f"{numero} es mayor que 10 y par")
elif numero > 10 and numero % 2 != 0:
    print(f"{numero} es mayor que 10 e impar")
else:
    print(f"{numero} es 10 o menor")

# En while loops
contador = 0
max_intentos = 3
exito = 10
while contador < max_intentos and not exito:  # éxito no definido, ejemplo
    print(f"Intento {contador + 1}")
    contador += 1

print("\n" + "=" * 40)
print("9. OPERADORES LÓGICOS CON COLECCIONES")
print("=" * 40)

lista = [1, 2, 3]
lista_vacia = []
diccionario = {"a": 1}

print("👉 CON LISTAS:")
print(f"lista and lista_vacia: {lista and lista_vacia}")  # [] (último falsy)
print(f"lista_vacia and lista: {lista_vacia and lista}")  # [] (primer falsy)
print(f"lista or lista_vacia: {lista or lista_vacia}")    # [1,2,3] (primer truthy)
print(f"lista_vacia or lista: {lista_vacia or lista}")    # [1,2,3] (segundo truthy)

print("\n👉 CON DICCIONARIOS:")
print(f"diccionario or {{}}: {diccionario or {}}")        # {'a': 1}
print(f"not lista_vacia: {not lista_vacia}")              # True

print("\n" + "=" * 40)
print("10. FUNCIONES ALL() Y ANY()")
print("=" * 40)

print("👉 ALL(): True si TODOS los elementos son Truthy")
print(f"all([True, True, True]): {all([True, True, True])}")  # True
print(f"all([True, False, True]): {all([True, False, True])}") # False
print(f"all([1, 2, 3]): {all([1, 2, 3])}")                  # True
print(f"all([1, 0, 3]): {all([1, 0, 3])}")                  # False

print("\n👉 ANY(): True si ALGÚN elemento es Truthy")
print(f"any([False, False, True]): {any([False, False, True])}")  # True
print(f"any([False, False, False]): {any([False, False, False])}") # False
print(f"any([0, 0, 1]): {any([0, 0, 1])}")                    # True
print(f"any([0, 0, 0]): {any([0, 0, 0])}")                    # False

print("\n" + "=" * 40)
print("11. EJEMPLOS PRÁCTICOS")
print("=" * 40)

# Validación de formulario
def validar_formulario(nombre, email, edad):
    return (
        nombre is not None and
        len(nombre.strip()) > 0 and
        '@' in email and
        '.' in email and
        edad >= 18 and
        edad <= 120
    )

print(f"Formulario válido: {validar_formulario('Juan', 'juan@email.com', 25)}")

# Sistema de permisos
def tiene_acceso(usuario, es_admin, tiene_permiso):
    return es_admin or (usuario is not None and tiene_permiso)

print(f"Acceso concedido: {tiene_acceso('user123', False, True)}")

print("\n" + "=" * 40)
print("12. TRUCOS Y MEJORES PRÁCTICAS")
print("=" * 40)

print("👉 USAR PARÉNTESIS PARA CLARIDAD:")
# En lugar de: a and b or c and d
# Mejor: (a and b) or (c and d)

print("👉 EVITAR EXPRESIONES MUY COMPLEJAS:")
# Mejor dividir en variables intermedias
condicion1 = edad >= 18
condicion2 = tiene_licencia
condicion3 = tiene_seguro
resultado = condicion1 and condicion2 and condicion3

print("👉 APROVECHAR CORTO CIRCUITO:")
# Para evitar errores y mejorar performance
if lista is not None and len(lista) > 0:
    print("Lista válida con elementos")

print("👉 USAR all() Y any() PARA MÚLTIPLES CONDICIONES:")
condiciones = [edad >= 18, tiene_licencia, tiene_seguro]
puede_conducir = all(condiciones)