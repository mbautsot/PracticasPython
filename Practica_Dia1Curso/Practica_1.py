'''
Vas a crear un código en Python que le pida a tu amigo que responda dos preguntas que
requieran una sola palabra cada una y que luego le muestre en pantalla esas palabras
combinadas, para formar una marca creativa.
'''
import random
print("=" * 60)
print("Vamos a crear el nombre de tu cerveza!!!!")
print("=" * 60)

color = input('¿Cual es color favorito?')
banda = input('¿Cual de estas 3 Bandas es tu Favorita : a) Rolling Stones , b) Led Zeppeling ,c) Black Sabat ?')

if banda == 'a':
    banda = 'Rolling Stones'
elif banda == 'b':
    banda = 'Led Zepelling'
elif banda == 'c':
    banda = 'Black Sabbat'
else:
    print('Opcion equivocada , solo puedes ser a,b, c')


nom_cerveza = banda.split()
print("*" * 60)
print(f'El nombre de tu cerveza es : \n"'+ nom_cerveza.pop() + color +'"')
print("*" * 60)
