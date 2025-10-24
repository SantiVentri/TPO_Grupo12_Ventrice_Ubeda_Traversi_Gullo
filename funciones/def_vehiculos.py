"""
-----------------------------------------------------------------------------------------------
Título: Funciones de vehiculos
Fecha:
Autores: Santino Ventrice, Valentina Ubeda, Santino Traversi y Rocco Gullo

Descripción: Funciones relacionadas a la gestión de vehiculos.

Pendientes:
-----------------------------------------------------------------------------------------------
"""
#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def validarPatente(patente, vehiculos):
    """
    Valida una patente argentina (formato viejo AAA123 o nuevo AB123CD).
    Muestra los mensajes de error o confirmación y devuelve True/False.
    """

    patente = patente.upper().strip()
    patenteValida = True

    # --- Verifico largo correcto ---
    if len(patente) == 6:  # Formato viejo: AAA123
            if not (patente[:3].isalpha() and patente[3:].isdigit()):
                print(" La patente es incorrecta. Formato esperado: AAA123")
                patenteValida = False

    elif len(patente) == 7:  # Formato nuevo: AB123CD
            if not (patente[:2].isalpha() and patente[2:5].isdigit() and patente[5:].isalpha()):
                print(" La patente es incorrecta. Formato esperado: AB123CD")
                patenteValida = False

    else:
            print(" La patente debe tener 6 o 7 caracteres.")
            patenteValida = False

    # --- Verificar si ya existe ---
    if patenteValida:
            if patente in vehiculos:
                print(" Ya existe un vehículo con esa patente.")
                patenteValida = False
            else:
                print(" Patente válida y disponible.")

    return patenteValida


def validarAñoCompra(añoCompra):
    """
    Valida que el año de compra del vehículo sea correcto.
    Muestra mensajes de error o confirmación y devuelve True o False.
    """

    # Eliminar espacios
    añoCompra = añoCompra.strip()
    añoValido = True

    # Verificar que sean solo números
    if not añoCompra.isdigit():
        print(" El año de compra debe contener solo números.")
        añoValido = False

    # Verificar longitud (4 dígitos)
    elif len(añoCompra) != 4:
        print(" El año debe tener exactamente 4 dígitos (ej. 2022).")
        añoValido = False

    # Verificar rango lógico (ejemplo: entre 1980 y año actual)
    else:
        añoNum = int(añoCompra)
        from datetime import datetime
        añoActual = datetime.now().year

        if añoNum < 1980 or añoNum > añoActual:
            print(f" El año debe estar entre 1980 y {añoActual}.")
            añoValido = False
        else:
            print(" Año de compra válido.")

    return añoValido


def validarCantKm(cantidadKm):
    """
    Valida que la cantidad de kilómetros sea un número positivo (entero o decimal).
    Muestra mensajes de error o confirmación. Devuelve True o False.
    """

    cantidadKm = cantidadKm.strip()
    valido = True

    # Validar que sea numérico (permite solo un punto)
    if not cantidadKm.replace(".", "", 1).isdigit():
        print("Error: el valor debe ser numérico.")
        valido = False

    elif cantidadKm.count(".") > 1:
        print("Solo se permite un punto decimal.")
        valido = False

    elif cantidadKm == "" or float(cantidadKm) < 0:
        print("El valor no puede ser vacío ni negativo.")
        valido = False

    else:
        print("Cantidad de Km válida.")

    return valido


def validarCostoKm(costoKm):
    """
    Valida que el costo por kilómetro sea un número positivo (entero o decimal).
    Muestra mensajes de error o confirmación. Devuelve True o False.
    """

    costoKm = costoKm.strip()
    valido = True

    # Verificar que sea numérico (permite un solo punto)
    if not costoKm.replace(".", "", 1).isdigit():
        print("Error: el costo debe ser un valor numérico.")
        valido = False

    elif costoKm.count(".") > 1:
        print("Solo se permite un punto decimal en el valor.")
        valido = False

    elif costoKm == "" or float(costoKm) <= 0:
        print("El costo no puede ser vacío, cero o negativo.")
        valido = False

    else:
        print("Costo por Km válido.")

    return valido

