mi_set = set([1,2,3,4,5 , 5,5,5,3,3,3,5,5]) #prmite repetidos pero los descarta en automatico
print(type(mi_set))
print(mi_set)

#otra forma de crear un set
otro_set = {1,2,3,4,5}
print(type(otro_set))
print(otro_set)


mi_set_nuevo = set([1,2,3,4,5 ,(6,7,8)]) #NO PERMITE TIPOS LISTA , DICCIONARIOS , ***SI ADMITE TUPLES
print(mi_set_nuevo) #como son imutables es por ello que acepta tuples

print(len(mi_set_nuevo))
print(2 in mi_set_nuevo) #verifica si esta el valor 2 n mi SET

s1 = {1,2,3}
s2 ={3,5,6}

s3 = s1.union(s2)
print(s3)

s3.add(4) #agregamos un elemento 4 en nuestro set
print(s3)

s3.remove(5) #remuve un elemento en este caso el 5
print(s3)

s3.discard(8) #descarta el valor 8 como no esta no enviar error

s3.pop() #elimina un elemento aleatorio
print(s3)

s3.clear()#limpia nuestro set
print(s3)


'''
Práctica Sets 1
Une los siguientes sets en uno solo, llamado mi_set_3:

{1, 2, "tres", "cuatro"}

{"tres", 4, 5}
'''

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}

mi_set_3 = mi_set_1.union(mi_set_2)
print(mi_set_3)


'''
Práctica Sets 2
Elimina un elemento al azar del siguiente set, utilizando métodos de sets.

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
'''
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

sorteo.pop()
print(sorteo)


'''
Práctica Sets 3
Agrega el nombre Damián al siguiente set, utilizando métodos de sets:

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
'''

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

sorteo.add("Damián")
print(sorteo)

