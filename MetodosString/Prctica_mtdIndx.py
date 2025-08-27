#Práctica Método Index() 1
#Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"

palabra = "ordenador"
print(palabra[4])

palabra = "ordenador"
print(palabra.index("n",0,6))


'''
Práctica Método Index() 2
Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:

"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
'''

cadena = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(cadena.index("práctica"))


'''
Práctica Método Index() 3
Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:

"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
'''
print(cadena.rindex("práctica"))

