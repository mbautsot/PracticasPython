# =============================================
# 30 PROBLEMAS COMPLEJOS DE MÉTODOS DE STRINGS
# =============================================
import unicodedata

print("=" * 50)
print("30 PROBLEMAS DE MÉTODOS DE STRINGS")
print("=" * 50)


# Problema 1
def problema_1(email:str)-> bool:
    """
    VALIDACIÓN DE EMAIL:
    Crea una función que valide si un email es válido.
    Debe contener un '@', no empezar ni terminar con '@',
    y tener al menos un punto después del '@'.
    """
    #email = "usuario@dominio.com"
    # Tu código aquí
    valid_email = True

    if '@' not in email:
        valid_email = False
    if email.startswith('@') or email.endswith('@'):
        valid_email = False

        # Dividir en usuario y dominio
    partes = email.split('@')
    if len(partes) != 2:
        valid_email = False

    dominio = partes[1]
    if '.' not in dominio:
        valid_email = False

    return valid_email


# Problema 2
def problema_2(email:str):
    """
    EXTRACCIÓN DE DOMINIO:
    Dado un email, extrae solo el dominio (lo que va después del '@').
    """
    #email = "usuario@empresa.com.mx"
    # Tu código aquí
    dominio = email.split('@')[1]

    return dominio


# Problema 3
def problema_3(tarjeta:str):
    """
    ENMASCARAR TARJETA:
    Toma un número de tarjeta y enmascara todos los dígitos
    excepto los primeros 4 y últimos 4.
    """
   # numTarjeta = "1234567890123456"
    # Tu código aquí
    trj =''
    if len(tarjeta)< 16:
        trj = 'Número de tarjeta invalido, Debe de tener 16 digitos'
    elif not tarjeta.isdigit():
        trj ='Número de tarjeta invalido, Solo debe contener dígitos'
    else:
        return tarjeta[:4] + '*' * 8 + tarjeta[-4:]

    return trj


# Problema 4
def problema_4(telefono:str):
    """
    FORMATEAR NÚMERO TELEFÓNICO:
    Convierte '5512345678' a formato '(55) 1234-5678'
    """
    #telefono = "5512345678"
    # Tu código aquí
    # Reultado esperado "(55) 1234-5678"


    if(not telefono.isdigit()) or (len(telefono) != 10):
        return 'El numero telefonico es erroneo'

    return f'({telefono[:2]}) {telefono[2:6]}-{telefono[6:]}'


# Problema 5
def problema_5(texto:str) -> int: #El -> int se llama type hint de retorno o annotation de retorno.

    """
    CONTADOR DE PALABRAS:
    Cuenta cuántas palabras hay en un texto, ignorando espacios extras.
    """
    # STRIP Eliminar espacios al inicio y final, luego dividir por espacios
    #"  Python   es   un   lenguaje   increíble  "
    #texto_strip = texto.strip()
    #print(texto_strip)#Python   es   un   lenguaje   increíble (SIN ESPACIOS INICIO Y FINAL)
    #texto_split = texto_strip.split()
    #print(texto_split) #Divide el texto en una lista de palabras, ignorando múltiples espacios entre palabras
    # Tu código aquí
    return len(texto.strip().split())


# Problema 6
def problema_6(frase:str) -> str:
    """
    INVERSIÓN DE PALABRAS:
    Invierte el orden de las palabras en una frase.
    "hola mundo" -> "mundo hola"
    """
    #frase = "Python es genial"
    # Tu código aquí
   # frase = frase.split()
   # frase.reverse()
   #La clave es usar ' '.join() para convertir la lista de palabras de vuelta a un string, uniéndolas con espacios.
   # return ' '.join(frase)

    #VERSION MAS COMPACTA
    return ' '.join(reversed(frase.split()))


# Problema 7
def problema_7(texto:str) -> str:
    """
    ELIMINAR ACENTOS:
    Remueve acentos y caracteres especiales de un texto.
    """
    texto = "áéíóúñÑçÇ"
    # Tu código aquí
    mapa_caracteres_especiales = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
        'ñ': 'n', 'ç': 'c',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'À': 'A', 'È': 'E', 'Ì': 'I', 'Ò': 'O', 'Ù': 'U',
        'Ä': 'A', 'Ë': 'E', 'Ï': 'I', 'Ö': 'O', 'Ü': 'U',
        'Â': 'A', 'Ê': 'E', 'Î': 'I', 'Ô': 'O', 'Û': 'U',
        'Ñ': 'N', 'Ç': 'C'
    }

    txt_sinacentos = []

    for caracter in texto:
        if caracter in mapa_caracteres_especiales:
            print(f'caracter : {caracter}')
            txt_sinacentos.append(mapa_caracteres_especiales[caracter])
        else:
            print(f'else caracter : {caracter}')
            txt_sinacentos.append(caracter)

    return ''.join(txt_sinacentos)


