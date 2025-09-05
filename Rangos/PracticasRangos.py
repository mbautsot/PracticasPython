#Antes
lista_num =[1,2,3,4,5]

for numero in lista_num:
    print(numero)

#Ahora con rangos
print('='*60)
print('Rango un parametro')

#RANGO UN PARAMETRO  EN ESTE CASO SERIA SOLO HASTA EL 5 (desde el 0)
for numero in range(5): #0,1,2,3,4
    print(numero)
print('='*60)

print('Rango un parametro  que inicie desde 1 hasta el 5')
for numero in range(1,5): #1,2,3,4
    print(numero)

print('='*60)

print('Rango un parametro  que inicie desde 1 hasta el 5 y que tenga saltos')
#Estos paramtros funcionan del siguiente modo : SOLO ACEPTA INTEGER
#(2) inicia desde 2
#(40) hasta 40
#(2) saltando de 2 en 2
for numero in range(2,40,2): # 2,4,6,8,10,12 .....38
    print(numero)
print('='*60)


#Crear una lista del 1 a el 100
#Para ellos sirve de igual forma los rango para crear como ejemplo la siguiente lista del 1 a el 50
lista = list(range(1,50))
print(lista)

'''
Práctica Rango 1
Crea una lista formada por todos los números desde el 2500 al 2585 (inclusive). 
Almacena dicha lista en la variable mi_lista.
'''
#SE agrega 2586 ya que debe de tomar el 2585
mi_lista = list(range(2500,2586))
print(mi_lista)

'''
Práctica Rango 2
Utilizando la función range(), 
crea en una única linea de código una lista formada 
por todos los números múltiplos de 3 desde el 3 al 300 (inclusive). 

Almacena dicha lista en la variable mi_lista.
'''

mi_lista2 = list(range(3,303,3))
print(mi_lista2)

'''
Práctica Rango 3
Utiliza la función range() y un loop para sumar los cuadrados de todos 
los números del 1 al 15 (inclusive). 
Almacena el resultado en una variable llamada suma_cuadrados.

Para ello:

Crea un rango de valores que puedas recorrer en un loop

Para cada uno de estos valores, 
calcula su valor al cuadrado (potencia de 2). 
Puede que necesites crear variables intermedias (de manera opcional).

Suma todos los valores al cuadrado obtenidos. 
Acumula la suma en la variable suma_cuadrados.
'''
print('='*60)
suma_cuadrados = 0
for numero in range(1,16):
    suma_cuadrados += numero**2
    print(suma_cuadrados)

