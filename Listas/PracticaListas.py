'''
Práctica Listas 1
Crea una lista con 5 elementos, dentro de la variable mi_lista.
Puedes incluir strings, booleanos, números, etc.
'''

mi_lista = ['M',6,False,78.1,'aut']
print(mi_lista)

'''
Práctica Listas 2
Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:

medios_transporte = ["avión", "auto", "barco", "bicicleta"]

No debes modificar la línea de código ya suministrada,
sino que debes emplear el método apropiado de listas para añadir un nuevo elemento.
'''
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
print(medios_transporte)


'''
Práctica Listas 3
Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, 
y almacénalo en una variable llamada eliminado. 

Utiliza métodos de listas sin alterar la línea de código ya suministrada.

manzana
banana
mango
cereza
sandía
'''

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado =frutas.pop(2)
print(eliminado)