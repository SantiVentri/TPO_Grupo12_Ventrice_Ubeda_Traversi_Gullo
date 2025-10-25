#----------------------------------------------------------------------------------------------
# FUNCIONES DE INFORMES
#----------------------------------------------------------------------------------------------
def informeViajesDelMes(rutas, choferes, vehiculos):
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
        hora_llegada = datos['horaLlegada']

        fila = [
            fecha,                    # fecha y hora
            f"LU{datos['idLegajo']}", # legajo
            patente,                  # patente
            totalKm,                  # total km
            costoRuta,               # costo calculado
            datos['horaSalida'],      # hora salida  
            hora_llegada             # hora llegada (sin segundos)
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
    Muestra un informe resumen mensual de rutas por vehículo,
    con el total de kilómetros y el costo total (Km * costoKm).
    Ordena por costo total de mayor a menor.
    """

    resumen = {}

    #Calcular rutas, km y costo total por vehículo 
    for cod in rutas:
        datos = rutas[cod]
        patente = datos["idPatente"]
        km = datos["totalKm"]

        if patente in vehiculos and vehiculos[patente]["activo"]:
            costoKm = vehiculos[patente]["costoKm"]

            if patente not in resumen:
                resumen[patente] = {"rutas": 0, "km": 0, "costo": 0.0}

            resumen[patente]["rutas"] += 1
            resumen[patente]["km"] += km
            resumen[patente]["costo"] += km * costoKm  

    #Convertir a lista para mostrar 
    lista = []
    for patente, datos in resumen.items():
        modelo = vehiculos[patente]["modelo"]
        fila = [patente, modelo, datos["rutas"], datos["km"], datos["costo"]]
        lista.append(fila)

    #Ordenar por costo total (posición 4) usando lista temporal 
    lista_temp = [[fila[4]] + fila for fila in lista]  
    lista_temp.sort(reverse=True)                      
    lista_ordenada = [fila[1:] for fila in lista_temp] 

    #Preparar encabezado y datos finales para la tabla
    encabezado = ["Pos.", "Patente", "Modelo", "Rutas", "Km Totales", "Total $"]
    tabla = []
    pos = 1
    total_general = 0.0

    for fila in lista_ordenada:
        total_general += fila[4]
        tabla.append([
            pos,
            fila[0],
            fila[1],
            fila[2],
            fila[3],
            f"${fila[4]:.2f}"
        ])
        pos += 1

    #Calcular anchos automáticos 
    anchos = [max(len(str(fila[i])) for fila in ([encabezado] + tabla)) for i in range(len(encabezado))]

    #Imprimir encabezado general
    ancho_total = sum(anchos) + len(anchos) * 3 + 1
    print("\n" + "-" * ancho_total)
    print(f"| {'RESUMEN MENSUAL DE COSTOS POR VEHÍCULO':^{ancho_total - 2}} |")
    print("-" * ancho_total)

    #Imprimir línea superior de la tabla
    print("+" + "+".join("-" * (anchos[i] + 2) for i in range(len(anchos))) + "+")

    #Imprimir encabezado
    print("| " + " | ".join(str(encabezado[i]).ljust(anchos[i]) for i in range(len(encabezado))) + " |")

    #Imprimir línea divisoria
    print("+" + "+".join("-" * (anchos[i] + 2) for i in range(len(anchos))) + "+")

    # Imprimir filas de la tabla
    for fila in tabla:
        print("| " + " | ".join(str(fila[i]).ljust(anchos[i]) for i in range(len(fila))) + " |")

    #Línea final de la tabla
    print("+" + "+".join("-" * (anchos[i] + 2) for i in range(len(anchos))) + "+")

    # Mostrar total general
    print(f"\nTOTAL GENERAL MENSUAL: ${total_general:.2f}\n")




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