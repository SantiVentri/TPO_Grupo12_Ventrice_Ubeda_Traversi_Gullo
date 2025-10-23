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

def validar_patente(patente):
    """
    Valida una patente argentina en formato viejo (AAA123) o nuevo (AB123CD).
    Devuelve (patenteValida, mensajeError)
    """
    patenteValida = True
    mensajeError = ""

    patente = patente.upper().strip()

    # Verifico largo correcto
    if len(patente) == 6:  # Formato viejo
        if not (patente[:3].isalpha() and patente[3:].isdigit()):
            patenteValida = False
            mensajeError = "La patente es incorrecta. Formato esperado: AAA123."

    elif len(patente) == 7:  # Formato nuevo
        if not (patente[:2].isalpha() and patente[2:5].isdigit() and patente[5:].isalpha()):
            patenteValida = False
            mensajeError = "La patente es incorrecta. Formato esperado: AB123CD."

    else:
        patenteValida = False
        mensajeError = "La patente debe tener 6 o 7 caracteres."

    return patenteValida, mensajeError


def validar_año_compra (añoCompra):
      """
      Validar que el año del vehiculo sea correcto
      """
      esValido = True
      mensajeError = ""

        # Verificar que sea numérico
      if not añoCompra.isdigit():
            esValido = False
            mensajeError = "El año debe contener solo números."

        # Verificar longitud
      elif len(añoCompra) != 4:
        esValido = False
        mensajeError = "El año debe tener 4 dígitos."

        # Verificar rango razonable
      else:
            año = int(añoCompra)
            if año < 1980 or año > 2025:
                esValido = False
                mensajeError = "El año debe estar entre 1980 y 2025."

    # Devuelve resultado al final
      return esValido, mensajeError

def validar_cant_km(cantidadKm):
    """
    Valida que un valor ingresado sea numérico (entero o decimal positivo).
    Devuelve una tupla (esValido, mensajeError)
    """
    esValido = True
    mensajeError = ""


    if not cantidadKm.replace(".", "", 1).isdigit():
        esValido = False
        mensajeError = "El valor debe ser numérico."
    elif cantidadKm.count(".") > 1:
        esValido = False
        mensajeError = "Solo puede tener un punto decimal."
    elif cantidadKm == "" or float(cantidadKm) < 0:
        esValido = False
        mensajeError = "El valor no puede ser vacío o negativo."

    return esValido, mensajeError

def validar_costo_km(costoKm):
    """
    Valida que el costo por kilómetro sea un número positivo (puede tener decimales).
    Devuelve una tupla (esValido, mensajeError)
    """
    esValido = True
    mensajeError = ""

    # Elimina espacios
    costoKm = costoKm.strip()

    # Verifica que no esté vacío
    if costoKm == "":
        esValido = False
        mensajeError = "El costo no puede estar vacío."

    # Verifica que tenga formato numérico (permite un solo punto)
    elif not costoKm.replace(".", "", 1).isdigit() or costoKm.count(".") > 1:
        esValido = False
        mensajeError = "El costo debe ser un número válido."

    # Verifica que no sea negativo
    elif float(costoKm) < 0:
        esValido = False
        mensajeError = "El costo no puede ser negativo."

    return esValido, mensajeError
