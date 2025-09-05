import math

palabra ='Python'
lista =[]

for letra in palabra:
    lista.append(letra)
#print(lista)

print('LISTA DINAMICA')
print('='*60)
#De la sigueinte forma se puede crear una lista de forma mas dinamica Y CON MENOS LINEAS DE CODIGO

#listasinamica = [letra for letra in palabra] en esta liena obtenemos los caracters de la palabra Python
listasinamica = [letra for letra in 'python'] #De igual forma se puede utilizar directamente el string
print(listasinamica)

print('='*60)

#CON NUMEROS
listanumeros = [num for num in range (0,20,2)] #obtiene la lista de numeros de 2 en 2 hasta el 20 : 0,2,4,6,...18
print(listanumeros)

#CON OPERACIONES
listanumeros = [num/2 for num in range (0,20,2)] #obtiene la lista de numeros de 2 en 2 hasta el 20 : 0,2,4,6,...18 Y DIVIDIDOS ENTRE 2
#NOTA IMPORTANTE : se puede alterar el numero antes de incluirlo en la lista
print(listanumeros)

listanumeros = [num if num * 2 > 10 else 'No' for num in range (0,20,2) ] #de igual forma podemos agregar validaciones.
#NOTA IMPORTANTE : se puede alterar el numero antes de incluirlo en la lista
#SE PUEDE AGREGAR EL ELSE PERO DEBE DE CAMBIAR LA POSISION pero se cumple
print(listanumeros)

#ejemplo conversiones
pies = [10,20,30,40,50]
metros =[p / 3.281 for p in pies ] #Metros equivalentes a la lista de pies
print(metros)


'''

Práctica Comprensión de Listas 1
Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. 
Si bien en programación el camino correcto es el que devuelve el resultado correcto, 
te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. 
¡Pueden resultarte muy útiles en tu práctica profesional!

Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.

valores = [1, 2, 3, 4, 5, 6, 9.5]

'''
print("Pactica 1")
print("="*60)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [val**2 for val in valores] #NUMERO A EL CUADRADO
print(valores_cuadrado)

'''
Práctica Comprensión de Listas 2
Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. 
Si bien en programación el camino correcto es el que devuelve el resultado correcto, 
te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡
Pueden resultarte muy útiles en tu práctica profesional!

Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.

valores = [1, 2, 3, 4, 5, 6, 9.5]

'''
print("Pactica 2")
print("="*60)
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [val for val in valores  if val%2==0 ] #VERIFICAMOS QUE CUANDO SE DIVIDEN ENTRE 2  ES PAR
print(valores_pares)

'''
Práctica Comprensión de Listas 3
Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. 
Si bien en programación el camino correcto es el que devuelve el resultado correcto, 
te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. 
¡Pueden resultarte muy útiles en tu práctica profesional!

Para la siguiente lista de temperaturas en grados Fahrenheit, 
expresa estos mismos valores en una nueva lista de valores de temperatura en grados Celsius. 
La conversión entre tipo de unidades es la siguiente:

°C = (°F - 32) * (5/9)

o expresado de otro modo:

(grados_fahrenheit-32)*(5/9)

La lista de temperaturas es la siguiente:

temperatura_fahrenheit = [32, 212, 275] 
Almacena esta nueva lista en una variable llamada grados_celsius

'''
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(gradosf-32) * (5/9) for gradosf in temperatura_fahrenheit]
print(grados_celsius)