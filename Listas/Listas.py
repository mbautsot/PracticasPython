mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2 #Concatena pero crea una nueva lista


otra_lista = ['hola', 55, 61.4]

resultado = len(mi_lista)
resultado_index = mi_lista[0:1]

print(type(mi_lista))
print(resultado)
print(resultado_index)
print(mi_lista + mi_lista2)
print(mi_lista3)

#Modificar lista algo que no s puede hacer con los String ya que son inmutables

mi_lista3[0] = 'ALPHA' #Se modifica el primer elemento o el indice en la posisicon 0
print(mi_lista3)

#Ahora vamos a agregar un valor a nuestra lista

mi_lista3.append('g')
print(mi_lista3)

#POP saltar o eliminar
mi_lista3.pop()#Sin parametros interpreta que se va a eliminar el ultimo de sus elementos
print(mi_lista3)

elim = mi_lista3.pop(0)
print(elim) #SE elimina y se reserva en una variable el elemento de la lista.

mi_lista_desordenada = ['c','d','e', 'b','a']
mi_lista_desordenada.sort() #ORDENA ALFABETICAMENTE
print(mi_lista_desordenada)
print(mi_lista_desordenada.sort()) #None Esto sucede si bien ordena la lista no devuelve ninguna dato por ello

mi_lista_desordenada2 = ['c','d','e', 'b','a']
mi_lista_desordenada2.reverse()
print(mi_lista_desordenada2)