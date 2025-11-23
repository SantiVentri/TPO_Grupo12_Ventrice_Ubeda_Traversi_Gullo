"""
-----------------------------------------------------------------------------------------------
Título: Funciones de Choferes
Fecha: 20/10/2025
Autores: Santino Ventrice, Valentina Ubeda, Santino Traversi y Rocco Gullo

Descripción: Funciones relacionadas a la gestión de choferes.

Pendientes:
-----------------------------------------------------------------------------------------------
"""
#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import random, json, re
from funciones.archivos import abrirArchivo, cerrarArchivo

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
# ------------------ Funciones de choferes ------------------
def registrarChofer():
    """
    Registra nuevos choferes en el sistema.
    """

    # Ruta de archivo del diccionario de choferes
    rutaChoferes = "diccionarios/choferes.json"

    while True:
        # Solicitar nombre
        nombre = solicitarNombre()
        
        # Solicitar apellido
        apellido = solicitarApellido()

        # Solicitar email
        email = solicitarEmail()

        # Solicitar teléfono
        telefono = solicitarTelefono()

        # Solicitar cantidad de km recorridos
        cantidadKm = solicitarKm()

        # Agregar turnos
        turnos = solicitarTurnos()

        # Cargar datos de choferes
        archivo = abrirArchivo(rutaChoferes, "r")
        if archivo is not None:
            choferes = json.load(archivo)
            cerrarArchivo(archivo)
        else:
            choferes = {}  # Si no existe, iniciar vacío

        # Crear legajo
        legajo = crearLegajo()

        # Crear diccionario con los datos del chofer
        datosChoferes = {
            "activo": True,
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "telefono": telefono,
            "cantidadKm": cantidadKm,
            "turnos": turnos
        }

        # Asignar los datos del chofer al chofer
        choferes[legajo] = datosChoferes

        # Abrir archivo en modo escritura
        archivo = abrirArchivo(rutaChoferes, "w")
        if archivo is not None:
            json.dump(choferes, archivo, indent=4, ensure_ascii=False)
            cerrarArchivo(archivo)

            # Mensaje de éxito
            print(f"\nSe agregó al chofer {nombre} {apellido}, LU{legajo} exitosamente.\n")

            # Preguntar si desea agregar otro chofer
            agregarOtro = input("¿Desea agregar otro chofer? (s/n): ").lower()
            if agregarOtro != "s" and agregarOtro != "si":
                break
        else:
            print("No se pudo guardar el chofer. Verifique el archivo.")

