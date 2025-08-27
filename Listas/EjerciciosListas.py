# =============================================
# 30 EJERCICIOS PRÁCTICOS DE LISTAS PARA EL TRABAJO
# =============================================

print("=" * 60)
print("30 EJERCICIOS PRÁCTICOS DE LISTAS")
print("=" * 60)


# Ejercicio 1
def ejercicio_1():
    """
    FILTRAR VENTAS ALTAS:
    Dada una lista de ventas diarias, filtra solo las ventas
    que superen $1000 y devuelve una nueva lista.
    """
    ventas = [850, 1200, 950, 1500, 1100, 800, 1300]
    # Tu código aquí
    return [1200, 1500, 1100, 1300]


# Ejercicio 2
def ejercicio_2():
    """
    CALCULAR COMISIONES:
    Dadas las ventas, calcula las comisiones (10% de cada venta)
    y devuelve una lista con las comisiones.
    """
    ventas = [2000, 1500, 3000, 2500]
    # Tu código aquí
    return [200, 150, 300, 250]


# Ejercicio 3
def ejercicio_3():
    """
    ENCONTRAR CLIENTES PREMIUM:
    Filtra clientes cuyo gasto mensual sea mayor a $5000.
    """
    clientes = [
        {"nombre": "Ana", "gasto": 4200},
        {"nombre": "Carlos", "gasto": 6500},
        {"nombre": "Maria", "gasto": 3800},
        {"nombre": "Juan", "gasto": 7200}
    ]
    # Tu código aquí
    return ["Carlos", "Juan"]


# Ejercicio 4
def ejercicio_4():
    """
    PROMEDIO DE VENTAS SEMANALES:
    Calcula el promedio de ventas de una semana.
    """
    ventas_semana = [1200, 1500, 1800, 900, 2100]
    # Tu código aquí
    return 1500


# Ejercicio 5
def ejercicio_5():
    """
    TOP 3 PRODUCTOS MÁS VENDIDOS:
    Encuentra los 3 productos con mayores ventas.
    """
    productos = [
        {"nombre": "Laptop", "ventas": 45},
        {"nombre": "Mouse", "ventas": 120},
        {"nombre": "Teclado", "ventas": 85},
        {"nombre": "Monitor", "ventas": 60},
        {"nombre": "Tablet", "ventas": 95}
    ]
    # Tu código aquí
    return ["Mouse", "Tablet", "Teclado"]


# Ejercicio 6
def ejercicio_6():
    """
    ACTUALIZAR INVENTARIO:
    Después de una venta, actualiza el inventario restando
    las unidades vendidas.
    """
    inventario = [100, 50, 75, 200]  # unidades por producto
    ventas = [15, 8, 20, 5]  # unidades vendidas
    # Tu código aquí
    return [85, 42, 55, 195]


# Ejercicio 7
def ejercicio_7():
    """
    CONCATENAR NOMBRES DE EQUIPO:
    Crea un string con los nombres del equipo separados por comas.
    """
    equipo = ["Ana", "Carlos", "Maria", "Juan"]
    # Tu código aquí
    return "Ana, Carlos, Maria, Juan"


# Ejercicio 8
def ejercicio_8():
    """
    CALCULAR GASTOS TOTALES POR CATEGORÍA:
    Suma los gastos por categoría.
    """
    gastos = [
        {"categoria": "marketing", "monto": 1500},
        {"categoria": "desarrollo", "monto": 3000},
        {"categoria": "marketing", "monto": 800},
        {"categoria": "operaciones", "monto": 1200}
    ]
    # Tu código aquí
    return {"marketing": 2300, "desarrollo": 3000, "operaciones": 1200}


# Ejercicio 9
def ejercicio_9():
    """
    ELIMINAR DUPLICADOS DE CORREOS:
    Remueve correos duplicados de una lista.
    """
    correos = ["ana@empresa.com", "carlos@empresa.com",
               "ana@empresa.com", "maria@empresa.com"]
    # Tu código aquí
    return ["ana@empresa.com", "carlos@empresa.com", "maria@empresa.com"]


# Ejercicio 10
def ejercicio_10():
    """
    ORDENAR EMPLEADOS POR SALARIO:
    Ordena empleados de mayor a menor salario.
    """
    empleados = [
        {"nombre": "Ana", "salario": 50000},
        {"nombre": "Carlos", "salario": 65000},
        {"nombre": "Maria", "salario": 45000}
    ]
    # Tu código aquí
    return ["Carlos", "Ana", "Maria"]


