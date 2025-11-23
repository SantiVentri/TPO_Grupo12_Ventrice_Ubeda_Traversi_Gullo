"""
-----------------------------------------------------------------------------------------------
Título: Funciones de Informes
Fecha: 20/10/2025
Autores: Santino Ventrice, Valentina Ubeda, Santino Traversi y Rocco Gullo

Descripción: Funciones relacionadas a los informes.
-----------------------------------------------------------------------------------------------
"""
#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import json
from funciones.archivos import abrirArchivo, cerrarArchivo

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def informeViajesDelMes():
    """
    Muestra un listado con todos los viajes del mes.
    """
    
    # Rutas de archivos
    rutaVehiculos = "diccionarios/vehiculos.json"
    rutaRutas = "diccionarios/rutas.json"

    # Cargar datos de vehículos
    archivo = abrirArchivo(rutaVehiculos, "r")
    if archivo is not None:
        vehiculos = json.load(archivo)
        cerrarArchivo(archivo)
    else:
        vehiculos = {}

    # Cargar datos de rutas
    archivo = abrirArchivo(rutaRutas, "r")
    if archivo is not None:
        rutas = json.load(archivo)
        cerrarArchivo(archivo)
    else:
        rutas = {}
    
    # Crear lista con los datos de cada viaje
    lista = []
    for fecha, datos in rutas.items():
        # Calcular costo multiplicando km por costo/km del vehículo
        patente = datos['idPatente']

        # Filtrar vehículos inactivos
        if vehiculos[patente]['activo']:
            totalKm = datos['totalKm']
            costoKm = vehiculos[patente]['costoKm']
            costoRuta = totalKm * costoKm

            # Formatear hora de llegada sin segundos
            horaLlegada = datos['horaLlegada']

            fila = [
                fecha,                    # fecha y hora
                f"LU{datos['idLegajo']}", # legajo
                patente,                  # patente
                totalKm,                  # total km
                costoRuta,                # costo calculado
                datos['horaSalida'],      # hora salida  
                horaLlegada               # hora llegada (sin segundos)
            ]
            lista.append(fila)

    # Imprimir encabezado
    print("-"*105)
    print(f"| {'LISTADO DE VIAJES DEL MES':^101} |")
    print("-"*105)
    print(f"|{'Fecha/Hora':^19}|{'Legajo':^8}|{'Patente':^10}|{'Total Km':^10}|{'Costo ($)':^12}|{'Hora Salida':^19}|{'Hora Llegada':^19}|")
    print("-"*105)

    # Imprimir cada fila
    for fila in lista:
        print(f"|{fila[0]:^19}|{fila[1]:^8}|{fila[2]:^10}|{fila[3]:^10}|{fila[4]:^12.2f}|{fila[5]:^19}|{fila[6]:^19}|")

    print("-"*105)

