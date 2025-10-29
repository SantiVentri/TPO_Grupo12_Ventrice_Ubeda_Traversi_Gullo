"""
-----------------------------------------------------------------------------------------------
Título: Funciones de Archivos
Fecha: 20/10/2025
Autores: Santino Ventrice, Valentina Ubeda, Santino Traversi y Rocco Gullo

Descripción: Funciones relacionadas a la gestión de archivos.

Pendientes:
-----------------------------------------------------------------------------------------------
"""
#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def abrirArchivo(ruta, modo):
    """
    Esta función se encarga de intentar abrir el archivo de la ruta recibida en el modo recibido.
    Parámetros:
    - ruta (str): La dirección del archivo a abrir
    - modo (str): El modo de apertura del archivo (r, w, a)
    Salida:
    - archivo/None: En caso de éxito, se devuelve el archivo. En caso de error, se devuelve None
    """

    try:
        if modo not in ["r", "w", "a"]:
            raise Exception("El modo de apertura no es válido.\n")
        
        archivo = open(ruta, modo, encoding="utf-8")
        return archivo

    except (FileNotFoundError, OSError):
        print("Error: No se encontró el archivo. Verifique su ubicación y sus permisos.\n")
        return None
    
    except Exception as e:
        print(f"Error: Hubo un error al abrir el archivo. Detalles: {e}\n")
        return None
    
def cerrarArchivo(archivo):
    """
    Esta función se encarga de intentar cerrar el archivo recibido.
    Parámetros:
    - archivo: El archivo a cerrar
    """
    
    try:
        if archivo is None:
            print("Error: El archivo proporcionado no existe.\n")
            return
        archivo.close()

    except:
        pass