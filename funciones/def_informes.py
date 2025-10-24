#----------------------------------------------------------------------------------------------
# FUNCIONES DE INFORMES
#----------------------------------------------------------------------------------------------

def informeResumenMensualRutasVehiculos(rutas, vehiculos):
    """
    Muestra un listado con resumen mensual de rutas por vehículo.
    """
    resumen = {}

    for cod in rutas:
        datos = rutas[cod]
        patente = datos["idPatente"]
        if patente not in resumen:
            resumen[patente] = {"rutas": 0, "km": 0}
        resumen[patente]["rutas"] = resumen[patente]["rutas"] + 1
        resumen[patente]["km"] = resumen[patente]["km"] + datos["totalKm"]

    lista = []
    for patente in resumen:
        if patente in vehiculos:
            if vehiculos[patente]["activo"] == True:
                modelo = vehiculos[patente]["modelo"]
                fila = [patente, modelo, resumen[patente]["rutas"], resumen[patente]["km"]]
                lista.append(fila)

    # Ordenar por km descendente (selección)
    n = len(lista)
    i = 0
    while i < n - 1:
        max_idx = i
        j = i + 1
        while j < n:
            if lista[j][3] > lista[max_idx][3]:
                max_idx = j
            j = j + 1
        if max_idx != i:
            aux = lista[i]
            lista[i] = lista[max_idx]
            lista[max_idx] = aux
        i = i + 1

    print("-"*66)
    print(f"| {"RESUMEN MENSUAL DE RUTAS POR VEHÍCULO":^62} |")
    print("-"*66)
    print(f"|{'Pos.':^5}|{'Patente':^10}|{'Modelo':^25}|{'Rutas':^8}|{'Km Totales':^12}|")
    print("-" * 66)

    pos = 1
    for fila in lista:
        print(f"|{pos:^5}|{fila[0]:^10}|{fila[1]:<25}|{fila[2]:^8}|{fila[3]:^12}|")
        pos = pos + 1

    print("-" * 66)


def informeRankingChoferes(choferes, rutas):
    """
    Muestra el ranking de choferes activos por km recorridos.
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