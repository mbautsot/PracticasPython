#Zip lo que va a realizar es entralazar dos o mas listas, entrelazando sus elementos en tuples
nombres = [
    "Marcos",
    "Lilian",
    "Sofia"
]
edades = [39,34,1]

cuidades = ['Mexico','Guadalajara','Cuidad de Mexico']

#Si se cambia el tamaño de la lista ejemplo se agrega , otro dato a edades , zip lo descarta ya , nombres en este caso solo tiene un tamaño de 3
#combinados = zip(nombres, edades) #De esta forma no va a mostrar los datos , lo debemos de castear a una lista
combinados = list(zip(nombres, edades, cuidades))#Aca de igual forma debemos de agregar Cuidades para que se integre en nuestro zip

for nombre, edad, cuidades in combinados:
        print(f'{nombre} tiene {edad} años y vive en {cuidades}')


'''
Práctica Zip 1
Muestra en pantalla frases como la del siguiente ejemplo:

La capital de Alemania es Berlín

Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente.

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
'''
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

info = list(zip(capitales, paises))
for capital, pais in info:
    print(f'La capital de {pais} es {capital}')


'''
Práctica Zip 2
Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.
'''
marca =['Mafex','Sentinel','SH Figuarts']
productos =['Marvel', 'Spiderman' , 'Dragon ball']
mi_zip = zip(marca, productos)


'''
Práctica Zip 3
Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:

uno / um / one
dos / dois / two
tres / três / three
cuatro / quatro / four
cinco / cinco / five

El resultado deberá seguir la estructura:

[('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]


1: uno / um / one
2: dos / dois / two
3: tres / três / three
4: cuatro / quatro / four
5: cinco / cinco / five
'''
print('='*60)
uno = ['uno','um','one']
dos = ['dos','dois' ,'two']
tres = ['tres','três','three']
cuatro = ['cuatro','quatro','four']
cinco = ['cinco','cinco','five']

#PENDIENTE!!!!!!!
#numeros = list(zip(uno, dos, tres, cuatro, cinco))
#print(numeros[0][0][0][0][0])

espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(espaniol, portugues, ingles))