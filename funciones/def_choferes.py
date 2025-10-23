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
        choferes (dict): Diccionario de choferes existentes con sus legajos como claves.
    Salida:
        legajo (int): Legajo único generado para el nuevo chofer.
    """
    while True:
        legajo = random.randint(10000, 99999)
        if legajo not in choferes:
            return legajo
        
def validarNombreApellido(tipo, texto):
    """
    Esta función valida el nombre de un chofer.
    Parámetros:
        nombre (str): El nombre a validar.
    Salidas:
        textoValido (bool): Indica si el nombre es válido.
        mensajeError (str): Mensaje de error en caso de que el nombre no sea válido.
    """

    textoValido = True
    mensajeError = ""

    if not texto or texto.strip() == "":
        textoValido = False
        mensajeError = f"El {tipo} no puede estar vacío."
    elif len(texto) < 3:
        textoValido = False
        mensajeError = f"El {tipo} debe tener al menos 3 caracteres."
    elif len(texto) > 15:
        textoValido = False
        mensajeError = f"El {tipo} no puede exceder los 15 caracteres."
    else:
        for char in texto:
            if not (char.isalpha() or char == " "):
                textoValido = False
                mensajeError = f"El {tipo} solo puede contener letras y espacios."
                break

    return textoValido, mensajeError

def formatearNombreApellido(texto):
    """
    Esta función formatea el nombre o apellido de un chofer para que la primera letra sea mayúscula.
    Parámetros:
        nombre (str): El nombre a formatear.
    Salida:
        textoFormateado (str): El nombre o apellido formateado con la primera letra en mayúscula y el resto en minúscula.
    """

    textoFormateado = texto.strip().title()
    return textoFormateado

def validarTelefono(telefono):
    """
    Esta función valida el teléfono de un chofer.
    Parámetros:
        telefono (str): El teléfono a validar.
    Salidas:
        telValido (bool): Indica si el teléfono es válido.
        mensajeError (str): Mensaje de error en caso de que el teléfono no sea válido.
    """

    telValido = True
    mensajeError = ""

    if not telefono.isdigit():
        telValido = False
        mensajeError = "El teléfono solo puede contener números."
    elif len(telefono) != 8:
        telValido = False
        mensajeError = "El teléfono debe tener 8 dígitos."

    return telValido, mensajeError

def validarKm(km):
    """
    Esta función valida la cantidad de km recorridos por un chofer.
    Parámetros:
        km (str): La cantidad km a validar.
    Salidas:
        kmValidos (bool): Indica si la cantidad de km es válido.
        mensajeError (str): Mensaje de error en caso de que el la cantidad de km no sea válido.
    """

    kmValido = True
    mensajeError = ""

    if not km.isdigit():
        kmValido = False
        mensajeError = "Los kilómetros solo pueden contener números."
    elif float(km) < 0:
        kmValido = False
        mensajeError = "Los kilómetros no pueden ser negativos."

    return kmValido, mensajeError

def validarTurno(turnos, turno):
    """
    Esta función valida un turno para un chofer y se fija si ya está en la lista de turnos.
    Parámetros:
        turnos (dict): Lista de turnos ya asignados al chofer.
        turno (str): El turno a validar en el formato "Día - Horario".
    Salidas:
        turnoValido (bool): Indica si el turno es válido.
        mensajeError (str): Mensaje de error en caso de que el turno no sea válido.
    """

    # Separa el día y el horario del turno
    dia, horario = turno.split(" - ")

    turnoValido = True

    if turno in turnos:
        turnoValido = False
        mensajeError = "El chofer ya tiene asignado ese turno."
    else:
        diaValido = dia.title() in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        horarioValido = horario.title() in ["Mañana", "Tarde", "Noche"]

        if not diaValido:
            turnoValido = False
            mensajeError = "El día del turno no es válido."
        elif not horarioValido:
            turnoValido = False
            mensajeError = "El horario del turno no es válido."
        else:
            mensajeError = ""

    return turnoValido, mensajeError
