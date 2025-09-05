nombres = ['Marcos','Luis','Hyram','Lilian','Sofia']

for elemento in nombres:
    num_persona = nombres.index(elemento)+1

    if elemento.startswith('S'):
        print(f"Persona {num_persona} : {elemento} ")
    elif elemento.startswith('M'):
        print(f"Persona {num_persona} : {elemento} ")
    elif elemento.startswith('L'):
        print(f"Persona {num_persona} : {elemento} ")


numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print(f"Mi valor de :{numero} es:  {mi_valor}")

print(mi_valor)


palabra = 'Python es genial '
for letra in palabra:
    print(letra)


for objetos in [[1,2],[3,4],[5,6],[7,8]]:
    print(objetos)


for a,b in [[1,2],[3,4],[5,6],[7,8]]:
    print(a)
    print(b)

dict = {'Clave1':'a','Clave2':'b','Clave3':'c'}
for item in dict.items(): #Se imprime solo las claves (dict) = dict.items (clave y valores)
    print(item) #Se imprime solo los valores (dict.items())


'''
Práctica Loop For 1
Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre.

Por ejemplo: "Hola María"

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]


'''
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for alumno in alumnos_clase:
    print(f'Hola {alumno}')

'''
Práctica Loop For 2
Dada la siguiente lista de números, realiza la suma de todos
 los números utilizando loops For y almacena el resultado de la suma en una variable llamada suma_numeros:

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
'''
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros = suma_numeros + numero
print(suma_numeros)


'''
Práctica Loop For 3
Dada la siguiente lista de números, realiza 
la suma de todos los números pares e impares* por separado en las variables suma_pares y suma_impares respectivamente:

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

*Recordando de los días anteriores: el módulo (o resto) de un número dividido 
2 es cero cuando dicho valor es par, y 1 cuando es impar

num % 2 == 0 (valores pares)

num % 2 == 1 (valores impares)
'''

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares += numero
    elif numero % 2 == 1:
        suma_impares += numero
print(suma_pares)
print(suma_impares)