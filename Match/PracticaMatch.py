serie = 'N-02'

'''
if serie == 'N-01':
    print('Samsung')
elif serie == 'N-02':
    print('Nokia')
elif serie == 'N-03':
    print('Motorola')
else: 'N existe se producto.'
'''


match serie:
    case 'N-01':
        print('Samsung')
    case "N-02":
        print('Nokia')
    case _:
        print('No existe producto')


cliente = {
            'nombre':'federico',
            'edad':45,
            'ocupacion':'instructor'
         }




pelicula = {'titulo':'Matrix',
            'ficha_tecnica':{'protagonista':'Keanu Reeves',
                             'director':'Hermanas Wachowski',
                             'año':1999}}


elementos = [cliente, pelicula,'Libro']

for e in elementos:
    match e:
        case {'nombre':nombre, 
              'edad':edad, 
              'ocupacion':ocupacion}:
            print(f'Cliente: {nombre}, edad :{edad} años : {ocupacion}')
        case {'titulo':t, 'ficha_tecnica':{'protagonista':p, 'director':d, 'año':a}}:
            print(f'Película: {t}, Protagonista: {p}, Director: {d}, Año: {a}')
        case _:
            print('No es ni cliente ni película')