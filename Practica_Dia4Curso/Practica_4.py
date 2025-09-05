'''
La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir
algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un
número y el programa puede responder cuatro cosas distintas:
 Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido
un número que no está permitido.
 Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a
decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.
 Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la
misma manera.
 Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos
intentos le ha tomado. 

'''


nombre = input('Hola m puedes indicar cual es tu nombre:')

print(f'Hola!!!, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número')

import random  
numero_secreto = random.randint(1, 100)

intentos = 8

while intentos > 0:
    try:
        numero_usuario = int(input('Por favor ingresa un número entre 1 y 100:'))
    except ValueError:
        print('Debes ingresar un número válido.')
        continue

    if numero_usuario < 1 or numero_usuario > 100:
        print('Has elegido un número que no está permitido. Por favor elige un número entre 1 y 100.')
    elif numero_usuario < numero_secreto:
        intentos -= 1
        print(f'Incorrecto. El número secreto es mayor que {numero_usuario}. Te quedan {intentos} intentos.')
    elif numero_usuario > numero_secreto:
        intentos -= 1
        print(f'Incorrecto. El número secreto es menor que {numero_usuario}. Te quedan {intentos} intentos.')
    else:
        print(f'¡Felicidades, {nombre}! Has adivinado el número secreto {numero_secreto} en {8 - intentos} intentos.')
        break

if intentos == 0:
    print(f'Lo siento, {nombre}. No has logrado adivinar el número secreto {numero_secreto}. Mejora suerte la próxima vez.')