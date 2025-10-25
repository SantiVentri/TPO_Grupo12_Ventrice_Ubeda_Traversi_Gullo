import time

def obtenerFechaHora():
    """
    Obtiene la fecha y hora actual en formato YYYY.MM.DD HH.MM.SS
    """
    fechaHora = time.strftime("%Y.%m.%d %H.%M.%S")

    return fechaHora

def validarFechaHora(fechaHora):
    """
    Valida una fecha y hora en formato 'YYYY.MM.DD HH.MM.SS'.
    Parámetro:
    - fechaHora (str): cadena con la fecha y hora a validar.
    Salida:
    - Devuelve True si es válida, False en caso contrario.
    """

    formato = "YYYY.MM.DD HH.MM.SS"

    # Verificar longitud exacta
    if len(fechaHora) != 19:
        print(f"La fecha y hora debe tener el formato {formato}")
        return False

    # Verificar estructura fija (puntos y espacios)
    if (fechaHora[4] != "." or fechaHora[7] != "." or
        fechaHora[10] != " " or fechaHora[13] != "." or
        fechaHora[16] != "." ):
        print(f"La fecha y hora debe tener el formato {formato}")
        return False

    # Extraer partes numéricas
    año = fechaHora[0:4]
    mes = fechaHora[5:7]
    dia = fechaHora[8:10]
    hora = fechaHora[11:13]
    minuto = fechaHora[14:16]
    segundo = fechaHora[17:19]

    # Debug - muestra lo que se está extrayendo
    print(f"Analizando: Año={año}, Mes={mes}, Día={dia}, Hora={hora}, Minuto={minuto}, Segundo={segundo}")

    # Verificar que todas las partes sean dígitos
    if not (año.isdigit() and mes.isdigit() and dia.isdigit() and hora.isdigit() and minuto.isdigit() and segundo.isdigit()):
        print(f"La fecha y hora debe tener el formato {formato}")
        return False

    # Convertir a enteros manualmente
    año = int(año)
    mes = int(mes)
    dia = int(dia)
    hora = int(hora)
    minuto = int(minuto)
    segundo = int(segundo)

    # Validaciones básicas de rango
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

    # Validar días según mes (usando time)
    dias_por_mes = [31, 29 if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not (1 <= dia <= dias_por_mes[mes - 1]):
        print("El día no corresponde al mes indicado")
        return False

    # Validar que sea una fecha válida
    partes = (año, mes, dia, hora, minuto, segundo, 0, 0, -1)
    fecha_formateada = time.strftime("%Y.%m.%d %H.%M.%S", partes)
    if fecha_formateada != fechaHora:
        print(f"La fecha y hora debe tener el formato {formato} y ser válida")
        return False
    
    return True