def modificarChofer():
    """
    Permite modificar los datos de un chofer existente.
    """
    
    # Ruta de archivo del diccionario de choferes
    rutaChoferes = "diccionarios/choferes.json"

    # Cargar datos de choferes
    archivo = abrirArchivo(rutaChoferes, "r")
    if archivo is not None:
        choferes = json.load(archivo)
        cerrarArchivo(archivo)
    else:
        choferes = {}  # Si no existe, iniciar vacío

    while True:
        # Preguntar legajo de chofer a modificar
        legajo = input("Ingrese el legajo del chofer a modificar (o '0' para salir): ")

        # Si el número ingresado es 0, se sale del bucle
        if legajo == "0":
            print("Saliendo de la modificación de choferes.\n")
            break
        elif not legajo.isdigit() or legajo not in choferes:
            print("Legajo inválido. Intente nuevamente.")
            break

        # Formatear celda de teléfono
        telefonoFormateado = f"+54 11 {str(choferes[legajo]['telefono'])[4:]}-{str(choferes[legajo]['telefono'])[:4]}"

        # Seleccionar dato a modificar
        print("\nDatos actuales del chofer:")
        print(f"1. Nombre: {choferes[legajo]['nombre']}")
        print(f"2. Apellido: {choferes[legajo]['apellido']}")
        print(f"3. Email: {choferes[legajo]['email']}")
        print(f"4. Teléfono: {telefonoFormateado}")
        print(f"5. Cantidad de km: {choferes[legajo]['cantidadKm']}")
        print("6. Ver turnos")
        print("\n¿Qué dato desea modificar?")
        
        opcion = input("Ingrese el número de la opción (1-5): ")
        
        if opcion == "1":
            # Ingresar nuevo nombre
            nuevoNombre = solicitarNombre()

            # Guardar nuevo nombre
            choferes[legajo]['nombre'] = nuevoNombre

            print("\nDato modificado exitosamente.")
            
        elif opcion == "2":
            # Ingresar nuevo apellido
            nuevoApellido = solicitarApellido()

            # Guardar nuevo apellido
            choferes[legajo]['apellido'] = nuevoApellido

            print("\nDato modificado exitosamente.")

        elif opcion == "3":
            # Ingresar nuevo email
            nuevoEmail = solicitarEmail()

            # Guardar nuevo email
            choferes[legajo]['email'] = nuevoEmail

            print("\nDato modificado exitosamente.")

        elif opcion == "4":
            # Solicitar teléfono
            nuevoTelefono = solicitarTelefono()

            # Guardar nuevo teléfono
            choferes[legajo]['telefono'] = nuevoTelefono

            print("\nDato modificado exitosamente.")

        elif opcion == "5":
            # Ingresar nueva cantidad de km recorridos
            nuevosKm = solicitarKm()

            # Guardar nueva cantidad de km
            choferes[legajo]['cantidadKm'] = nuevosKm

            print("\nDato modificado exitosamente.")
                    
        elif opcion == "6":
            # Ver turnos
            print("\nTurnos actuales del chofer:")
            for i in range(1, 4):
                if f"turno{i}" in choferes[legajo]['turnos']:
                    print(f"{i}. {choferes[legajo]['turnos'][f'turno{i}']}")
                else:
                    print(f"{i}. Sin turno asignado")

            # Seleccionar turno a modificar
            turnoModificar = input("\nIngrese el número del turno a modificar (1-3) o '0' para salir: ")

            if turnoModificar == "0":
                print("Saliendo de la modificación de turnos.\n")
                break
            elif turnoModificar not in ["1", "2", "3"]:
                print("Opción inválida. Intente nuevamente.")
            else:
                turnosExistentes = list(choferes[legajo]['turnos'].values())
                nuevoTurno = solicitarUnTurno(int(turnoModificar), turnosExistentes)

                if nuevoTurno:
                    choferes[legajo]['turnos'][f'turno{turnoModificar}'] = nuevoTurno
                else:
                    if f'turno{turnoModificar}' in choferes[legajo]['turnos']:
                        del choferes[legajo]['turnos'][f'turno{turnoModificar}']

        else:
            print("Opción inválida.")
            
        # Abrir archivo en modo escritura
        archivo = abrirArchivo(rutaChoferes, "w")
        if archivo is not None:
            json.dump(choferes, archivo, indent=4, ensure_ascii=False)
            cerrarArchivo(archivo)
        else:
            print("No se pudo guardar el chofer. Verifique el archivo.")

