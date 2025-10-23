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
        
def validarNombre(nombre):
    """
    Esta función valida el nombre de un chofer.
    Parámetros:
        nombre (str): El nombre a validar.
    Salidas:
        nombreValido (bool): Indica si el nombre es válido.
        mensajeError (str): Mensaje de error en caso de que el nombre no sea válido.
    """

    nombreValido = True
    mensajeError = ""

    if not nombre or nombre.strip() == "":
        nombreValido = False
        mensajeError = "El nombre no puede estar vacío."
    elif len(nombre) < 3:
        nombreValido = False
        mensajeError = "El nombre debe tener al menos 3 caracteres."
    elif len(nombre) > 15:
        nombreValido = False
        mensajeError = "El nombre no puede exceder los 15 caracteres."
    else:
        for char in nombre:
            if not (char.isalpha() or char == " "):
                nombreValido = False
                mensajeError = "El nombre solo puede contener letras y espacios."
                break

    return nombreValido, mensajeError

def validarApellido(apellido):
    """
    Esta función valida el apellido de un chofer.
    Parámetros:
        apellido (str): El apellido a validar.
    Salidas:
        apellidoValido (bool): Indica si el apellido es válido.
        mensajeError (str): Mensaje de error en caso de que el apellido no sea válido.
    """

    apellidoValido = True
    mensajeError = ""

    if not apellido or apellido.strip() == "":
        apellidoValido = False
        mensajeError = "El apellido no puede estar vacío."
    elif len(apellido) < 3:
        apellidoValido = False
        mensajeError = "El apellido debe tener al menos 3 caracteres."
    elif len(apellido) > 20:
        apellidoValido = False
        mensajeError = "El apellido no puede exceder los 20 caracteres."
    else:
        for char in apellido:
            if not (char.isalpha() or char == " "):
                apellidoValido = False
                mensajeError = "El apellido solo puede contener letras y espacios."
                break

    return apellidoValido, mensajeError

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