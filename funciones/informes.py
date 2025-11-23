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
...

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def informeViajesDelMes(rutas, vehiculos):
    """
    Muestra un listado con todos los viajes del mes.
    Parámetros:
    - rutas (dict): diccionario con datos de las rutas
    - choferes (dict): diccionario con datos de los choferes
    - vehiculos (dict): diccionario con datos de los vehículos
    """
    # Crear lista con los datos de cada viaje
    lista = []
    for fecha, datos in rutas.items():
        # Calcular costo multiplicando km por costo/km del vehículo
        patente = datos['idPatente']
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

def informeResumenMensualKmVehiculo(patente, rutas, vehiculos):
    """
    Muestra un resumen mensual de rutas por vehículo,
    mostrando la cantidad total de kilómetros recorridos.
    """

    # Verificar si el vehículo existe y si esta activo
    if patente not in vehiculos:
        print(f"No existe un vehículo con la patente '{patente}'.")
        return

    vehiculo = vehiculos[patente]

    
    if not vehiculo["activo"]:
        print(f"El vehículo con patente '{patente}' está inactivo.")
        return

    #Calcular kilómetros totales 
    kmTotales = 0
    cantidadRutas = 0

    for cod, datos in rutas.items():
        if datos["idPatente"] == patente:
            kmTotales += datos["totalKm"]
            cantidadRutas += 1

    #Preparar los datos para la tabla
    encabezado = ["Patente", "Modelo", "Año", "Rutas", "Km Totales"]
    tabla = [[
        patente,
        vehiculo["modelo"],
        vehiculo["añoCompra"],
        cantidadRutas,
        kmTotales
    ]]

    #Calcular anchos de columnas
    anchos = [max(len(str(fila[i])) for fila in ([encabezado] + tabla)) for i in range(len(encabezado))]

    #Imprimir el título del informe 
    print("\n" + "-" * (sum(anchos) + len(anchos) * 3 + 1))
    print(f"| {'RESUMEN MENSUAL DE RUTAS POR VEHÍCULO':^{sum(anchos) + len(anchos) * 3 - 1}} |")
    print("-" * (sum(anchos) + len(anchos) * 3 + 1))

    #Imprimir la tabla 
    # Línea superior
    print("+" + "+".join("-" * (anchos[i] + 2) for i in range(len(anchos))) + "+")

    # Encabezado
    print("| " + " | ".join(str(encabezado[i]).ljust(anchos[i]) for i in range(len(encabezado))) + " |")

    # Línea divisoria
    print("+" + "+".join("-" * (anchos[i] + 2) for i in range(len(anchos))) + "+")

    # Fila
    for fila in tabla:
        print("| " + " | ".join(str(fila[i]).ljust(anchos[i]) for i in range(len(fila))) + " |")

    # Línea inferior
    print("+" + "+".join("-" * (anchos[i] + 2) for i in range(len(anchos))) + "+")

    #Mensaje si no tuvo rutas 
    if cantidadRutas == 0:
        print("Este vehículo no realizó rutas este mes.")


def informeResumenMensualCostosVehiculos(rutas, vehiculos):
    """
    Listado de resumen de monto en pesos de las operaciones por año y por mes.
    Entidad: vehículos activos.
    """

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


def informeRankingChoferes(choferes, rutas):
    """
    Muestra el ranking de choferes activos por km recorridos.
    Parámetros:
    - choferes (dict): diccionario con datos de los choferes.
    - rutas (dict): diccionario con datos de las rutas.
    """
    ranking = {}
    for cod in rutas:
        datos = rutas[cod]
        legajo = datos["idLegajo"]

        # Conversión manual a entero si es string
        if type(legajo) is str:
            num = 0
            i = 0
            while i < len(legajo):
                c = legajo[i]
                if c >= "0" and c <= "9":
                    num = num * 10 + (ord(c) - 48)
                i = i + 1
            legajo = num

        if legajo not in ranking:
            ranking[legajo] = 0
        ranking[legajo] = ranking[legajo] + datos["totalKm"]

    lista = []
    for legajo in ranking:
        if legajo in choferes:
            if choferes[legajo]["activo"] == True:
                nombre = choferes[legajo]["nombre"] + " " + choferes[legajo]["apellido"]
                fila = [legajo, nombre, ranking[legajo]]
                lista.append(fila)

    # Ordenar descendente por km (selección)
    n = len(lista)
    i = 0
    while i < n - 1:
        max_idx = i
        j = i + 1
        while j < n:
            if lista[j][2] > lista[max_idx][2]:
                max_idx = j
            j = j + 1
        if max_idx != i:
            aux = lista[i]
            lista[i] = lista[max_idx]
            lista[max_idx] = aux
        i = i + 1

    print("-"*60)
    print(f"| {"RANKING DE CHOFERES":^56} |")
    print("-"*60)
    print(f"|{'Pos.':^6}|{'Legajo':^10}|{'Nombre':^25}|{'Km Recorridos':^14}|")
    print("-" * 60)

    pos = 1
    for fila in lista:
        legajo = fila[0]
        nombre = fila[1]
        km = fila[2]
        print(f"|{pos:^6}| LU{legajo:^7}| {nombre:<24}|{km:^14}|")
        pos = pos + 1

    print("-" * 60)


def informeRankingVehiculos(vehiculos, rutas):
    """
    Muestra el ranking de vehículos activos por km recorridos.
    Parámetros:
    - vehiculos (dict): diccionario con datos de los vehículos.
    - rutas (dict): diccionario con datos de las rutas.
    """
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
                fila = [patente, modelo, ranking[patente]]
                lista.append(fila)

    # Ordenar descendente por km (selección)
    n = len(lista)
    i = 0
    while i < n - 1:
        max_idx = i
        j = i + 1
        while j < n:
            if lista[j][2] > lista[max_idx][2]:
                max_idx = j
            j = j + 1
        if max_idx != i:
            aux = lista[i]
            lista[i] = lista[max_idx]
            lista[max_idx] = aux
        i = i + 1

    print("-"* 60)
    print(f"| {'RANKING DE VEHÍCULOS':^56} |")
    print("-"* 60)
    print(f"|{'Pos.':^6}|{'Patente':^10}|{'Modelo':^25}|{'Cantidad Kms':^14}|")
    print("-" * 60)

    pos = 1
    for fila in lista:
        print(f"|{pos:^6}|{fila[0]:^10}| {fila[1]:<24}|{fila[2]:^14}|")
        pos = pos + 1

    print("-" * 60)