menor = min(2,4,6,78,10,9,23)
print(menor)

mayor = max(2,4,6,78,20,9,23)
print(mayor)

lista = [2,4,6,7,20,9,23]
print(max(lista))
print(f'El mayor es {max(lista)} y el menor es {min(lista)}')

print('*'*60)
nombres = ['Marcos','Lilian','Sofia','Nicolas','Santiago']
print(max(nombres))
print(min(nombres))

nombre = 'Marcos'
print(min(nombre.lower()))#Los string es una coleccion de caracteres , po lo cual primero buscara por simbolo , despues mayusculas y por ultimo las minusculas

dic = {'C1':45,'C2':56}
print(dic['C1'])
print(dic['C2'])
print(min(dic.values()))


'''

Práctica Min y Max 1
Obtén el valor máximo entre los valores de la siguiente lista, y almacénalo en una variable llamada valor_maximo:

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5] 

'''
print('='*60)
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)
print(valor_maximo)

'''
Práctica Min y Max 2
Calcula la diferencia entre el valor máximo y el mínimo en la siguiente lista de números, y almacénalo en una variable llamada rango:

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
'''
print('='*60)

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

maximo = max(lista_numeros)
minimo = min(lista_numeros)

rango = (maximo - minimo)
print(rango)

'''

Práctica Min y Max 3
Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente diccionario:

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

Almacena dicho valor en una variable llamada edad_minima.

También, obtén el nombre que se ubica último en orden alfabético, y almacénalo en una variable llamada ultimo_nombre.

'''
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())
print(edad_minima)
ultimo_nombre = max(diccionario_edades.keys())
print(ultimo_nombre)