# Ejercicio 11
def ejercicio_11():
    """
    ENCONTRAR PROYECTOS ATRASADOS:
    Filtra proyectos que tengan fecha límite pasada.
    """
    from datetime import datetime, timedelta
    hoy = datetime.now()
    proyectos = [
        {"nombre": "Web App", "fecha_limite": hoy + timedelta(days=5)},
        {"nombre": "Mobile App", "fecha_limite": hoy - timedelta(days=2)},
        {"nombre": "API", "fecha_limite": hoy - timedelta(days=1)}
    ]
    # Tu código aquí
    return ["Mobile App", "API"]


# Ejercicio 12
def ejercicio_12():
    """
    CALCULAR HORAS EXTRAS:
    Calcula las horas extras (horas > 8 por día).
    """
    horas_trabajadas = [8, 9, 10, 7, 8.5]
    # Tu código aquí
    return [0, 1, 2, 0, 0.5]


# Ejercicio 13
def ejercicio_13():
    """
    GENERAR USUARIOS DE EMAIL:
    Crea emails corporativos a partir de nombres.
    """
    nombres = ["Ana García", "Carlos López", "Maria Rodriguez"]
    # Tu código aquí
    return ["ana.garcia@empresa.com", "carlos.lopez@empresa.com",
            "maria.rodriguez@empresa.com"]


# Ejercicio 14
def ejercicio_14():
    """
    CONTAR TIPOS DE TICKETS:
    Cuenta cuántos tickets hay por prioridad.
    """
    tickets = [
        {"id": 1, "prioridad": "alta"},
        {"id": 2, "prioridad": "media"},
        {"id": 3, "prioridad": "alta"},
        {"id": 4, "prioridad": "baja"}
    ]
    # Tu código aquí
    return {"alta": 2, "media": 1, "baja": 1}


# Ejercicio 15
def ejercicio_15():
    """
    CALCULAR COMISIÓN POR VENDEDOR:
    Calcula comisiones (5% de ventas) para cada vendedor.
    """
    vendedores = [
        {"nombre": "Ana", "ventas": 20000},
        {"nombre": "Carlos", "ventas": 15000},
        {"nombre": "Maria", "ventas": 30000}
    ]
    # Tu código aquí
    return [1000, 750, 1500]


# Ejercicio 16
def ejercicio_16():
    """
    FILTRAR PRODUCTOS SIN STOCK:
    Encuentra productos con stock menor a 10 unidades.
    """
    productos = [
        {"nombre": "Laptop", "stock": 5},
        {"nombre": "Mouse", "stock": 25},
        {"nombre": "Teclado", "stock": 8},
        {"nombre": "Monitor", "stock": 15}
    ]
    # Tu código aquí
    return ["Laptop", "Teclado"]


# Ejercicio 17
def ejercicio_17():
    """
    CALCULAR EDAD PROMEDIO DE CLIENTES:
    Calcula la edad promedio de los clientes.
    """
    clientes = [
        {"nombre": "Ana", "edad": 35},
        {"nombre": "Carlos", "edad": 28},
        {"nombre": "Maria", "edad": 42},
        {"nombre": "Juan", "edad": 31}
    ]
    # Tu código aquí
    return 34


# Ejercicio 18
def ejercicio_18():
    """
    CONVERTIR PRECIOS A DÓLARES:
    Convierte precios de pesos a dólares (tipo de cambio: 20:1).
    """
    precios_pesos = [1000, 2000, 5000, 1500]
    # Tu código aquí
    return [50, 100, 250, 75]


# Ejercicio 19
def ejercicio_19():
    """
    ENCONTRAR PICO DE VISITAS:
    Encuentra el día con máximo tráfico en el sitio.
    """
    visitas_diarias = [1200, 1500, 1800, 900, 2100, 1700]
    # Tu código aquí
    return 2100


# Ejercicio 20
def ejercicio_20():
    """
    CALCULAR DESCUENTOS POR VOLUMEN:
    Aplica 10% de descuento a compras mayores a $1000.
    """
    compras = [800, 1200, 950, 1500, 1100]
    # Tu código aquí
    return [800, 1080, 950, 1350, 990]


# Ejercicio 21
def ejercicio_21():
    """
    GENERAR REPORTE DE VENTAS:
    Crea un string con el reporte de ventas formateado.
    """
    ventas = [
        {"producto": "Laptop", "cantidad": 5, "precio": 1000},
        {"producto": "Mouse", "cantidad": 20, "precio": 25}
    ]
    # Tu código aquí
    return "Laptop: 5 unidades, $5000 total\nMouse: 20 unidades, $500 total"


