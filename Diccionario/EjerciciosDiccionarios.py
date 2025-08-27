"""
30 EJERCICIOS DE DICCIONARIOS EN PYTHON
"""

# ==========================================================================
# EJERCICIOS BÁSICOS (1-10)
# ==========================================================================

def ejercicio_1():
    """Crea un diccionario vacío"""
    return {}

def ejercicio_2():
    """Crea un diccionario con 3 pares clave-valor de tu elección"""
    return {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

def ejercicio_3():
    """Accede al valor de la clave 'edad' en el diccionario persona"""
    persona = {"nombre": "Carlos", "edad": 30, "ciudad": "Barcelona"}
    return persona["edad"]

def ejercicio_4():
    """Usa get() para obtener el valor de 'ciudad' con valor por defecto 'Desconocida'"""
    persona = {"nombre": "Laura", "edad": 28}
    return persona.get("ciudad", "Desconocida")

def ejercicio_5():
    """Verifica si la clave 'email' existe en el diccionario"""
    usuario = {"nombre": "Juan", "edad": 35}
    return "email" in usuario

def ejercicio_6():
    """Añade una nueva clave 'país' con valor 'España'"""
    persona = {"nombre": "Ana", "edad": 25}
    persona["país"] = "España"
    return persona

def ejercicio_7():
    """Actualiza la edad a 26 años"""
    persona = {"nombre": "Carlos", "edad": 25}
    persona["edad"] = 26
    return persona

def ejercicio_8():
    """Elimina la clave 'ciudad' usando pop()"""
    persona = {"nombre": "Laura", "edad": 28, "ciudad": "Sevilla"}
    persona.pop("ciudad")
    return persona

def ejercicio_9():
    """Obtén todas las claves del diccionario"""
    persona = {"nombre": "Juan", "edad": 35, "ciudad": "Valencia"}
    return list(persona.keys())

def ejercicio_10():
    """Obtén todos los valores del diccionario"""
    persona = {"nombre": "Maria", "edad": 29, "ciudad": "Bilbao"}
    return list(persona.values())

# ==========================================================================
# EJERCICIOS INTERMEDIOS (11-20)
# ==========================================================================

def ejercicio_11():
    """Combina dos diccionarios usando update()"""
    dic1 = {"a": 1, "b": 2}
    dic2 = {"c": 3, "d": 4}
    dic1.update(dic2)
    return dic1

def ejercicio_12():
    """Crea una copia del diccionario (no referencia)"""
    original = {"a": 1, "b": 2}
    copia = original.copy()
    copia["c"] = 3
    return original, copia

def ejercicio_13():
    """Cuenta la frecuencia de letras en la palabra 'python'"""
    palabra = "python"
    frecuencia = {}
    for letra in palabra:
        frecuencia[letra] = frecuencia.get(letra, 0) + 1
    return frecuencia

def ejercicio_14():
    """Invierte un diccionario (claves → valores, valores → claves)"""
    original = {"a": 1, "b": 2, "c": 3}
    invertido = {v: k for k, v in original.items()}
    return invertido

def ejercicio_15():
    """Filtra un diccionario para mantener solo valores pares"""
    numeros = {"a": 1, "b": 2, "c": 3, "d": 4}
    filtrado = {k: v for k, v in numeros.items() if v % 2 == 0}
    return filtrado

def ejercicio_16():
    """Suma todos los valores de un diccionario"""
    precios = {"manzana": 1.5, "naranja": 2.0, "plátano": 1.0}
    return sum(precios.values())

def ejercicio_17():
    """Encuentra la clave con el valor máximo"""
    edades = {"Ana": 25, "Carlos": 30, "Laura": 28}
    return max(edades, key=edades.get)

def ejercicio_18():
    """Concatena dos diccionarios (Python 3.9+)"""
    dic1 = {"a": 1, "b": 2}
    dic2 = {"c": 3, "d": 4}
    return dic1 | dic2

def ejercicio_19():
    """Crea un diccionario con fromkeys()"""
    claves = ["nombre", "edad", "ciudad"]
    return dict.fromkeys(claves, "desconocido")

def ejercicio_20():
    """Usa setdefault() para agregar una clave si no existe"""
    persona = {"nombre": "Ana", "edad": 25}
    ciudad = persona.setdefault("ciudad", "Madrid")
    return persona, ciudad

# ==========================================================================
# EJERCICIOS AVANZADOS (21-30)
# ==========================================================================

def ejercicio_21():
    """Diccionario anidado: accede al nombre del primer empleado"""
    empresa = {
        "empleados": [
            {"nombre": "Ana", "departamento": "IT"},
            {"nombre": "Carlos", "departamento": "RH"}
        ]
    }
    return empresa["empleados"][0]["nombre"]

def ejercicio_22():
    """Agrupa palabras por su longitud"""
    palabras = ["python", "java", "c", "javascript", "go"]
    grupos = {}
    for palabra in palabras:
        longitud = len(palabra)
        if longitud not in grupos:
            grupos[longitud] = []
        grupos[longitud].append(palabra)
    return grupos

def ejercicio_23():
    """Combina dos listas en un diccionario"""
    claves = ["a", "b", "c"]
    valores = [1, 2, 3]
    return dict(zip(claves, valores))

def ejercicio_24():
    """Diccionario de diccionarios: encuentra el salario máximo"""
    empleados = {
        "emp1": {"nombre": "Ana", "salario": 30000},
        "emp2": {"nombre": "Carlos", "salario": 35000},
        "emp3": {"nombre": "Laura", "salario": 32000}
    }
    return max(emp["salario"] for emp in empleados.values())

def ejercicio_25():
    """Comprueba si todos los valores son mayores que 0"""
    numeros = {"a": 1, "b": 2, "c": 3, "d": 0}
    return all(valor > 0 for valor in numeros.values())

def ejercicio_26():
    """Ordena un diccionario por valores"""
    edades = {"Ana": 25, "Carlos": 30, "Laura": 28}
    return dict(sorted(edades.items(), key=lambda x: x[1]))

def ejercicio_27():
    """Encuentra claves comunes entre dos diccionarios"""
    dic1 = {"a": 1, "b": 2, "c": 3}
    dic2 = {"b": 2, "c": 3, "d": 4}
    return dic1.keys() & dic2.keys()

def ejercicio_28():
    """Merge de diccionarios con preferencia al segundo"""
    dic1 = {"a": 1, "b": 2}
    dic2 = {"b": 3, "c": 4}
    return {**dic1, **dic2}

def ejercicio_29():
    """Diccionario con valores por defecto (defaultdict)"""
    from collections import defaultdict
    contador = defaultdict(int)
    palabra = "python"
    for letra in palabra:
        contador[letra] += 1
    return dict(contador)

def ejercicio_30():
    """Convierte una lista de tuplas en diccionario"""
    tuplas = [("a", 1), ("b", 2), ("c", 3)]
    return dict(tuplas)

# ==========================================================================
# TEST DE TODOS LOS EJERCICIOS
# ==========================================================================

if __name__ == "__main__":
    print("Ejecutando ejercicios...")
    for i in range(1, 31):
        funcion = globals()[f"ejercicio_{i}"]
        resultado = funcion()
        print(f"Ejercicio {i}: {resultado}")