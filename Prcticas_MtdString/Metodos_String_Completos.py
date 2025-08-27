# =============================================
# MÉTODOS DE STRINGS EN PYTHON - GUÍA COMPLETA
# =============================================

print("=" * 65)
print("MÉTODOS DE STRINGS EN PYTHON - GUÍA COMPLETA")
print("=" * 65)

# String de ejemplo para las pruebas
texto_ejemplo = "  Python es un lenguaje de programación  "
texto_mayusculas = "PYTHON ES GENIAL"
texto_minusculas = "python es fácil"
texto_mixed = "PyThOn Es InCrEbLe"
texto_numeros = "12345"
texto_espacios = "   Hello   World   "
texto_special = "áéíóúñç"

print(f"Texto ejemplo: '{texto_ejemplo}'")
print(f"Texto mayúsculas: '{texto_mayusculas}'")
print(f"Texto minúsculas: '{texto_minusculas}'")
print(f"Texto mixed: '{texto_mixed}'")

# =============================================
# 1. MÉTODOS DE CONVERSIÓN DE CASE
# =============================================

print("\n" + "=" * 50)
print("1. MÉTODOS DE CONVERSIÓN DE CASE")
print("=" * 50)

# upper() - Convierte a mayúsculas
print(f"\nupper(): '{texto_minusculas.upper()}'")

# lower() - Convierte a minúsculas
print(f"lower(): '{texto_mayusculas.lower()}'")

# capitalize() - Primera letra en mayúscula, resto minúsculas
print(f"capitalize(): '{texto_mixed.capitalize()}'")

# title() - Cada palabra con primera letra en mayúscula
print(f"title(): '{texto_ejemplo.title()}'")

# swapcase() - Intercambia mayúsculas y minúsculas
print(f"swapcase(): '{texto_mixed.swapcase()}'")

# casefold() - Similar a lower() pero más agresivo para comparaciones
print(f"casefold(): '{texto_mixed.casefold()}'")

# =============================================
# 2. MÉTODOS DE BÚSQUEDA
# =============================================

print("\n" + "=" * 50)
print("2. MÉTODOS DE BÚSQUEDA")
print("=" * 50)

texto_busqueda = "Python es genial, Python es fácil"

# find() - Busca subcadena, devuelve posición o -1
print(f"\nfind('genial'): {texto_busqueda.find('genial')}")
print(f"find('Java'): {texto_busqueda.find('Java')}")

# index() - Busca subcadena, devuelve posición o error
print(f"index('genial'): {texto_busqueda.index('genial')}")

# rfind() - Busca desde el final
print(f"rfind('Python'): {texto_busqueda.rfind('Python')}")

# rindex() - Busca desde el final con error si no encuentra
print(f"rindex('Python'): {texto_busqueda.rindex('Python')}")

# count() - Cuenta ocurrencias
print(f"count('Python'): {texto_busqueda.count('Python')}")
print(f"count('es'): {texto_busqueda.count('es')}")

# startswith() - Verifica si empieza con
print(f"startswith('Python'): {texto_busqueda.startswith('Python')}")
print(f"startswith('Java'): {texto_busqueda.startswith('Java')}")

# endswith() - Verifica si termina con
print(f"endswith('fácil'): {texto_busqueda.endswith('fácil')}")
print(f"endswith('difícil'): {texto_busqueda.endswith('difícil')}")

# =============================================
# 3. MÉTODOS DE VALIDACIÓN
# =============================================

print("\n" + "=" * 50)
print("3. MÉTODOS DE VALIDACIÓN")
print("=" * 50)

# isalpha() - Solo letras
print(f"\nisalpha(): '{'abc'.isalpha()}' vs '{'abc123'.isalpha()}'")

# isnumeric() - Solo números
print(f"isnumeric(): '{'123'.isnumeric()}' vs '{'123abc'.isnumeric()}'")

# isalnum() - Letras y números
print(f"isalnum(): '{'abc123'.isalnum()}' vs '{'abc 123'.isalnum()}'")

# isdigit() - Solo dígitos
print(f"isdigit(): '{'123'.isdigit()}' vs '{'12.3'.isdigit()}'")