def desactivarChofer():
    """
    Permite desactivar (dar de baja lógica) a un chofer.
    """
    
    # Ruta de archivo del diccionario de choferes
    rutaChoferes = "diccionarios/choferes.json"
    
    # Cargar datos de choferes
    archivo = abrirArchivo(rutaChoferes, "r")
    if archivo is not None:
        choferes = json.load(archivo)
        cerrarArchivo(archivo)
    else:
        choferes = {}  # Si no existe, iniciar vacío

    while True:
        # Se pide el número de legajo a eliminar
        legajo = input("Ingrese el legajo del chofer a desactivar (o '0' para salir): ")

        # Si el número ingresado es 0, se sale del bucle
        if legajo == "0":
            break
        # Validar legajo
        elif not legajo.isdigit() or legajo not in choferes:
            print("Legajo inválido. Intente nuevamente.")
        else:
            chofer = choferes[legajo] # Obtener datos del chofer

            # Mensaje de confirmación
            confirmar = input(f"¿Está seguro que desea desactivar al chofer {chofer['nombre']} {chofer['apellido']} (LU{legajo})? (s/n): ").lower()
            
            # Si el usuario confirma la acción, se desactiva el chofer. Sino, se cancela la operación
            if confirmar == "s" or confirmar == "si":
                choferes[legajo]["activo"] = False

                # Abrir archivo en modo escritura usando tu función
                archivo = abrirArchivo(rutaChoferes, "w")
                if archivo is not None:
                    json.dump(choferes, archivo, indent=4, ensure_ascii=False)
                    cerrarArchivo(archivo)

                    # Mensaje de éxito
                    print(f"\nSe desactivó al chofer {chofer['nombre']} {chofer['apellido']}, LU{legajo} exitosamente.\n")
                else:
                    print("No se pudo guardar el chofer. Verifique el archivo.")
            else:
                print("Desactivación cancelada.\n")

def listarChoferes():
    """
    Esta función se encarga de mostrar un listado de choferes activos con sus datos formateados.
    Parámetros:
    - choferes (dict): Diccionario de choferes con sus datos.
    """
    try:
        # Crear variable con dirección de archivo del diccionario de choferes
        rutaChoferes = "diccionarios/choferes.json"

        # Cargar datos de choferes
        archivo = abrirArchivo(rutaChoferes, "r")
        if archivo is not None:
            choferes = json.load(archivo)
            cerrarArchivo(archivo)
        else:
            choferes = {}  # Si no existe, iniciar vacío
        
        # Crear matriz con los datos de los choferes
        matriz = []
        for legajo, datos in choferes.items():
            if datos["activo"] == True:
                # Si hay turnos asignados, mostrarlos. Sino, mostrar mensaje.
                turnos = ", ".join(datos["turnos"].values()) or "Sin turnos asignado"
                
                fila = [
                    legajo,
                    f"{datos['nombre']} {datos['apellido']}",
                    f"{datos['email']}",
                    f"+54 11 {str(datos['telefono'])[:4]}-{str(datos['telefono'])[4:]}",
                    f"{datos['cantidadKm']}",
                    turnos
                ]
                matriz.append(fila)

        if choferes != {}:
            print("SE LISTAN LOS CHOFERES ACTIVOS:\n")
            
            # Imprimir los títulos de la tabla
            print("-" * 152)
            print(f"|{"Legajo":^11}|{"Nombre":^18}|{"Email":^27}|{"Teléfono":^18}|{"Km Recorridos":^15}|{"Turnos":^56}|")
            print("-" * 152)
            # Recorrer matriz con for i / for j e imprimir tabla
            for i in range(len(matriz)):
                print("|", end="")
                for j in range(len(matriz[i])):
                    if j == 0:
                        # Imprimir legajo
                        print(f" LU{matriz[i][j]:^8}|", end="")
                    elif j == 1:
                        # Reemplazar los ultimos 3 caracteres del nombre por "..." si es muy largo
                        nombre = matriz[i][j]
                        if len(nombre) > 16:
                            nombre = nombre[:13] + "..."
                        print(f" {nombre:<17}|", end="")
                    elif j == 2:
                        # Reemplazar los ultimos 3 caracteres del email por "..." si es muy largo
                        email = matriz[i][j]
                        if len(email) > 25:
                            email = email[:22] + "..."
                        print(f" {email:<26}|", end="")
                    elif j == 3:
                        # Imprimir teléfono
                        print(f" {matriz[i][j]:^17}|", end="")
                    elif j == 4:
                        # Imprimir km recorridos
                        print(f"{matriz[i][j]:>14} |", end="")
                    elif j == 5:
                        # Imprimir turnos
                        print(f" {matriz[i][j]:<55}|", end="")
                print()  # salto de línea entre filas

            # Cerrar tabla
            print("-" * 152)

    except Exception as e:
        print("Error al listar choferes.")
        print(f"Detalles: {e}")

