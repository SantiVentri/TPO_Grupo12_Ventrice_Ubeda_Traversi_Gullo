"""
-----------------------------------------------------------------------------------------------
Título: Funciones de vehiculos
Fecha: 20/10/2025
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

# ------------------ Solicitar y validar patentes ------------------
# ------------------ Solicitar y validar patentes ------------------
def solicitarPatente(vehiculos, tipo="nueva"):
    """
    Esta función solicita y valida la patente del vehículo.
    Parámetros:
    - vehiculos (dict): Diccionario de vehículos para verificar existencia.
    - tipo (str): "nueva" para patentes nuevas, "existente" para patentes ya registradas.
    Salida:
    - patente (str): La patente validada.
    """
    patenteValida = False
    while not patenteValida:
        try:
            patente = input("Ingrese la patente del vehículo (ej. AE456GH): ").upper()
            
            if tipo == "nueva":
                patenteValida = validarPatente(patente, vehiculos)
            elif tipo == "existente":
                patenteValida = validarPatenteExistente(patente, vehiculos)
            else:
                print("Tipo de validación de patente desconocido.")
                patenteValida = False

        except Exception as e:
            # Cualquier error inesperado en el proceso de lectura/validación
            print(f"Ocurrió un error al procesar la patente: {e}")
            patenteValida = False

    return patente


def validarPatente(patente, vehiculos):
    """
    Valida una patente argentina (formato viejo AAA123 o nuevo AB123CD).
    Muestra los mensajes de error o confirmación y devuelve True/False.
    """
    try:
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

    except Exception as e:
        print(f"Ocurrió un error inesperado al validar la patente: {e}")
        return False


def validarPatenteExistente(patente, vehiculos):
    """
    Valida una patente argentina (formato viejo AAA123 o nuevo AB123CD).
    Muestra los mensajes de error o confirmación y devuelve True/False.
    """
    try:
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
            if not (patente in vehiculos):
                print("No existe un vehículo con esa patente.")
                patenteValida = False

        return patenteValida

    except Exception as e:
        print(f"Ocurrió un error inesperado al validar la patente existente: {e}")
        return False


# ------------------ Solicitar y validar año de compra de vehículo ------------------
def solicitarAñoCompra():
    """
    Esta función solicita y valida el año de compra del vehículo.
    Salida:
    - añoCompra (int): El año de compra validado.
    """
    añoValido = False
    añoCompra = None

    while not añoValido:
        añoCompra = input("Ingrese el año de compra del vehículo: ")
        try:
            añoValido = validarAñoCompra(añoCompra)
        except Exception as e:
            print(f"Ocurrió un error inesperado al validar el año: {e}")
            añoValido = False

    # Conversión final a int con manejo de errores por si algo raro se coló
    try:
        return int(añoCompra)
    except ValueError:
        print("Error al convertir el año a número. Se devolverá 0 por defecto.")
        return 0


def validarAñoCompra(añoCompra):
    """
    Valida que el año de compra del vehículo sea correcto. Muestra mensajes de error o confirmación.
    Parámetros:
    - añoCompra (str): El año a validar.
    Salida:
    - añoValido (bool): Indica si el año es válido (True) o no (False).
    """
    añoCompra = añoCompra.strip()

    try:
        # Verificar que sean solo números
        if not añoCompra.isdigit():
            raise ValueError(" El año de compra debe contener solo números.")

        # Verificar longitud (4 dígitos)
        if len(añoCompra) != 4:
            raise ValueError(" El año debe tener exactamente 4 dígitos (ej. 2022).")

        # Verificar rango lógico (ejemplo: entre 1980 y año actual)
        from datetime import datetime
        añoNum = int(añoCompra)
        añoActual = datetime.now().year

        if añoNum < 1980 or añoNum > añoActual:
            raise ValueError(f" El año debe estar entre 1980 y {añoActual}.")

    except ValueError as e:
        # Errores esperados de validación
        print(e)
        return False

    except Exception as e:
        # Cualquier error inesperado
        print(f"Ocurrió un error inesperado al validar el año: {e}")
        return False

    else:
        # Solo entra si no hubo ninguna excepción
        print(" Año de compra válido.")
        return True

    finally:
        # Bloque que se ejecuta siempre
        print(" Fin de la validación del año de compra.")


# ------------------ Solicitar y validar costo x km ------------------
def solicitarCostoKm():
    """
    Esta función solicita y valida el costo por kilómetro del vehículo.
    Salida:
    - costoKm (float): El costo por kilómetro validado.
    """
    costoValido = False
    costoKm = None

    while not costoValido:
        costoKm = input("Ingrese el costo por Km: ")
        try:
            costoValido = validarCostoKm(costoKm)
        except Exception as e:
            print(f"Ocurrió un error inesperado al validar el costo: {e}")
            costoValido = False

    # Conversión final a float con try/except por seguridad
    try:
        return float(costoKm)
    except ValueError:
        print("Error al convertir el costo a número. Se devolverá 0.0 por defecto.")
        return 0.0


def validarCostoKm(costoKm):
    """
    Valida que el costo por kilómetro sea un número positivo (entero o decimal).
    Muestra mensajes de error o confirmación.
    Parámetros:
    - costoKm (str): el costo por kilómetro a validar.
    Salida:
    - valido (bool): Indica si el costo es válido (True) o no (False).
    """
    costoKm = costoKm.strip()

    try:
        if costoKm == "":
            raise ValueError("El costo no puede ser vacío.")

        if costoKm.count(".") > 1:
            raise ValueError("Solo se permite un punto decimal en el valor.")

        # Intentamos convertir a float
        valor = float(costoKm)

        if valor <= 0:
            raise ValueError("El costo no puede ser cero o negativo.")

    except ValueError as e:
        # Errores esperados de validación
        print(e)
        return False

    except Exception as e:
        # Cualquier error inesperado
        print(f"Ocurrió un error inesperado al validar el costo por Km: {e}")
        return False

    else:
        print("Costo por Km válido.")
        return True


# ------------------ Agregar y modificar infracciones ------------------
def agregarInfraccion(vehiculo, descripcion):
    """
    Agrega una nueva infracción al vehículo.
    """
    try:
        descripcion = descripcion.strip()

        if descripcion == "":
            print("La descripción no puede estar vacía.")
            return

        clave = f"infraccion{len(vehiculo['infracciones']) + 1}"
        vehiculo["infracciones"][clave] = descripcion
        print(f"Se agregó la infracción '{descripcion}' correctamente.")

    except KeyError:
        print("Error: el vehículo no tiene la estructura esperada (falta 'infracciones').")
    except Exception as e:
        print(f"Ocurrió un error al agregar la infracción: {e}")


def eliminarInfraccion(vehiculo, claveEliminar):
    """
    Elimina una infracción existente por su clave (ej: infraccion1).
    """
    try:
        infracciones = vehiculo["infracciones"]

        if len(infracciones) == 0:
            print("Este vehículo no tiene infracciones registradas.")
            return

        if claveEliminar in infracciones:
            del infracciones[claveEliminar]
            print("Infracción eliminada correctamente.")

            # Reordenar nombres (para mantener infraccion1, infraccion2, ...)
            nuevas = {}
            for i, desc in enumerate(infracciones.values(), start=1):
                nuevas[f"infraccion{i}"] = desc
            vehiculo["infracciones"] = nuevas

        else:
            print("No existe una infracción con ese nombre.")

    except KeyError:
        print("Error: el vehículo no tiene la estructura esperada (falta 'infracciones').")
    except Exception as e:
        print(f"Ocurrió un error al eliminar la infracción: {e}")


def mostrarInfracciones(vehiculo):
    """
    Muestra todas las infracciones actuales del vehículo.
    """
    try:
        infracciones = vehiculo["infracciones"]

        if len(infracciones) == 0:
            print("Este vehículo no tiene infracciones registradas.")
        else:
            print("\nInfracciones actuales del vehículo:")
            for clave, desc in infracciones.items():
                print(f"  {clave}: {desc}")

    except KeyError:
        print("Error: el vehículo no tiene la estructura esperada (falta 'infracciones').")
    except Exception as e:
        print(f"Ocurrió un error al mostrar las infracciones: {e}")


# ------------------ Listado de vehículos ------------------
def listarVehiculos(vehiculos):
    """
    Muestra una lista de todos los vehículos registrados.
    """
    try:
        if len(vehiculos) == 0:
            print("No hay vehiculos cargados.")
            return
        
        else: 
            encabezado = ["Patente", "Modelo", "Año", "Km", "Costo/Km", "Activo", "Infracciones"]
            tabla = []
            
            # Cargar datos de cada vehiculo
            for patente, datos in vehiculos.items():
                # Solo procesar los vehículos activos
                if datos["activo"]:
                    fila = [
                        patente,
                        datos["modelo"],
                        datos["añoCompra"],
                        datos["cantidadKm"],
                        f"${datos['costoKm']:.2f}",
                        "Sí" if datos["activo"] else "No",
                        len(datos["infracciones"])
                    ]
                    tabla.append(fila)
            
            # Calcular ancho de cada columna 
            anchos = [max(len(str(fila[i])) for fila in ([encabezado] + tabla)) for i in range(len(encabezado))]

            # Función para imprimir una linea divisoria 
            def linea():
                print("+" + "+".join("-" * (anchos[i] + 2) for i in range(len(anchos))) + "+")
            
            # Función para imprimir una fila formateada 
            def filaTexto(fila):
                print(" | " + " | ".join(str(fila[i]).ljust(anchos[i]) for i in range(len(fila))) + " |")
            
            # Imprimir la tabla completa
            linea()
            filaTexto(encabezado)
            linea()
            for f in tabla:
                filaTexto(f)
            linea()

        print("\n")

    except KeyError as e:
        print(f"Error en la estructura de datos de un vehículo: falta la clave {e}.")
    except Exception as e:
        print(f"Ocurrió un error al listar los vehículos: {e}")
