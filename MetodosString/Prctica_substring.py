


txt  = "ABCDEFGHIJKLM"
#A=0 ,B=1 , C=2 , D=3, E=4, F=5 .....
#fragmnto = txt[2] = C  Se imprime el caracter en la segunda posicion  2
#fragmnto = txt[2:5] = CDE Se imprimie apartir de la posicion 2 a la posicion 5
#fragmnto = txt[:7] = ABCDEFG desde la posicion 0 hasta la 7
#fragmnto = txt[2:10:2]
#  CEGI = El terce factor cada cuanto caracteres va ir extrayendo

#fragmnto = txt[::3]
#tomara toda la cadena y estara saltado de 3 en tres posiciones apartir del 0
# A = 0 ...D ...G...J...M

#fragmnto = txt[::-1]
#Toda la cadena  a inverso = MLKJIHGFEDCBA
#print(fragmnto)


'''
Práctica Sub-Strings 1
Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:

"Controlar la complejidad es la esencia de la programación"

Pista: "Controlar" tiene un largo de 9 caracteres.
'''
frase = 'Controlar tiene un largo de 9 caracteres.'
slicing = frase[:9]
print(slicing)

'''
Práctica Sub-Strings 2
Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.

"Nunca confíes en un ordenador que no puedas lanzar por una ventana"

'''
frase_DOS = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
slicing_DOS = frase_DOS[8::3]
print(slicing_DOS)


'''
La sintaxis del slicing: [inicio:fin:paso]

INICIO
# La string completa:
# N u n c a   c o n f í e s   e n...
# 0 1 2 3 4 5 6 7 8 9 10 11 12...

frase[8]  # Esto sería: 'o' (de "confíes")


FIN (VACIO)
# Al dejar vacío después de los dos puntos:
# significa "hasta el final de la string"
frase[8:]  # Desde índice 8 hasta el final

# Toma cada tercer carácter
# Ejemplo: índices 8, 11, 14, 17, 20...
frase[8::3]  # Desde 8 hasta el final, cada 3 caracteres


EJEMPLO PASO A PASO 

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"

# Los índices que se tomarían:
# 8: 'o'
# 11: 'f'  (8 + 3 = 11)
# 14: 'e'  (11 + 3 = 14)
# 17: ' '  (14 + 3 = 17)
# 20: 'n'  (17 + 3 = 20)
# 23: 'u'  (20 + 3 = 23)
# ... y así sucesivamente

'''

'''
Práctica Sub-Strings 3
Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.

"Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
'''

frase_TRES ="Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
slicing_TRES = frase_TRES[::-1]
print(slicing_TRES)