'''
📚 Explicación detallada:
1. resultado = []
Creamos una lista vacía donde guardaremos los caracteres procesados

Es como un "contenedor temporal" para el resultado

2. for caracter in texto:
texto: Es el string de entrada (ej: "café")

caracter: Variable que toma cada letra individual:

1ª iteración: caracter = "c"

2ª iteración: caracter = "a"

3ª iteración: caracter = "f"

4ª iteración: caracter = "é"

3. if caracter in mapa_acentos:
mapa_acentos: ¡SÍ! Es un diccionario (key-value pairs)

in: Verifica si la clave existe en el diccionario

Ejemplo: "é" in mapa_acentos → True (porque "é" es una clave)

4. resultado.append(mapa_acentos[caracter])
mapa_acentos[caracter]: Accede al valor correspondiente a la clave

Ejemplo: mapa_acentos["é"] → devuelve "e"

resultado.append("e"): Agrega "e" a la lista

5. else: resultado.append(caracter)
Si el carácter NO está en el diccionario (no tiene acento)

Lo agregamos tal cual a la lista

Ejemplo: "c" → no está en mapa_acentos → se agrega "c"

6. return ''.join(resultado)
resultado: Lista con caracteres procesados → ["c", "a", "f", "e"]

''.join(resultado): Une todos los elementos de la lista en un string

Resultado final: "cafe"


'''

# Problema 8
def problema_8():
    """
    GENERAR USERNAME:
    Crea un username a partir de nombre y apellido.
    "Juan Pérez" -> "juan.perez"
    """
    nombre = "María García López"
    # Tu código aquí
    return "maria.garcia.lopez"


# Problema 9
def problema_9():
    """
    VALIDAR CONTRASEÑA:
    Verifica que una contraseña tenga al menos:
    8 caracteres, 1 mayúscula, 1 minúscula, 1 número, 1 especial.
    """
    password = "Passw0rd!"
    # Tu código aquí
    return True


# Problema 10
def problema_10():
    """
    EXTRACCIÓN DE ARCHIVO:
    Dada una ruta, extrae solo el nombre del archivo sin extensión.
    "/ruta/al/archivo/documento.pdf" -> "documento"
    """
    ruta = "C:/Users/Docs/informe_final.docx"
    # Tu código aquí
    return "informe_final"


# Problema 11
def problema_11():
    """
    NORMALIZAR TEXTO:
    Convierte texto a formato título, pero manteniendo
    artículos en minúscula (el, la, los, las, de, del).
    """
    texto = "el señor de los anillos"
    # Tu código aquí
    return "El Señor de los Anillos"


# Problema 12
def problema_12():
    """
    CONTAR VOCALES Y CONSONANTES:
    Cuenta cuántas vocales y consonantes hay en un texto.
    """
    texto = "Python Programming"
    # Tu código aquí
    return (4, 11)  # (vocales, consonantes)


# Problema 13
def problema_13():
    """
    VERIFICAR PALÍNDROMO:
    Determina si una palabra es palíndromo (se lee igual al derecho y al revés).
    """
    palabra = "reconocer"
    # Tu código aquí
    return True


# Problema 14
def problema_14():
    """
    EXTRACCIÓN DE DATOS:
    Extrae el nombre y dominio de una lista de emails.
    """
    emails = ["ana@company.com", "pedro@empresa.org", "lucia@corp.net"]
    # Tu código aquí
    return [("ana", "company.com"), ("pedro", "empresa.org"), ("lucia", "corp.net")]


# Problema 15
def problema_15():
    """
    FORMATEAR MONEDA:
    Convierte un número a formato de moneda con separadores.
    1234567.89 -> "$1,234,567.89"
    """
    monto = 9876543.21
    # Tu código aquí
    return "$9,876,543.21"


# Problema 16
def problema_16():
    """
    CODIFICAR URL:
    Reemplaza espacios por %20 y caracteres especiales por su encoding.
    """
    url = "mi documento final.pdf"
    # Tu código aquí
    return "mi%20documento%20final.pdf"


