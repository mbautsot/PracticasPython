monedas =5

while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas -= 1 #Restamos las monedas para que finalice el programa
else:
    print(f'No tengo mas monedas')



respuesta = 'S'

while respuesta == 'S':
    respuesta = input('Quieres continuar: (S/N)?')
else:
    print('Gracias')

'''
resonse = 'S'
while resonse == 'S':
    pass #Continue
print('Hola')
'''


nombre = input('Nombre: ')
for letra in nombre:
    if  letra == 'r':
        break #finalice
    print(letra)


nombre2 = input('Nombre: ')
for letra2 in nombre2:
    if  letra2 == 'r':
        continue #CONTINUA IMPRIMIRA TODAS LAS LETRAS EXCEPTO R
    print(letra2)


'''
Práctica Loop While 1
Crea un Loop While que se imprima en pantalla los números del 10 al 0, uno a la vez.
'''

num = 10
while num >= 0:
    print(num)
    num -= 1

'''
Práctica Loop While 2
Crea un Loop While que reste de uno en uno los números desde el 50 al 0 
(ambos números incluídos) con las siguientes condiciones adicionales:

- Si el número es divisible por 5, mostrar dicho número en pantalla 
(¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)

- Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla 
(no te olvides de seguir restando para que el programa no corra infinitamente).
'''

numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
        numero -= 1
    elif numero % 5 != 0:
        numero -= 1
        continue

'''
Práctica Interrupción de Flujo
Crea un loop For a lo largo de la siguiente lista de números, 
imprimiendo en pantalla cada uno de sus elementos, e 
interrumpe el flujo en el momento que encuentres un valor negativo:

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

No debes cambiar el orden de la lista.
'''
print('='*60)
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for numero in lista_numeros:
    if numero <0:
        break
    print(numero)

