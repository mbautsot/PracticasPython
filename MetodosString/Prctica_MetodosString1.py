'''
Práctica Métodos de String 1
Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:
'''

frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
#print(frase.upper())

'''
Práctica Métodos de String 2
Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
'''
lista_palabras = ["La","legibilidad","cuenta."]

#print(' '.join(lista_palabras))

'''
Práctica Métodos de String 3
Reemplaza en la siguiente frase:

"Si la implementación es difícil de explicar, puede que sea una mala idea."

los siguientes pares de palabras:

"difícil" --> "fácil"

"mala" --> "buena"

y muestra en pantalla la frase con ambas palabras modificadas.
'''
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."

print(frase.replace('difícil', 'fácil').replace('mala', 'buena'))