# ------------------ Creación de legajos ------------------
def crearLegajo():
    """
    Esta función genera un legajo único para un nuevo chofer.
    Salida:
    - legajo (int): Legajo único generado para el nuevo chofer.
    """
    
    # Generar el legajo de 5 dígitos del chofer
    while True:
        legajo = random.randint(10000, 99999)
        if existeLegajo(legajo) == False:
            return legajo
        
def existeLegajo(legajo):
    """
    Esta función valida si un legajo de chofer existe en el sistema.
    """

    # Inicializar ruta del archivo de choferes
    rutaChoferes = "diccionarios/choferes.json"

    # Cargar datos de choferes
    archivo = abrirArchivo(rutaChoferes, "r")
    if archivo is not None:
        choferes = json.load(archivo)
        cerrarArchivo(archivo)
    else:
        choferes = {}

    if legajo not in choferes:
        return False # El legajo no existe
    else:
        return True # El legajo existe

# ------------------ Solicitar y validar nombre y apellido ------------------
def solicitarNombre():
    """
    Esta función solicita el nombre y apellido de un chofer y los valida.
    Salidas:
    - nombre (str): Nombre válido del chofer.
    - apellido (str): Apellido válido del chofer.
    """
    nombreValido = False
    while not nombreValido:
        nombre = input("Ingrese el primer nombre del chofer: ")
        nombreValido = validarNombre("nombre", nombre)

    return nombre

def solicitarApellido():
    """
    Esta función solicita el apellido de un chofer y los valida.
    Salidas:
    - apellido (str): Apellido válido del chofer.
    """
    apellidoValido = False
    while not apellidoValido:
        apellido = input("Ingrese el apellido del chofer: ")
        apellidoValido = validarNombre("apellido", apellido)

    return apellido

def validarNombre(tipo, texto):
    """
    Esta función valida el nombre o apellido de un chofer.
    Parámetros:
    - tipo (str): Indica si se está validando el nombre o el apellido.
    - texto (str): El texto a validar.
    Salidas:
    - textoValido (bool): Indica si el texto es válido.
    """
    textoValido = True

    try:
        if not texto or texto.strip() == "":
            raise Exception(f"El {tipo} no puede estar vacío. Intente nuevamente.")
        elif len(texto) < 3:
            raise Exception(f"El {tipo} debe tener al menos 3 caracteres. Intente nuevamente.")
        elif len(texto) > 15:
            raise Exception(f"El {tipo} no puede exceder los 15 caracteres. Intente nuevamente.")

        for char in texto:
            if not (char.isalpha() or char == " "):
                raise Exception(f"El {tipo} solo puede contener letras y espacios. Intente nuevamente.")

    except Exception as e:
        textoValido = False
        print(e)

    finally:
        return textoValido

# ------------------ Solicitar y validar email ------------------
def solicitarEmail():
    """
    Esta función solicita el email de un chofer y lo valida.
    Salidas:
    - email (str): Email válido del chofer.
    """

    emailValido = False
    while not emailValido:
        email = input("Ingrese el email del chofer: ")
        emailValido = validarEmail(email)

    return email

def validarEmail(email):
    """
    Esta función valida el email de un chofer.
    Parámetros:
    - email (str): El email a validar.
    Salidas:
    - emailValido (bool): Indica si el email es válido.
    """

    emailValido = True

    pat = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    try:
        if not re.match(pat, email):
            raise Exception("El email no es válido. Intente nuevamente.")
        
    except Exception as e:
        emailValido = False
        print(e)

    return emailValido

# ------------------ Solicitar y validar teléfonos ------------------
def solicitarTelefono():
    """
    Esta función solicita el teléfono de un chofer y lo valida.
    Salidas:
    - telefono (str): Teléfono válido del chofer.
    """

    telValido = False
    while not telValido:
        telefono = input("Ingrese el teléfono del chofer: +54 11 ")
        telValido = validarTelefono(telefono)

    return telefono