def informeResumenMensualKmVehiculo():
    """
    Muestra un resumen mensual de rutas por vehículo (CANTIDADES KM),
    en formato matricial (filas: vehículos, columnas: meses).
    """

    # Rutas de archivos
    rutaVehiculos = "diccionarios/vehiculos.json"
    rutaRutas = "diccionarios/rutas.json"

    # Cargar datos de vehículos
    archivo = abrirArchivo(rutaVehiculos, "r")
    if archivo is not None:
        vehiculos = json.load(archivo)
        cerrarArchivo(archivo)
    else:
        vehiculos = {}

    # Cargar datos de rutas
    archivo = abrirArchivo(rutaRutas, "r")
    if archivo is not None:
        rutas = json.load(archivo)
        cerrarArchivo(archivo)
    else:
        rutas = {}

    if not rutas:
        print("No hay rutas registradas.")
        return

    # Tomar automáticamente el año del primer registro para el encabezado
    primera_clave = next(iter(rutas))
    año = int(primera_clave[0:4])

    # Meses abreviados
    meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN",
             "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]

    # 1. Inicializar matriz para vehículos ACTIVOS
    #    [cite_start]Diccionario: patente -> lista de 12 valores (uno por mes) [cite: 92]
    matriz = {}
    for patente, v in vehiculos.items():
        if v["activo"]:
            matriz[patente] = [0] * 12

    # 2. Rellenar la matriz con los datos de las rutas
    for clave, datos in rutas.items():
        fechaSalida = datos["horaSalida"] 
        # El formato es "YYYY.MM.DD HH.MM"
        añoRuta = int(fechaSalida[0:4])
        mesRuta = int(fechaSalida[5:7])
        patente = datos["idPatente"]

        # Solo sumamos si el vehículo está en la matriz (activo) y coincide el año
        if añoRuta == año and patente in matriz:
            km = datos["totalKm"]
            matriz[patente][mesRuta - 1] += km

    # 3. Imprimir el informe matricial
    print("\n" + "-" * 150)
    print(f"{f'KILÓMETROS TOTALES POR MES ({año})':^150}")
    print("-" * 150)

    # Encabezado de Columnas (Meses)
    print(f"{'Vehículo':<20}", end="")
    for m in meses:
        # Formato ENE.25
        print(f"{m}.{str(año)[2:]}".rjust(10), end="")
    print()
    print("-" * 150)

    # Filas de Datos
    for patente, valores in matriz.items():
        # Obtenemos el modelo para mostrarlo junto a la patente
        modelo = vehiculos[patente]['modelo']
        # Recortamos modelo si es muy largo para que entre en la columna
        etiqueta = f"{patente} ({modelo[:10]})"
        
        print(f"{etiqueta:<20}", end="")
        for cantidad in valores:
            if cantidad == 0:
                 print(f"{'-':>10}", end="") # Guión si es 0 para lectura más limpia
            else:
                 print(f"{cantidad:10.0f}", end="") # Número entero alineado
        print()

    print("-" * 150)

def informeResumenMensualCostosVehiculos():
    """
    Listado de resumen de monto en pesos de las operaciones por año y por mes.
    Entidad: vehículos activos.
    """

    # Rutas de archivos
    rutaVehiculos = "diccionarios/vehiculos.json"
    rutaRutas = "diccionarios/rutas.json"

    # Cargar datos de vehículos
    archivo = abrirArchivo(rutaVehiculos, "r")
    if archivo is not None:
        vehiculos = json.load(archivo)
        cerrarArchivo(archivo)
    else:
        vehiculos = {}

    # Cargar datos de rutas
    archivo = abrirArchivo(rutaRutas, "r")
    if archivo is not None:
        rutas = json.load(archivo)
        cerrarArchivo(archivo)
    else:
        rutas = {}

    if not rutas:
        print("No hay rutas registradas.")
        return

    # Tomar automáticamente el año del primer registro
    primera_clave = next(iter(rutas))
    año = int(primera_clave[0:4])

    # Meses abreviados
    meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN",
             "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]

    # Crear base: patente -> 12 valores
    matriz = {}
    for patente, v in vehiculos.items():
        if v["activo"]:
            matriz[patente] = [0] * 12

    # Completar matriz
    for clave, datos in rutas.items():
        fechaSalida = datos["horaSalida"] 
        añoRuta = int(fechaSalida[0:4])
        mesRuta = int(fechaSalida[5:7])
        patente = datos["idPatente"]

        if añoRuta == año and patente in matriz:
            km = datos["totalKm"]
            costoKm = vehiculos[patente]["costoKm"]
            monto = km * costoKm
            matriz[patente][mesRuta - 1] += monto

    # Encabezado visual
    print("\n" + "-" * 150)
    print(f"{'PESOS TOTALES POR MES':^150}")
    print("-" * 150)

    # Títulos de columnas
    print(f"{'Vehículo':<20}", end="")
    for m in meses:
        print(f"{m}.{str(año)[2:]}".rjust(10), end="")
    print()
    print("-" * 150)

    # Filas con montos
    for patente, valores in matriz.items():
        print(f"{patente:<20}", end="")
        for monto in valores:
            print(f"{monto:10.0f}", end="")   # sin decimales
        print()

    print("-" * 150)

