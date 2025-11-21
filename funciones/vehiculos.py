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
def solicitarPatente(vehiculos, tipo="nueva"):
    """
    Esta función solicita y valida la patente del vehículo.
    Parámetros:
    - vehiculos (dict): Diccionario de vehículos para verificar existencia.
    - tipo (str): "nueva" para patentes nuevas, "existente" para patentes ya registradas.
    Salida:
    - patente (str): La patente validada.
    """
    patenteValida=False
    while not patenteValida:
        patente = input("Ingrese la patente del vehículo (ej. AE456GH): ").upper()
        if tipo == "nueva":
            patenteValida = validarPatente(patente, vehiculos)
        elif tipo == "existente":
            patenteValida = validarPatenteExistente(patente, vehiculos)

    return patente

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

def validarPatenteExistente(patente, vehiculos):
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
        if not (patente in vehiculos):
            print("No existe un vehículo con esa patente.")
            patenteValida = False

    return patenteValida

# ------------------ Solicitar y validar año de compra de vehículo ------------------
def solicitarAñoCompra():
    """
    Esta función solicita y valida el año de compra del vehículo.
    Salida:
    - añoCompra (int): El año de compra validado.
    """
    añoValido = False
    while not añoValido:
        añoCompra = input("Ingrese el año de compra del vehículo: ")
        añoValido = validarAñoCompra(añoCompra)

    return int(añoCompra)

def validarAñoCompra(añoCompra):
    """
    Valida que el año de compra del vehículo sea correcto. Muestra mensajes de error o confirmación.
    Parámetros:
    - añoCompra (str): El año a validar.
    Salida:
    - añoValido (bool): Indica si el año es válido (True) o no (False).
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

# ------------------ Solicitar y validar costo x km ------------------
def solicitarCostoKm():
    """
    Esta función solicita y valida el costo por kilómetro del vehículo.
    Salida:
    - costoKm (float): El costo por kilómetro validado.
    """

    costoValido = False
    while not costoValido:
        costoKm = input("Ingrese el costo por Km: ")
        costoValido = validarCostoKm(costoKm)

    return float(costoKm)

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

# ------------------ Agregar y modificar infracciones ------------------
def agregarInfraccion(vehiculo, descripcion):
    """
    Agrega una nueva infracción al vehículo.
    """
    descripcion = descripcion.strip()

    if descripcion == "":
        print("La descripción no puede estar vacía.")
        return

    clave = f"infraccion{len(vehiculo['infracciones']) + 1}"
    vehiculo["infracciones"][clave] = descripcion
    print(f"Se agregó la infracción '{descripcion}' correctamente.")

def eliminarInfraccion(vehiculo, claveEliminar):
    """
    Elimina una infracción existente por su clave (ej: infraccion1).
    """
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

def mostrarInfracciones(vehiculo):
    """
    Muestra todas las infracciones actuales del vehículo.
    """
    infracciones = vehiculo["infracciones"]

    if len(infracciones) == 0:
        print("Este vehículo no tiene infracciones registradas.")
    else:
        print("\nInfracciones actuales del vehículo:")
        for clave, desc in infracciones.items():
            print(f"  {clave}: {desc}")

# ------------------ Listado de vehículos ------------------
def listarVehiculos(vehiculos):
    """
    Muestra una lista de todos los vehículos registrados.
    """
    if len(vehiculos) == 0:
        print("No hay vehiculos cargados.")
        return
    
    else: 
        encabezado = ["Patente", "Modelo", "Año", "Km", "Costo/Km", "Activo", "Infracciones"]
        tabla = []
        
        #Cargar datos de cada vehiculo
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
        
        #Calcular ancho de cada columna 
        anchos=[max(len(str(fila[i])) for fila in ([encabezado] + tabla)) for i in range(len(encabezado))]

        #Funcion para imprimir una linea dvisoria 
        def linea():
            print("+" + "+".join("-" * (anchos[i] + 2) for i in range(len(anchos))) + "+")
        
        #Funcion para imprimir una fila formateada 
        def filaTexto(fila):
            print(" | " + " | ".join(str(fila[i]).ljust(anchos[i]) for i in range(len(fila))) + " |")
        
        #Imprimir la tabla completa
        linea()
        filaTexto(encabezado)
        linea()
        for f in tabla:
            filaTexto(f)
        linea()

    print("\n")