def validarTelefono(telefono):
    """
    Esta función valida el teléfono de un chofer.
    Parámetros:
    - telefono (str): El teléfono a validar.
    Salidas:
    - telValido (bool): Indica si el teléfono es válido.
    """

    telValido = True

    try:
        int(telefono)

        if len(telefono) != 8:
            raise Exception("El teléfono debe tener 8 dígitos. Intente nuevamente.")
        
    except ValueError:
        telValido = False
        print("El teléfono solo puede contener números. Intente nuevamente.")

    except Exception as e:
        telValido = False
        print(e)

    finally:
        return telValido

# ------------------ Solicitar y validar kms ------------------
def solicitarKm():
    kmValidos = False
    while not kmValidos:
        cantidadKm = input("Ingrese la cantidad de km (Presione Enter para 0): ")
        if cantidadKm.strip() == "":
            cantidadKm = "0"
        kmValidos = validarKm(cantidadKm)

    return float(cantidadKm)

def validarKm(km):
    """
    Esta función valida la cantidad de km recorridos por un chofer. Lanza un error si no es un número positivo.
    Parámetros:
    - km (str): La cantidad km a validar.
    Salidas:
    - kmValidos (bool): Indica si la cantidad de km es válido.
    """

    kmValido = True

    try:
        km = float(km)
        if km < 0:
            kmValido = False
            print("Los kilómetros no pueden ser negativos. Intente nuevamente.")

    except ValueError:
        kmValido = False
        print("Los kilómetros deben ser un número válido. Intente nuevamente.")

    finally:
        return kmValido

# ------------------ Solicitar y validar turnos ------------------
def solicitarTurnos():
    """
    Esta función solicita hasta 3 turnos para un chofer y los valida.
    Salidas:
    - turnos (dict): Diccionario con los turnos válidos asignados al chofer.
    """

    turnos = {}
    for i in range(3):
        nuevoTurno = solicitarUnTurno(i + 1, turnos)
        if nuevoTurno:
            turnos[f"turno{i+1}"] = nuevoTurno

    return turnos

def solicitarUnTurno(numeroTurno, turnosExistentes):
    """
    Solicita un turno individual y lo valida.
    Parámetros:
    - numeroTurno (int): El número de turno que se está solicitando (1, 2 o 3).
    - turnosExistentes (dict): Diccionario de turnos ya asignados para validar duplicados.
    Salidas:
    - nuevoTurno (str|None): El string del turno válido o None si se dejó vacío.
    """
    while True:
        # Ingresar nuevo día
        diaTurno = input(f"Ingrese el día para el turno {numeroTurno} (Lunes, Martes, etc.) o '-' para dejarlo vacío: ")
        
        if diaTurno == "-":
            print(f"Turno {numeroTurno} quedará vacío.")
            return None
        
        # Ingresar nuevo horario
        horarioTurno = input("Ingrese el horario (Mañana, Tarde o Noche): ")
        
        # Crear y validar el turno
        nuevoTurno = f"{diaTurno.title()} - {horarioTurno.title()}"
        
        if validarTurno(turnosExistentes, nuevoTurno):
            print(f"Turno {nuevoTurno} agregado exitosamente.")
            return nuevoTurno

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
    turnoValido = True

    try:
        dia, horario = turno.split(" - ")

        if turno in turnos:
            turnoValido = False
            print("El chofer ya tiene asignado ese turno. Intente nuevamente.")
        else:
            diaValido = dia.title() in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
            if not diaValido:
                raise Exception("día")
            
            horarioValido = horario.title() in ["Mañana", "Tarde", "Noche"]
            if not horarioValido:
                raise Exception("horario")

    except ValueError:
        turnoValido = False
        print("Hubo un error al obtener el formato")

    except Exception as e:
        turnoValido = False
        print(f"El {e} del turno no es válido. Intente nuevamente.")

    finally:
        return turnoValido