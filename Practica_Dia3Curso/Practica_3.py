'''
La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que
ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
letras a su elección y a partir de ese momento nuestro código va a procesar esa información
para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:

Info PDF
'''
print("=" * 60)
print("Bienvenido Practica 3!!!!")
print("=" * 60)

letras = []
'''
Que nada te detenga en el camino a perseguir tus sueños; yo estaré siempre aquí para motivarte y apoyarte, pase lo que pase 
'''

txt = input("Hola!!,Ingresar un texto , artículo, párrafo, frase o poema que te guste:")
#print(txt)

letras.append(input("Ingresa primer letra de tu elección:"))
letras.append(input("Ingresa segunda letra de tu elección:"))
letras.append(input("Ingresa tercera letra de tu elección:"))



if len(letras) == 3:
    # Para verificar si ALGUNA letra está en el texto:
    print(any(letra in txt for letra in letras))
    if any(letra in txt for letra in letras):
        print("1) CONTEO LETRAS EN =========================")
        #Si se encuentra en mi texto este caracter
        print(f"Número de veces que se presenta la letra ({list(letras)[0]}) "
                  f"en el texto es :{txt.count(list(letras)[0])}")

        # Si se encuentra en mi texto este caracter
        print(f"Número de veces que se presenta la letra ({list(letras)[1]}) "
                      f"en el texto es :{txt.count(list(letras)[1])}")

        print(f"Número de veces que se presenta la letra ({list(letras)[2]}) "
              f"en el texto es :{txt.count(list(letras)[2])}")

elif len(letras) < 3:
    print("Debes de ingresar 3 caracteres")
else:
#Validar que sean solo 3 caracteres
    print(letras)

print("2) NUMERO DE PALABRAS ============================")
palabras = len(txt.split())
print(f"Número de palabras en el texto: {palabras}")
print("=" * 60)


print("3) PRIMER LETRA Y ULTIMA LETRAS ============================")
print(f"Primer letra :{list(txt)[0]}")
#print(f"Utima letra :{list(txt)[(len(txt)-1)]}")
print(f"Utima letra :{list(txt)[-1]}")

print("=" * 60)

print("4) TEXTO INVERTIDO ============================")

#En este punto separe los caracteres , pero no las palabras
caracteres_txt = list(txt)
caracteres_txt.reverse()
#print(caractres_txt)
txt_invertido =''.join(caracteres_txt)

palabras_txt = txt.split()
palabras_txt.reverse()
palabras_invertidas = ' '.join(palabras_txt)
print(f"Invertido :{palabras_invertidas}")

print("=" * 60)

print("5) SE ENCUENTRA PYHTON ============================")
print(f"Existe la palabra python: {'SI' if 'python' in txt.lower() else 'NO'}")
print("=" * 60)
