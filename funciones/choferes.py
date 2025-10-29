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

def listarChoferes(choferes):
    """
    Esta función se encarga de mostrar un listado de choferes activos con sus datos formateados.
    Parámetros:
    - choferes (dict): Diccionario de choferes con sus datos.
    """
    print("--------------------------------------")
    print("MENÚ DE CHOFERES > Listado de choferes")
    print("--------------------------------------\n")

    try:
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

    except Exception as e:
        print("Error al listar choferes.")
        print(f"Detalles: {e}")