# Ejercicio 22
def ejercicio_22():
    """
    ORDENAR PEDIDOS POR URGENCIA:
    Ordena pedidos por prioridad (alta > media > baja).
    """
    pedidos = [
        {"id": 1, "prioridad": "media"},
        {"id": 2, "prioridad": "alta"},
        {"id": 3, "prioridad": "baja"},
        {"id": 4, "prioridad": "alta"}
    ]
    # Tu código aquí
    return [2, 4, 1, 3]


# Ejercicio 23
def ejercicio_23():
    """
    CALCULAR TIEMPO PROMEDIO DE RESPUESTA:
    Calcula el tiempo promedio de respuesta a tickets.
    """
    tiempos_respuesta = [2.5, 1.8, 3.2, 4.1, 2.9]  # en horas
    # Tu código aquí
    return 2.9


# Ejercicio 24
def ejercicio_24():
    """
    FILTRAR EMPLEADOS PARA BONO:
    Encuentra empleados con evaluación mayor a 8/10.
    """
    empleados = [
        {"nombre": "Ana", "evaluacion": 8.5},
        {"nombre": "Carlos", "evaluacion": 7.2},
        {"nombre": "Maria", "evaluacion": 9.1},
        {"nombre": "Juan", "evaluacion": 8.8}
    ]
    # Tu código aquí
    return ["Ana", "Maria", "Juan"]


# Ejercicio 25
def ejercicio_25():
    """
    CALCULAR COSTO TOTAL DE PROYECTO:
    Suma los costos de todos los items del proyecto.
    """
    items_proyecto = [
        {"descripcion": "Desarrollo", "costo": 5000},
        {"descripcion": "Diseño", "costo": 3000},
        {"descripcion": "Testing", "costo": 2000}
    ]
    # Tu código aquí
    return 10000


# Ejercicio 26
def ejercicio_26():
    """
    CONVERTIR LISTA A DICCIONARIO:
    Convierte una lista de tuplas a diccionario.
    """
    items = [("nombre", "Ana"), ("edad", 30), ("cargo", "Developer")]
    # Tu código aquí
    return {"nombre": "Ana", "edad": 30, "cargo": "Developer"}


# Ejercicio 27
def ejercicio_27():
    """
    ENCONTRAR CLIENTES POR UBICACIÓN:
    Filtra clientes de una ciudad específica.
    """
    clientes = [
        {"nombre": "Ana", "ciudad": "Madrid"},
        {"nombre": "Carlos", "ciudad": "Barcelona"},
        {"nombre": "Maria", "ciudad": "Madrid"},
        {"nombre": "Juan", "ciudad": "Valencia"}
    ]
    # Tu código aquí
    return ["Ana", "Maria"]


# Ejercicio 28
def ejercicio_28():
    """
    CALCULAR MARGEN DE GANANCIA:
    Calcula margen de ganancia (precio - costo) / precio.
    """
    productos = [
        {"precio": 100, "costo": 60},
        {"precio": 200, "costo": 120},
        {"precio": 150, "costo": 90}
    ]
    # Tu código aquí
    return [0.4, 0.4, 0.4]  # 40% para todos


# Ejercicio 29
def ejercicio_29():
    """
    GENERAR NÚMEROS DE SERIE:
    Crea números de serie para productos.
    """
    producto = "Laptop"
    cantidad = 5
    # Tu código aquí
    return ["Laptop-001", "Laptop-002", "Laptop-003", "Laptop-004", "Laptop-005"]


# Ejercicio 30
def ejercicio_30():
    """
    ANALIZAR SENTIMIENTO DE RESEÑAS:
    Clasifica reseñas como positivas (>3 estrellas) o negativas.
    """
    reseñas = [
        {"producto": "Laptop", "estrellas": 4},
        {"producto": "Mouse", "estrellas": 2},
        {"producto": "Teclado", "estrellas": 5},
        {"producto": "Monitor", "estrellas": 3}
    ]
    # Tu código aquí
    return {"positivas": ["Laptop", "Teclado"], "negativas": ["Mouse"]}


# Ejecutar todos los ejercicios
if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5,
                  ejercicio_6, ejercicio_7, ejercicio_8, ejercicio_9, ejercicio_10,
                  ejercicio_11, ejercicio_12, ejercicio_13, ejercicio_14, ejercicio_15,
                  ejercicio_16, ejercicio_17, ejercicio_18, ejercicio_19, ejercicio_20,
                  ejercicio_21, ejercicio_22, ejercicio_23, ejercicio_24, ejercicio_25,
                  ejercicio_26, ejercicio_27, ejercicio_28, ejercicio_29, ejercicio_30]

    print("Ejercicios cargados. Resuélvelos y verifica con el archivo soluciones.txt")
    print(f"Total de ejercicios: {len(ejercicios)}")