# Problema 17
def problema_17():
    """
    ANALIZAR LOG:
    Extrae las direcciones IP de un log de servidor.
    """
    log = "192.168.1.1 - GET /index.html\n10.0.0.2 - POST /login.php"
    # Tu código aquí
    return ["192.168.1.1", "10.0.0.2"]


# Problema 18
def problema_18():
    """
    GENERAR SLUG:
    Crea un slug para URL a partir de un título.
    "Cómo aprender Python en 30 días" -> "como-aprender-python-en-30-dias"
    """
    titulo = "Guía Completa de Métodos en Python"
    # Tu código aquí
    return "guia-completa-de-metodos-en-python"


# Problema 19
def problema_19():
    """
    VALIDAR ISBN:
    Verifica si un código ISBN-10 es válido.
    """
    isbn = "0-306-40615-2"
    # Tu código aquí
    return True


# Problema 20
def problema_20():
    """
    EXTRACCIÓN DE HASHTAGS:
    Extrae todos los hashtags de un texto.
    """
    texto = "Me encanta #Python y #DataScience #Aprendiendo"
    # Tu código aquí
    return ["#Python", "#DataScience", "#Aprendiendo"]


# Problema 21
def problema_21():
    """
    NORMALIZAR FECHA:
    Convierte fecha de formato "dd/mm/yyyy" a "yyyy-mm-dd"
    """
    fecha = "25/12/2024"
    # Tu código aquí
    return "2024-12-25"


# Problema 22
def problema_22():
    """
    CONTAR OCURRENCIAS DE PALABRA:
    Cuenta cuántas veces aparece cada palabra en un texto.
    """
    texto = "python es genial python es poderoso"
    # Tu código aquí
    return {"python": 2, "es": 2, "genial": 1, "poderoso": 1}


# Problema 23
def problema_23():
    """
    REMOVER HTML TAGS:
    Elimina todas las etiquetas HTML de un texto.
    """
    html = "<div><p>Hola <b>mundo</b></p></div>"
    # Tu código aquí
    return "Hola mundo"


# Problema 24
def problema_24():
    """
    GENERAR ACRÓNIMO:
    Crea un acrónimo a partir de un nombre.
    "World Health Organization" -> "WHO"
    """
    nombre = "Asynchronous JavaScript and XML"
    # Tu código aquí
    return "AJAX"


# Problema 25
def problema_25():
    """
    VALIDAR PLACA:
    Verifica si una placa de auto tiene formato válido (3 letras + 3 números).
    """
    placa = "ABC123"
    # Tu código aquí
    return True


# Problema 26
def problema_26():
    """
    EXTRACCIÓN DE DATOS CSV:
    Extrae la segunda columna de una línea CSV.
    """
    csv_line = "Juan,Pérez,25,Engineer"
    # Tu código aquí
    return "Pérez"


# Problema 27
def problema_27():
    """
    CODIFICACIÓN CESAR:
    Aplica cifrado César con desplazamiento 3.
    "abc" -> "def"
    """
    texto = "hola mundo"
    # Tu código aquí
    return "krod pxqgr"


# Problema 28
def problema_28():
    """
    NORMALIZAR NÚMERO:
    Remueve todos los caracteres no numéricos de un número telefónico.
    "+52 (55) 1234-5678" -> "525512345678"
    """
    telefono = "+1 (800) 555-1234"
    # Tu código aquí
    return "18005551234"


# Problema 29
def problema_29():
    """
    VERIFICAR ANAGRAMA:
    Determina si dos palabras son anagramas.
    """
    palabra1 = "listen"
    palabra2 = "silent"
    # Tu código aquí
    return True


# Problema 30
def problema_30():
    """
    PROCESAR TWEET:
    Acorta un texto a 280 caracteres, agregando "..." si es necesario.
    """
    tweet = "Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Se trata de un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional."
    # Tu código aquí
    return "Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Se trata de un lenguaje de programación multiparadigma, ya que..."


# Ejecutar todos los problemas
if __name__ == "__main__":
    problemas = [problema_1, problema_2, problema_3, problema_4, problema_5,
                 problema_6, problema_7, problema_8, problema_9, problema_10,
                 problema_11, problema_12, problema_13, problema_14, problema_15,
                 problema_16, problema_17, problema_18, problema_19, problema_20,
                 problema_21, problema_22, problema_23, problema_24, problema_25,
                 problema_26, problema_27, problema_28, problema_29, problema_30]

    print("Problemas cargados. Resuélvelos y verifica con el archivo soluciones.txt")
    print(f"Total de problemas: {len(problemas)}")