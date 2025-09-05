diccionario = {'Clave1':100, 'Clave2':200, 'Clave3':300}

'''
El método popitem() elimina y retorna el último par clave-valor insertado en el diccionario. 
El resultado es una tupla (clave, valor). Después de usarlo, el diccionario ya no contiene ese elemento.
'''

a = diccionario.popitem()
'''
print(a)
print(diccionario)
print('------------------')

'''

'''
a = diccionario.popitem()
print(a)           # Muestra la tupla eliminada, por ejemplo: ('Clave3', 300)
print(diccionario) # Muestra el diccionario sin ese par
'''


'''
Práctica Métodos y Ayuda 1
Remueve los caracteres a la izquierda de nuestro texto principal:

,

:

%

_

#

Utiliza el método lstrip(). Imprime el resultado en pantalla:

",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa. 
Puedes utilizar variables intermedias si las necesitas.

'''
caracteres = ",:_#,,,,,,:::____##Pyt%n_ _Total,,,,,,::#"
resultado = caracteres.lstrip(",:_%_#")
print(resultado)  # Salida: "Pyt%on_ _Total,,,,,,::#"

'''
El método lstrip() elimina los caracteres especificados al inicio (izquierda) de una cadena. 
Si no se especifican caracteres, elimina los espacios en blanco. 

No afecta los caracteres en el resto de la cadena, solo los del principio.
'''

'''
Práctica Métodos y Ayuda 2
Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando

el método insert():

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

Busca en la documentación acerca del funcionamiento del método 
solicitado para saber cómo actúa y cómo es su funcionamiento.

'''

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, "naranja")  # Inserta "naranja" en la posición 3 (cuarta posición)
print(frutas)  # Salida: ['m

'''
Práctica Métodos y Ayuda 3
Verifica si los sets a continuación forman conjuntos aislados (es decir, 
que no tienen elementos en común), utilizando el método isdisjoint().
Almacena dicho resultado en la variable conjuntos_aislados:

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
Busca en la documentación acerca del funcionamiento del método 
solicitado para saber cómo actúa y cómo es su funcionamiento.

'''

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)  # Salida: False, porque tienen elementos en común ("Samsung" y "LG")

'''
El método isdisjoint() verifica si dos conjuntos (sets) no tienen elementos en común. 
Devuelve True si son conjuntos aislados (sin elementos compartidos) 
y False si tienen al menos un elemento en común.
'''