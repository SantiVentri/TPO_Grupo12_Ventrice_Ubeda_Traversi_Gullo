"""
-----------------------------------------------------------------------------------------------
Título: Funciones de Rutas
Fecha: 20/10/2025
Autores: Santino Ventrice, Valentina Ubeda, Santino Traversi y Rocco Gullo

Descripción: Funciones relacionadas a la gestión de rutas.
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import time
import json
from funciones.archivos import abrirArchivo, cerrarArchivo
from funciones.choferes import existeLegajo, legajoActivo, solicitarKm
from funciones.vehiculos import solicitarPatente

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
# ------------------ Funciones de rutas ------------------
def registrarRuta():
    """
    Registra una nueva ruta en el sistema.
    """

    # Rutas de archivos de los diccionarios
    rutaChoferes = "diccionarios/choferes.json"
    rutaVehiculos = "diccionarios/vehiculos.json"
    rutaRutas = "diccionarios/rutas.json"

    # Cargar datos de choferes
    archivo = abrirArchivo(rutaChoferes, "r")
    if archivo is not None:
        choferes = json.load(archivo)
        cerrarArchivo(archivo)
    else:
        choferes = {}

    # Cargar datos de vehículos
    archivo = abrirArchivo(rutaVehiculos, "r")
    if archivo is not None:
        vehiculos = json.load(archivo)
        cerrarArchivo(archivo)
    else:
        vehiculos = {}

    # Cargar datos de rutas
    archivo = abrirArchivo(rutaRutas, "r")
    if archivo is not None:
        rutas = json.load(archivo)
        cerrarArchivo(archivo)
    else:
        rutas = {}

    # Ingresar legajo
    while True:
        legajo = input("Ingrese el legajo del chofer (o '0' para salir): ")

        if legajo == "0":
            return

        if existeLegajo(legajo) and legajoActivo(legajo):
            break
        else:
            print("El legajo ingresado no existe. Por favor, intente nuevamente.")

    # Ingresar patente
    patente = solicitarPatente(vehiculos, "existente")

    # Ingresar kms
    totalKm = solicitarKm()

    # Ingresar salida
    fechaSalida = solicitarFechaHora()

    # Ingresar llegada
    fechaLlegada = solicitarFechaHora()

    # Confirmación
    print("\nResumen de la ruta a registrar:")
    print(f"Chofer: LU{legajo} - {choferes[legajo]['nombre']} {choferes[legajo]['apellido']}")
    print(f"Vehículo: {patente} - {vehiculos[patente]['modelo']}")
    print(f"Km recorridos: {totalKm} km")
    print(f"Fecha y hora de salida: {fechaSalida}")
    print(f"Fecha y hora de llegada: {fechaLlegada}")
    confirmar = input("¿Desea registrar esta ruta? (s/n): ").lower()

    if confirmar == "s" or confirmar == "si":
        # Obtener la fecha y hora actual para la clave
        fechaHora = obtenerFechaHora()

        # Calcular costo de la ruta
        costoKm = vehiculos[patente]['costoKm']
        costoRuta = totalKm * costoKm

        # Guardar ruta
        rutas[fechaHora] = {
            "idLegajo": legajo,
            "idPatente": patente,
            "totalKm": totalKm,
            "costoRuta": costoRuta,
            "horaSalida": fechaSalida,
            "horaLlegada": fechaLlegada
        }

        # Actualizar km del chofer y vehículo
        choferes[legajo]['cantidadKm'] += totalKm
        vehiculos[patente]['cantidadKm'] += totalKm

        # Abrir archivo de choferes en modo escritura
        archivo = abrirArchivo(rutaChoferes, "w")
        if archivo is not None:
            json.dump(choferes, archivo, indent=4, ensure_ascii=False)
            cerrarArchivo(archivo)
        else:
            print("No se pudo guardar el chofer. Verifique el archivo.")

        # Abrir archivo de vehiculos en modo escritura
        archivo = abrirArchivo(rutaVehiculos, "w")
        if archivo is not None:
            json.dump(vehiculos, archivo, indent=4, ensure_ascii=False)
            cerrarArchivo(archivo)
        else:
            print("No se pudo guardar el chofer. Verifique el archivo.")

        # Abrir archivo de rutas en modo escritura
        archivo = abrirArchivo(rutaRutas, "w")
        if archivo is not None:
            json.dump(rutas, archivo, indent=4, ensure_ascii=False)
            cerrarArchivo(archivo)

            print(f"\nRuta registrada exitosamente.\n")
        else:
            print("No se pudo guardar el chofer. Verifique el archivo.")

# ------------------ Funciones individuales de rutas ------------------
def obtenerFechaHora():
    """
    Obtiene la fecha y hora actual en formato YYYY.MM.DD HH.MM.SS
    """
    try:
        fechaHora = time.strftime("%Y.%m.%d %H.%M.%S")
        return fechaHora
    except Exception as e:
        print(f"Error al obtener la fecha y hora actual: {e}")
        return "0000.00.00 00.00.00"   # Valor de emergencia

def solicitarFechaHora():
    """
    Solicita al usuario una fecha y hora en formato 'YYYY.MM.DD HH.MM.SS' y la valida.
    """
    fechaHoraValida = False

    while not fechaHoraValida:
        try:
            fechaHora = input("Ingrese la fecha y hora (formato 'YYYY.MM.DD HH.MM.SS'): ")
        except Exception as e:
            print(f"Error al leer la entrada: {e}")
            continue

        try:
            fechaHoraValida = validarFechaHora(fechaHora)
        except Exception as e:
            print(f"Error inesperado validando la fecha: {e}")
            fechaHoraValida = False

    return fechaHora

def validarFechaHora(fechaHora):
    """
    Valida una fecha y hora en formato 'YYYY.MM.DD HH.MM.SS'.
    """
    formato = "YYYY.MM.DD HH.MM.SS"

    try:
        # Verificar longitud
        if len(fechaHora) != 19:
            print(f"La fecha y hora debe tener el formato {formato}")
            return False

        # Verificar estructura fija
        if (fechaHora[4] != "." or fechaHora[7] != "." or
            fechaHora[10] != " " or fechaHora[13] != "." or
            fechaHora[16] != "."):
            print(f"La fecha y hora debe tener el formato {formato}")
            return False

        # Extraer partes con try por si hay error de índices
        try:
            año = fechaHora[0:4]
            mes = fechaHora[5:7]
            dia = fechaHora[8:10]
            hora = fechaHora[11:13]
            minuto = fechaHora[14:16]
            segundo = fechaHora[17:19]
        except Exception:
            print("Error al extraer partes de la fecha.")
            return False

        print(f"Analizando: Año={año}, Mes={mes}, Día={dia}, Hora={hora}, Minuto={minuto}, Segundo={segundo}")

        # Verificar dígitos
        if not (año.isdigit() and mes.isdigit() and dia.isdigit()
                and hora.isdigit() and minuto.isdigit() and segundo.isdigit()):
            print(f"La fecha y hora debe tener el formato {formato}")
            return False

        # Convertir a enteros de forma segura
        try:
            año = int(año)
            mes = int(mes)
            dia = int(dia)
            hora = int(hora)
            minuto = int(minuto)
            segundo = int(segundo)
        except ValueError:
            print("Los valores numéricos ingresados no son válidos.")
            return False

        # Validaciones de rango
        if año < 2025:
            print("El año debe ser mayor o igual a 2025")
            return False
        if not (1 <= mes <= 12):
            print("El mes debe estar entre 01 y 12")
            return False
        if not (0 <= hora <= 23):
            print("La hora debe estar entre 00 y 23")
            return False
        if not (0 <= minuto <= 59):
            print("Los minutos deben estar entre 00 y 59")
            return False
        if not (0 <= segundo <= 59):
            print("Los segundos deben estar entre 00 y 59")
            return False

        # Validación de días según el mes
        diasPorMes = [
            31,
            29 if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)) else 28,
            31, 30, 31, 30, 31, 31, 30, 31, 30, 31
        ]

        if not (1 <= dia <= diasPorMes[mes - 1]):
            print("El día no corresponde al mes indicado")
            return False

        # Validación final con time.strftime
        try:
            partes = (año, mes, dia, hora, minuto, segundo, 0, 0, -1)
            fechaFormateada = time.strftime("%Y.%m.%d %H.%M.%S", partes)
        except Exception:
            print("Error al formatear la fecha para validar.")
            return False

        if fechaFormateada != fechaHora:
            print(f"La fecha y hora debe tener el formato {formato} y ser válida")
            return False

        return True

    except Exception as e:
        print(f"Error inesperado en la validación: {e}")
        return False

def codigoRuta():
    """
    Solicita al usuario un código de ruta y lo devuelve.
    """
    codigo = input("Ingrese el código de la ruta: ").strip()
    return codigo

def datosRuta():
    """
    Solicita los datos necesarios para crear una ruta y devuelve un diccionario.
    """
    print("\n--- INGRESO DE DATOS DE LA RUTA ---")
    origen = input("Ingrese el origen: ")
    destino = input("Ingrese el destino: ")
    fechaHora = solicitarFechaHora()   # Usa tu función existente

    datos = {
        "origen": origen,
        "destino": destino,
        "fechaHora": fechaHora
    }

    return datos