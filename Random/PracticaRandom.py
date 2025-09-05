from random import * #Traer todo lo de la libreria random

alatorio = randint(0,100)#Estoy indicando que me va a obtener un numero INTEGER aleatorio de el 0 a 100 (random integer)
print(alatorio)

alatoriouniform = round(uniform(1,5),1)#obtener un floar aleatorio
print(alatoriouniform)

alatoriorandom = random()#Elije un numero decimal aleatorio entre el 0 -1
print(alatoriorandom)

colores =['azul','verde','rojo','amarillo']
aleatorio_colores = choice(colores) #ALEATORIOS LISTAS (STRINGS)
print(aleatorio_colores)

numeros = list(range(5,50,5))
shuffle(numeros)#Mezclar ---> realizara una mezcla aleatoria NO SE PUEDE ALMACENAR EN UNA LISTA
print(numeros)

#ES UN METODO INSITO  EN EL LUGAR - esta realizando el cambio


'''

Práctica Random 1
Implementa la función randint() de la librería random que te permita obtener un número entero del 1 al 10, 
y almacena dicho valor en una variable llamada aleatorio

'''
aleatorio = randint(1,10)

'''
Práctica Random 2
Implementa la función random() de la librería random que te permita obtener un número decimal entre 0 y 1, 
y almacena dicho valor en una variable llamada aleatorio
'''

aleatorio = random()
print(aleatorio)

'''
Práctica Random 3
Utiliza el método choice() de la librería random para 
obtener un elemento al azar de la lista de nombres a continuación,
 y almacena el nombre escogido en una variable llamada sorteo.

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

'''

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)
print(sorteo)