# isdecimal() - Solo decimales
print(f"isdecimal(): '{'123'.isdecimal()}' vs '{'12.3'.isdecimal()}'")

# isspace() - Solo espacios
print(f"isspace(): '{'   '.isspace()}' vs '{'hello'.isspace()}'")

# islower() - Todo minúsculas
print(f"islower(): '{'hello'.islower()}' vs '{'Hello'.islower()}'")

# isupper() - Todo mayúsculas
print(f"isupper(): '{'HELLO'.isupper()}' vs '{'Hello'.isupper()}'")

# istitle() - Formato título
print(f"istitle(): '{'Hello World'.istitle()}' vs '{'hello world'.istitle()}'")

# =============================================
# 4. MÉTODOS DE MANIPULACIÓN
# =============================================

print("\n" + "=" * 50)
print("4. MÉTODOS DE MANIPULACIÓN")
print("=" * 50)

# strip() - Elimina espacios al inicio y final
print(f"\nstrip(): '{texto_espacios.strip()}'")

# lstrip() - Elimina espacios al inicio
print(f"lstrip(): '{texto_espacios.lstrip()}'")

# rstrip() - Elimina espacios al final
print(f"rstrip(): '{texto_espacios.rstrip()}'")

# replace() - Reemplaza subcadenas
texto_reemplazo = "Me gusta Java"
print(f"replace(): '{texto_reemplazo.replace('Java', 'Python')}'")

# split() - Divide en lista
texto_split = "manzana,pera,naranja"
print(f"split(','): {texto_split.split(',')}")
print(f"split(): {'hola mundo'.split()}")

# rsplit() - Divide desde la derecha
print(f"rsplit(',', 1): {texto_split.rsplit(',', 1)}")

# splitlines() - Divide por líneas
texto_lineas = "Línea 1\nLínea 2\nLínea 3"
print(f"splitlines(): {texto_lineas.splitlines()}")

# partition() - Divide en 3 partes
print(f"partition('es'): {texto_ejemplo.partition('es')}")

# rpartition() - Divide desde la derecha
print(f"rpartition('es'): {texto_ejemplo.rpartition('es')}")

# =============================================
# 5. MÉTODOS DE UNIÓN Y RELLENO
# =============================================

print("\n" + "=" * 50)
print("5. MÉTODOS DE UNIÓN Y RELLENO")
print("=" * 50)

# join() - Une elementos con separador
lista = ["Python", "Java", "C++"]
print(f"\njoin(): {', '.join(lista)}")

# center() - Centra texto con relleno
print(f"center(20): '{'Hola'.center(20)}'")
print(f"center(20, '*'): '{'Hola'.center(20, '*')}'")

# ljust() - Alinea a izquierda con relleno
print(f"ljust(15): '{'Hola'.ljust(15)}'")
print(f"ljust(15, '-'): '{'Hola'.ljust(15, '-')}'")

# rjust() - Alinea a derecha con relleno
print(f"rjust(15): '{'Hola'.rjust(15)}'")
print(f"rjust(15, '+'): '{'Hola'.rjust(15, '+')}'")

# zfill() - Rellena con ceros a la izquierda
print(f"zfill(8): {'42'.zfill(8)}")
print(f"zfill(8): {'-42'.zfill(8)}")

# =============================================
# 6. MÉTODOS DE CODIFICACIÓN
# =============================================

print("\n" + "=" * 50)
print("6. MÉTODOS DE CODIFICACIÓN")
print("=" * 50)

# encode() - Codifica a bytes
texto_unicode = "áéíóúñ"
print(f"\nencode(): {texto_unicode.encode('utf-8')}")
print(f"encode('ascii', 'ignore'): {texto_unicode.encode('ascii', 'ignore')}")

# =============================================
# 7. MÉTODOS DE TRANSLACIÓN
# =============================================

print("\n" + "=" * 50)
print("7. MÉTODOS DE TRANSLACIÓN")
print("=" * 50)

# translate() - Traduce caracteres
tabla = str.maketrans('aeiou', '12345')
texto_traduccion = "hola mundo"
print(f"translate(): {texto_traduccion.translate(tabla)}")

