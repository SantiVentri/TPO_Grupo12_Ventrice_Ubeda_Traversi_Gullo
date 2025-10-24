"""
-----------------------------------------------------------------------------------------------
Título: Funciones de Choferes
Fecha:
Autores: Santino Ventrice, Valentina Ubeda, Santino Traversi y Rocco Gullo

Descripción: Funciones relacionadas a la gestión de choferes.

Pendientes:
-----------------------------------------------------------------------------------------------
"""
#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import random

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def crearLegajo(choferes):
    """
    Esta función genera un legajo único para un nuevo chofer.
    Parámetros:
    - choferes (dict): Diccionario de choferes existentes con sus legajos como claves.
    Salida:
    - legajo (int): Legajo único generado para el nuevo chofer.
    """
    
    while True:
        legajo = random.randint(10000, 99999)
        if legajo not in choferes:
            return legajo
        
def validarNombreApellido(tipo, texto):
    """
    Esta función valida el nombre de un chofer.
    Parámetros:
    - nombre (str): El nombre a validar.
    Salidas:
    - textoValido (bool): Indica si el nombre es válido.
    """

    textoValido = True

    if not texto or texto.strip() == "":
        textoValido = False
        print(f"El {tipo} no puede estar vacío. Intente nuevamente.")
    elif len(texto) < 3:
        textoValido = False
        print(f"El {tipo} debe tener al menos 3 caracteres. Intente nuevamente.")
    elif len(texto) > 15:
        textoValido = False
        print(f"El {tipo} no puede exceder los 15 caracteres. Intente nuevamente.")
    else:
        for char in texto:
            if not (char.isalpha() or char == " "):
                textoValido = False
                print(f"El {tipo} solo puede contener letras y espacios. Intente nuevamente.")
                break

    return textoValido

def formatearNombreApellido(texto):
    """
    Esta función formatea el nombre o apellido de un chofer para que la primera letra sea mayúscula.
    Parámetros:
    - nombre (str): El nombre a formatear.
    Salida:
    - textoFormateado (str): El nombre o apellido formateado con la primera letra en mayúscula y el resto en minúscula.
    """

    textoFormateado = texto.strip().title()
    return textoFormateado

def validarTelefono(telefono):
    """
    Esta función valida el teléfono de un chofer.
    Parámetros:
    - telefono (str): El teléfono a validar.
    Salidas:
    - telValido (bool): Indica si el teléfono es válido.
    """

    telValido = True

    if not telefono.isdigit():
        telValido = False
        print("El teléfono solo puede contener números. Intente nuevamente.")
    elif len(telefono) != 8:
        telValido = False
        print("El teléfono debe tener 8 dígitos. Intente nuevamente.")

    return telValido

def validarKm(km):
    """
    Esta función valida la cantidad de km recorridos por un chofer. Lanza un error si no es un número positivo.
    Parámetros:
    - km (str): La cantidad km a validar.
    Salidas:
    - kmValidos (bool): Indica si la cantidad de km es válido.
    """

    kmValido = True

    for char in km:
        if not char.isdigit() and char != '.' and char != '-':
            kmValido = False
            print("Los kilómetros solo pueden contener números y un punto decimal. Intente nuevamente.")
            return kmValido
        elif float(km) < 0:
            kmValido = False
            print("Los kilómetros no pueden ser negativos. Intente nuevamente.")
            return kmValido

    return kmValido

def validarTurno(turnos, turno):
    """
    Esta función valida un turno para un chofer y se fija si ya está en la lista de turnos.
    Parámetros:
    - turnos (dict): Lista de turnos ya asignados al chofer.
    - turno (str): El turno a validar en el formato "Día - Horario".
    Salidas:
    - turnoValido (bool): Indica si el turno es válido.
    """

    # Separa el día y el horario del turno
    dia, horario = turno.split(" - ")

    turnoValido = True

    if turno in turnos:
        turnoValido = False
        print("El chofer ya tiene asignado ese turno. Intente nuevamente.")
    else:
        diaValido = dia.title() in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        horarioValido = horario.title() in ["Mañana", "Tarde", "Noche"]

        if not diaValido:
            turnoValido = False
            print("El día del turno no es válido. Intente nuevamente.")
        elif not horarioValido:
            turnoValido = False
            print("El horario del turno no es válido. Intente nuevamente.")

    return turnoValido

def listarChoferes(choferes):
    """
    Esta función se encarga de mostrar un listado de choferes activos con sus datos formateados.
    Parámetros:
    - choferes (dict): Diccionario de choferes con sus datos.
    """
    print("--------------------------------------")
    print("MENÚ DE CHOFERES > Listado de choferes")
    print("--------------------------------------\n")

    print("SE LISTAN LOS CHOFERES ACTIVOS:\n")

    # Imprimir los títulos de la tabla
    print("-" * 124)
    print(f"|{"Legajo":^11}|{"Nombre":^18}|{"Teléfono":^18}|{"Km Recorridos":^15}|{"Turnos":^56}|")
    print("-" * 124)

    # Crear matriz con los datos de los choferes
    matriz = []
    for legajo, datos in choferes.items():
        if datos["activo"]:
            # Procesar celda de turnos
            if len(datos['turnos']) == 0:
                celdaTurnos = "Sin turnos"
            else:
                celdaTurnos = ", ".join(datos['turnos'].values())

            # Formatear celda de teléfono
            telefonoFormateado = "+54 11 " + str(datos['telefono'])[:-4] + "-" + str(datos['telefono'])[-4:]

            # Agregar fila a la matriz
            matriz.append([
                str(legajo),
                f"{datos['nombre']} {datos['apellido']}",
                telefonoFormateado,
                str(datos['cantidadKm']),
                celdaTurnos
            ])

    # Recorrer matriz con for i / for j e imprimir tabla
    for i in range(len(matriz)):
        print("|", end="")
        for j in range(len(matriz[i])):
            if j == 0:
                print(f" LU{matriz[i][j]:^8}|", end="")
            elif j == 1:
                print(f" {matriz[i][j]:<17}|", end="")
            elif j == 2:
                print(f" {matriz[i][j]:^17}|", end="")
            elif j == 3:
                print(f" {matriz[i][j] + "km ":>14}|", end="")
            elif j == 4:
                print(f" {matriz[i][j]:<55}|", end="")
        print()  # salto de línea entre filas

    # Cerrar tabla
    print("-" * 124)