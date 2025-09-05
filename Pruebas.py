print(len(['A', 'B', 1]))

print(len([sum([1,1,1])]))
'''
sum([1,1,1]) suma los elementos de la lista [1,1,1], dando como resultado 3.
[sum([1,1,1])] crea una lista que contiene un solo elemento: [3].
len([3]) devuelve la cantidad de elementos en la lista, que es 1.
'''

L=[1,3,2]
print(sorted(L)) 


def print_function(A):
    for a in A:
        print(a + '1')
print_function(['a', 'b', 'c'])