def informeRankingChoferes():
    """
    Muestra el ranking de choferes activos por km recorridos.
    """

    # Rutas de archivos
    rutaChoferes = "diccionarios/choferes.json"
    rutaRutas = "diccionarios/rutas.json"

    # Cargar datos de choferes
    archivo = abrirArchivo(rutaChoferes, "r")
    if archivo is not None:
        choferes = json.load(archivo)
        cerrarArchivo(archivo)
    else:
        choferes = {}

    # Cargar datos de rutas
    archivo = abrirArchivo(rutaRutas, "r")
    if archivo is not None:
        rutas = json.load(archivo)
        cerrarArchivo(archivo)
    else:
        rutas = {}

    ranking = {}
    for cod in rutas:
        datos = rutas[cod]
        legajo = datos["idLegajo"]

        if legajo not in ranking:
            ranking[legajo] = 0
        ranking[legajo] = ranking[legajo] + datos["totalKm"]

    lista = []
    for legajo in ranking:
        if legajo in choferes:
            if choferes[legajo]["activo"] == True:
                nombre = choferes[legajo]["nombre"] + " " + choferes[legajo]["apellido"]
                # Guardamos primero el km para poder ordenar directamente
                fila = [ranking[legajo], legajo, nombre]
                lista.append(fila)

    # Ordenar descendente por km (primer elemento)
    lista.sort(reverse=True)

    print("-"*60)
    print(f"| {'RANKING DE CHOFERES':^56} |")
    print("-"*60)
    print(f"|{'Pos.':^6}|{'Legajo':^10}|{'Nombre':^25}|{'Km Recorridos':^14}|")
    print("-" * 60)

    pos = 1
    for fila in lista:
        km = fila[0]
        legajo = fila[1]
        nombre = fila[2]
        print(f"|{pos:^6}| LU{legajo:^7}| {nombre:<24}|{km:^14}|")
        pos = pos + 1

    print("-" * 60)

def informeRankingVehiculos():
    """
    Muestra el ranking de vehículos activos por km recorridos.
    """

    # Rutas de archivos
    rutaVehiculos = "diccionarios/vehiculos.json"
    rutaRutas = "diccionarios/rutas.json"

    # Cargar datos de vehículos
    archivo = abrirArchivo(rutaVehiculos, "r")
    if archivo is not None:
        vehiculos = json.load(archivo)
        cerrarArchivo(archivo)
    else:
        vehiculos = {}

    # Cargar datos de rutas
    archivo = abrirArchivo(rutaRutas, "r")
    if archivo is not None:
        rutas = json.load(archivo)
        cerrarArchivo(archivo)
    else:
        rutas = {}

    ranking = {}
    for cod in rutas:
        datos = rutas[cod]
        patente = datos["idPatente"]
        if patente not in ranking:
            ranking[patente] = 0
        ranking[patente] = ranking[patente] + datos["totalKm"]

    lista = []
    for patente in ranking:
        if patente in vehiculos:
            if vehiculos[patente]["activo"] == True:
                modelo = vehiculos[patente]["modelo"]
                # Guardamos primero el km para poder ordenar directamente
                fila = [ranking[patente], patente, modelo]
                lista.append(fila)

    # Ordenar descendente por km (primer elemento)
    lista.sort(reverse=True)

    print("-"* 60)
    print(f"| {'RANKING DE VEHÍCULOS':^56} |")
    print("-"* 60)
    print(f"|{'Pos.':^6}|{'Patente':^10}|{'Modelo':^25}|{'Cantidad Kms':^14}|")
    print("-" * 60)

    pos = 1
    for fila in lista:
        km = fila[0]
        patente = fila[1]
        modelo = fila[2]
        print(f"|{pos:^6}|{patente:^10}| {modelo:<24}|{km:^14}|")
        pos = pos + 1

    print("-" * 60)