# maketrans() - Crea tabla de traducción
tabla2 = str.maketrans({'a': 'A', 'e': 'E', 'i': 'I'})
print(f"translate() con dict: {'aeiou'.translate(tabla2)}")

# =============================================
# 8. MÉTODOS DE FORMATEO
# =============================================

print("\n" + "=" * 50)
print("8. MÉTODOS DE FORMATEO")
print("=" * 50)

# format() - Formatea string
nombre = "Ana"
edad = 25
print(f"\nformat(): {'Hola {}, tienes {} años'.format(nombre, edad)}")
print(f"format() con nombres: {'Hola {nombre}, tienes {edad} años'.format(nombre=nombre, edad=edad)}")

# format_map() - Formatea con mapping
datos = {'nombre': 'Carlos', 'edad': 30}
print(f"format_map(): {'Hola {nombre}, tienes {edad} años'.format_map(datos)}")

# =============================================
# 9. MÉTODOS ESPECIALES
# =============================================

print("\n" + "=" * 50)
print("9. MÉTODOS ESPECIALES")
print("=" * 50)

# expandtabs() - Expande tabs
texto_tabs = "Hola\tMundo\tPython"
print(f"\nexpandtabs(): '{texto_tabs.expandtabs(10)}'")

# =============================================
# 10. EJEMPLOS PRÁCTICOS COMBINADOS
# =============================================

print("\n" + "=" * 50)
print("10. EJEMPLOS PRÁCTICOS")
print("=" * 50)

# Ejemplo 1: Limpiar y formatear input de usuario
usuario_input = "  jUaN pErEz  "
nombre_limpio = usuario_input.strip().title()
print(f"Nombre formateado: '{nombre_limpio}'")

# Ejemplo 2: Validar email
email = "usuario@example.com"
if email.count('@') == 1 and not email.startswith('@') and not email.endswith('@'):
    print("Email válido")
else:
    print("Email inválido")

# Ejemplo 3: Contar palabras
texto_largo = "Python es un lenguaje de programación interpretado de alto nivel"
palabras = texto_largo.split()
print(f"Número de palabras: {len(palabras)}")

# Ejemplo 4: Enmascarar datos sensibles
tarjeta = "1234567890123456"
tarjeta_enmascarada = tarjeta[:4] + '*' * 8 + tarjeta[-4:]
print(f"Tarjeta enmascarada: {tarjeta_enmascarada}")

# Ejemplo 5: Generar username
nombre_completo = "María García López"
username = nombre_completo.lower().replace(' ', '_').replace('á', 'a').replace('é', 'e')
print(f"Username: {username}")

# =============================================
# 11. COMPARACIÓN DE MÉTODOS SIMILARES
# =============================================

print("\n" + "=" * 50)
print("11. COMPARACIÓN DE MÉTODOS SIMILARES")
print("=" * 50)

print("\nfind() vs index():")
print("find() devuelve -1 si no encuentra")
print("index() lanza ValueError si no encuentra")

print("\nisdigit() vs isnumeric() vs isdecimal():")
print("isdigit(): Solo dígitos 0-9")
print("isnumeric(): Incluye números Unicode")
print("isdecimal(): Solo caracteres decimales")

# =============================================
# 12. RESUMEN DE MÉTODOS MÁS USADOS
# =============================================

print("\n" + "=" * 50)
print("12. RESUMEN - MÉTODOS MÁS USADOS")
print("=" * 50)

metodos_importantes = [
    "lower()/upper()",
    "strip()/lstrip()/rstrip()",
    "split()/join()",
    "replace()",
    "find()/index()",
    "startswith()/endswith()",
    "format()",
    "count()"
]

for i, metodo in enumerate(metodos_importantes, 1):
    print(f"{i}. {metodo}")

print("\n" + "=" * 65)
print("¡FIN DE LA GUÍA DE MÉTODOS DE STRINGS!")
print("=" * 65)

# Información adicional
print(f"\n📊 Total de métodos mostrados: {len(dir(str)) - len([m for m in dir(str) if m.startswith('_')])}")
print("💡 Tip: Usa help(str.metodo) para más información sobre cualquier método")
print("🚀 Ejemplo: help(str.upper)")