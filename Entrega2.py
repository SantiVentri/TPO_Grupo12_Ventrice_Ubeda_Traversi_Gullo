"""
-----------------------------------------------------------------------------------------------
Título:
Fecha: 8/10/2025
Autores: Santino Ventrice, Valentina Ubeda, Santino Traversi y Rocco Gullo

Descripción: Empresa de transporte que realiza viajes con sus vehículos y choferes.
Cada vehículo tiene como dato su costo por kilómetro. El único usuario del sistema será el que
gestiona los viajes en la empresa.

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import json
from funciones.archivos import *
from funciones.choferes import *
from funciones.vehiculos import *
from funciones.rutas import *
from funciones.informes import *

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    """
    # Precarga de datos de choferes
    choferes = {
        12507: {
            "activo": True,
            "nombre": "Carlos",
            "apellido": "Pérez",
            "telefono": 34567890,
            "cantidadKm": 25400,
            "turnos": {
                "turno1": "Lunes - Mañana",
                "turno2": "Miércoles - Mañana",
                "turno3": "Viernes - Mañana"
            }
        },
              
        12994: {
            "activo": True,
            "nombre": "Rocco",
            "apellido": "Morillo",
            "telefono": 26335567,
            "cantidadKm": 34500,
            "turnos": {
                "turno1": "Martes - Mañana",
                "turno2": "Jueves - Tarde",
                "turno3": "Viernes - Mañana"
            }
        },
        33051: {
            "activo": True,
            "nombre": "María",
            "apellido": "Gómez",
            "telefono": 23456789,
            "cantidadKm": 18750,
            "turnos": {
                "turno1": "Martes - Tarde",
                "turno2": "Jueves - Tarde",
                "turno3": "Sábado - Tarde"
            }
        },
        27713: {
            "activo": True,
            "nombre": "Jorge",
            "apellido": "López",
            "telefono": 45678901,
            "cantidadKm": 31000,
            "turnos": {
                "turno1": "Lunes - Noche",
                "turno2": "Miércoles - Noche",
                "turno3": "Viernes - Noche"
            }
        },
        44128: {
            "activo": False,
            "nombre": "Ana",
            "apellido": "Martínez",
            "telefono": 67890123,
            "cantidadKm": 9800,
            "turnos": {
                "turno1": "Martes - Tarde",
                "turno2": "Jueves - Tarde",
                "turno3": "Sábado - Tarde"
            }
        },
        56982: {
            "activo": True,
            "nombre": "Luis",
            "apellido": "Rodríguez",
            "telefono": 78901234,
            "cantidadKm": 42000,
            "turnos": {
                "turno1": "Lunes - Mañana",
                "turno2": "Martes - Mañana",
                "turno3": "Jueves - Mañana"
            }
        },
        61895: {
            "activo": True,
            "nombre": "Sofía",
            "apellido": "Fernández",
            "telefono": 89012345,
            "cantidadKm": 22100,
            "turnos": {
                "turno1": "Martes - Noche",
                "turno2": "Jueves - Noche",
                "turno3": "Sábado - Noche"
            }
        },
        78136: {
            "activo": False,
            "nombre": "Diego",
            "apellido": "Ruiz",
            "telefono": 90123456,
            "cantidadKm": 15000,
            "turnos": {
                "turno1": "Lunes - Tarde",
                "turno2": "Miércoles - Tarde",
                "turno3": "Viernes - Tarde"
            }
        },
        81306: {
            "activo": True,
            "nombre": "Elena",
            "apellido": "Silva",
            "telefono": 31234567,
            "cantidadKm": 30500,
            "turnos": {
                "turno1": "Martes - Mañana",
                "turno2": "Jueves - Mañana",
                "turno3": "Sábado - Mañana"
            }
        },
        96767: {
            "activo": True,
            "nombre": "Harry",
            "apellido": "Farias",
            "telefono": 34366785,
            "cantidadKm": 30500,
            "turnos": {
                "turno1": "Martes - Tarde",
                "turno2": "Lunes - Mañana",
                "turno3": "Sábado - Tarde"
            }
        }
    }
    """

    """
    # Precarga de datos de vehículos
    vehiculos = {
        "AE456GH": {
            "activo": False,
            "modelo": "Mercedes-Benz Sprinter",
            "añoCompra": 2022,
            "cantidadKm": 85200,
            "costoKm": 85.5,
            "infracciones": {
                "infraccion1": "Exceso de velocidad"
            }
        },
        "AC456FG": {
            "activo": True,
            "modelo": "Renault Master",
            "añoCompra": 2021,
            "cantidadKm": 112350,
            "costoKm": 91.0,
            "infracciones": {
                "infraccion1": "Mal estacionamiento",
                "infraccion2": "Cruce en rojo"
            }
        },
        "AD789HI": {
            "activo": False,
            "modelo": "Ford Transit",
            "añoCompra": 2019,
            "cantidadKm": 185000,
            "costoKm": 98.2,
            "infracciones": {}
        },
        "AE101JK": {
            "activo": True,
            "modelo": "Iveco Daily",
            "añoCompra": 2020,
            "cantidadKm": 145100,
            "costoKm": 105.5,
            "infracciones": {
                "infraccion1": "Exceso de velocidad"
            }
        },
        "AF212LM": {
            "activo": False,
            "modelo": "Citroën Jumper",
            "añoCompra": 2018,
            "cantidadKm": 210000,
            "costoKm": 88.8,
            "infracciones": {
                "infraccion1": "Falta de VTV",
                "infraccion2": "Uso de celular al conducir"
            }
        },
        "AA345NO": {
            "activo": True,
            "modelo": "Peugeot Boxer",
            "añoCompra": 2023,
            "cantidadKm": 45300,
            "costoKm": 93.3,
            "infracciones": {}
        },
        "AB678PQ": {
            "activo": True,
            "modelo": "Hyundai H100",
            "añoCompra": 2021,
            "cantidadKm": 95000,
            "costoKm": 83.0,
            "infracciones": {
                "infraccion1": "Giro en U prohibido"
            }
        },
        "AC901RS": {
            "activo": False,
            "modelo": "Kia K2500",
            "añoCompra": 2019,
            "cantidadKm": 195400,
            "costoKm": 99.1,
            "infracciones": {
                "infraccion1": "Exceso de velocidad",
                "infraccion2": "Mal estacionamiento",
                "infraccion3": "Circular sin luces"
            }
        },
        "AE452EV": {
            "activo": True,
            "modelo": "Volkswagen Crafter",
            "añoCompra": 2020,
            "cantidadKm": 134800,
            "costoKm": 94.7,
            "infracciones": {
                "infraccion1": "Exceso de velocidad"
                
             }
        },
        "AE432VX": {
            "activo": False,
            "modelo": "Fiat Ducato",
            "añoCompra": 2018,
            "cantidadKm": 207300,
            "costoKm": 87.9,
            "infracciones": {
                "infraccion1": "Circula sin luces"                
            }
        }
    }
    """

    """
    # Precarga de datos de rutas
    rutas = {
        "2025.10.21 06.45.00": {
            "idLegajo": "12507",      # Carlos Pérez
            "idPatente": "AA345NO",   # Peugeot Boxer
            "totalKm": 180,
            "costoRuta": 16794.0,
            "horaSalida": "2025.10.21 06.45",
            "horaLlegada": "2025.10.21 09.15"
        },
        "2025.10.22 14.00.00": {
            "idLegajo": "33051",      # María Gómez
            "idPatente": "AC456FG",   # Renault Master
            "totalKm": 220,
            "costoRuta": 20020.0,
            "horaSalida": "2025.10.22 14.00",
            "horaLlegada": "2025.10.22 18.30"
        },
        "2025.10.21 22.30.00": {
            "idLegajo": "27713",      # Jorge López
            "idPatente": "AE101JK",   # Iveco Daily
            "totalKm": 310,
            "costoRuta": 32705.0,
            "horaSalida": "2025.10.21 22.30",
            "horaLlegada": "2025.10.22 03.45"  # Cruce de medianoche
        },
        "2025.10.22 08.00.00": {
            "idLegajo": "81306",      # Elena Silva
            "idPatente": "AE456GH",   # Mercedes-Benz Sprinter
            "totalKm": 160,
            "costoRuta": 13680.0,
            "horaSalida": "2025.10.22 08.00",
            "horaLlegada": "2025.10.22 10.40"
        },
        "2025.10.24 19.00.00": {
            "idLegajo": "61895",      # Sofía Fernández
            "idPatente": "AB678PQ",   # Hyundai H100
            "totalKm": 195,
            "costoRuta": 16185.0,
            "horaSalida": "2025.10.24 19.00",
            "horaLlegada": "2025.10.24 23.10"
        },
        "2025.10.21 07.15.00": {
            "idLegajo": "56982",      # Luis Rodríguez
            "idPatente": "AA345NO",   # Peugeot Boxer
            "totalKm": 240,
            "costoRuta": 22392.0,
            "horaSalida": "2025.10.21 07.15",
            "horaLlegada": "2025.10.21 11.45"
        },
        "2025.10.23 22.30.00": {
            "idLegajo": "27713",      # Jorge López
            "idPatente": "AE101JK",   # Iveco Daily
            "totalKm": 275,
            "costoRuta": 29012.5,
            "horaSalida": "2025.10.23 22.30",
            "horaLlegada": "2025.10.24 02.20"  # Cruce de medianoche
        },
        "2025.10.24 14.00.00": {
            "idLegajo": "33051",      # María Gómez
            "idPatente": "AC456FG",   # Renault Master
            "totalKm": 190,
            "costoRuta": 17290.0,
            "horaSalida": "2025.10.24 14.00",
            "horaLlegada": "2025.10.24 18.00"
        },
        "2025.10.24 08.30.00": {
            "idLegajo": "81306",      # Elena Silva
            "idPatente": "AE452EV",    # Vehículo: Volkswagen Crafter
            "totalKm": 250,
            "costoRuta": 23675.0,     # 250 km * 94.7 $/km
            "horaSalida": "2025.10.24 08.30",
            "horaLlegada": "2025.10.24 13.15"
        },
        "2025.10.21 06.46.00": {
            "idLegajo": "96767",      # Harry Farias
            "idPatente": "AE432VX",   # Vehículo: Fiat Ducato
            "totalKm": 145,
            "costoRuta": 13528.5,
            "horaSalida": "2025.10.21 06.46",
            "horaLlegada": "2025.10.21 10.00"
        }
    }
    """
    
    # Rutas de archivos de los diccionarios
    rutaChoferes = "diccionarios/choferes.json"
    rutaVehiculos = "diccionarios/vehiculos.json"
    rutaRutas = "diccionarios/rutas.json"

    #-------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True:
        while True:
            opciones = 4
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL")
            print("---------------------------")
            print("[1] Gestión de choferes")
            print("[2] Gestión de vehículos")
            print("[3] Gestión de rutas")
            print("[4] Informes")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            
            opcionSubmenu = ""
            opcionMenuPrincipal = input("Seleccione una opción: ")
            if opcionMenuPrincipal in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcionMenuPrincipal == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcionMenuPrincipal == "1":   # Opción 1 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE CHOFERES")
                    print("---------------------------------")
                    print("[1] Ingresar choferes")
                    print("[2] Modificar choferes")
                    print("[3] Eliminar choferes")
                    print("[4] Listado choferes")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    print("------------------------------------")
                    print("MENÚ DE CHOFERES > Ingresar choferes")
                    print("------------------------------------\n")

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
                        legajo = crearLegajo(choferes)

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

                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    print("----------------------------------------")
                    print("MENÚ DE CHOFERES > Modificar de choferes")
                    print("----------------------------------------\n")

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
                            nuevoNombre = solicitarNombre("nombre")

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
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    print("------------------------------------")
                    print("MENÚ DE CHOFERES > Desactivar choferes")
                    print("------------------------------------\n")

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
                            
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    listarChoferes()

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        elif opcionMenuPrincipal == "2":   # Opción 2 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE VEHÍCULOS")
                    print("---------------------------")
                    print("[1] Ingresar vehículos")
                    print("[2] Modificar vehículos")
                    print("[3] Desactivar vehículos")
                    print("[4] Listado vehículos")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()


                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                        print("--------------------------------------")
                        print("MENÚ DE VEHÍCULOS > Agregar vehículos")
                        print("--------------------------------------\n")
                        
                        # Cargar datos de vehículos
                        archivo = abrirArchivo(rutaVehiculos, "r")
                        if archivo is not None:
                            vehiculos = json.load(archivo)
                            cerrarArchivo(archivo)
                        else:
                            vehiculos = {}
                        
                        # Solicitar patente
                        patente = solicitarPatente(vehiculos)
                       
                        #modelo del vehiculo 
                        modelo = input("Ingrese el modelo del vehiculo: ")
                        
                        #Agregar y validar año de compra 
                        añoCompra = solicitarAñoCompra()

                        #Agregar y validar cantidad de Km
                        cantidadKm = solicitarKm()

                        #Agregar y modificar costo de Km
                        costoKm = solicitarCostoKm()

                        vehiculos[patente] = {
                            "activo": True,  # Siempre TRUE al cargar
                            "modelo": modelo,
                            "añoCompra": añoCompra,
                            "cantidadKm": cantidadKm,
                            "costoKm": costoKm,
                            "infracciones": {}  # VACÍO AL INICIO
                        }

                        # Guardar vehículo en archivo
                        archivo = abrirArchivo(rutaVehiculos, "w")
                        if archivo is not None:
                            json.dump(vehiculos, archivo, indent=4, ensure_ascii=False)
                            cerrarArchivo(archivo)
                            print("Se ingresó el vehículo correctamente!")
                        else:
                            print("Se ingresó el vehículo en memoria pero no se pudo guardar en el archivo.")
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    print("--------------------------------------")
                    print("MENÚ DE VEHÍCULOS > Modificar vehículos")
                    print("--------------------------------------\n")
                    
                    # Cargar datos actuales de vehiculos desde archivo antes de modificar
                    archivo = abrirArchivo(rutaVehiculos, "r")
                    if archivo is not None:
                        vehiculos = json.load(archivo)
                        cerrarArchivo(archivo)
                    else:
                        vehiculos = {}

                    patente = input("Ingrese la patente del vehiculo a modificar: ").upper()

                    if patente not in vehiculos:
                        print("Error: la patente no se encuentra registrada")
                    else:
                        vehiculo = vehiculos[patente]

                        print("Datos actuales del vehiculo: ")
                        for campo, valor in vehiculo.items():
                            if campo != "infracciones":
                                print(f"  {campo}: {valor}")

                        print()
                        print("¿Que datos deseas modificar?")
                        print("1. Patente")
                        print("2. Modelo")
                        print("3. Año de compra")
                        print("4. Kilometro")
                        print("5. Costo por Km")
                        print("6. Infracciones")
                        opcionMod = input("Seleccione una opcion: ")

                        guardado = False

                        if opcionMod == "1":
                            nuevaPatenteValida = False
                            while not nuevaPatenteValida:
                                nuevaPatente = input("Ingrese la nueva patente: ").upper()
                                nuevaPatenteValida = validarPatente(nuevaPatente, vehiculos)

                            # reasignar y eliminar la entrada antigua
                            vehiculos[nuevaPatente] = vehiculo
                            del vehiculos[patente]
                            guardado = True
                            print("Patente modificada correctamente")

                        elif opcionMod == "2":
                            # Modificar modelo
                            nuevoModelo = input("Ingrese el nuevo modelo: ")
                            vehiculo["modelo"] = nuevoModelo
                            guardado = True
                            print("Modelo modificado correctamente.")

                        elif opcionMod == "3":
                            # Modificar año de compra
                            nuevoAño = solicitarAñoCompra()
                            vehiculo["añoCompra"] = int(nuevoAño)
                            guardado = True
                            print("Año de compra modificado correctamente")

                        elif opcionMod == "4":
                            # Modificar cantidad de Km
                            nuevoKm = solicitarKm()
                            vehiculo["cantidadKm"] = nuevoKm
                            guardado = True
                            print("Cantidad de Km modificado correctamente")
                            
                        elif opcionMod == "5":
                            # Modificar costo por Km 
                            nuevoCosto = solicitarCostoKm()
                            vehiculo["costoKm"] = nuevoCosto
                            guardado = True
                            print ("Costo del Km actualizado")
                        
                        elif opcionMod == "6":
                            print("\n------ MODIFICAR INFRACCIONES ------")
                            print("1. Agregar infracción")
                            print("2. Eliminar infracción")
                            print("3. Ver infracciones actuales")

                            opcionInf = input("Seleccione una opción: ")

                            if opcionInf == "1":
                                descripcion = input("Ingrese la descripción de la infracción: ")
                                agregarInfraccion(vehiculo, descripcion)
                                guardado = True

                            elif opcionInf == "2":
                                mostrarInfracciones(vehiculo)
                                claveEliminar = input("Ingrese el nombre exacto de la infracción a eliminar (ej: infraccion1): ")
                                eliminarInfraccion(vehiculo, claveEliminar)
                                guardado = True

                            elif opcionInf == "3":
                                mostrarInfracciones(vehiculo)

                            else:
                                print("Opción inválida en el menú de infracciones.")
                                                        
                        else:
                            print("Opcion invalida.")

                        # Si hubo cambios, guardar el diccionario completo en el archivo JSON
                        if guardado:
                            archivo = abrirArchivo(rutaVehiculos, "w")
                            if archivo is not None:
                                json.dump(vehiculos, archivo, indent=4, ensure_ascii=False)
                                cerrarArchivo(archivo)
                                print("Cambios guardados en el archivo de vehículos.")
                            else:
                                print("No se pudo guardar los cambios en el archivo.")
                                        
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    print("--------------------------------------")
                    print("MENÚ DE VEHÍCULOS > Desactivar vehículos")
                    print("--------------------------------------\n")

                    # Cargar datos de vehículos
                    archivo = abrirArchivo(rutaVehiculos, "r")
                    if archivo is not None:
                        vehiculos = json.load(archivo)
                        cerrarArchivo(archivo)
                    else:
                        vehiculos = {}

                    patente = input("Ingrese la patente del vehiculo a desactivar: ").upper()
                    if patente not in vehiculos:
                        print("No existe un vehículo con esa patente.")
                    else:
                        if not vehiculos[patente]["activo"]:
                            print("Ese vehículo ya está inactivo.")
                        else:
                            confirm = input(f"¿Deseas desactivar el vehículo {patente}? (si/no): ").upper()
                            if confirm == "SI":
                                vehiculos[patente]["activo"] = False
                                
                                # Guardar cambios en archivo
                                archivo = abrirArchivo(rutaVehiculos, "w")
                                if archivo is not None:
                                    json.dump(vehiculos, archivo, indent=4, ensure_ascii=False)
                                    cerrarArchivo(archivo)
                                    print("Vehículo desactivado con éxito.")
                                else:
                                    print("No se pudo guardar los cambios.")
                            else:
                                print("Operación cancelada.")

                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    print("--------------------------------------")
                    print("MENÚ DE VEHÍCULOS > Listar vehículos")
                    print("--------------------------------------\n")

                    # Cargar datos actualizados de vehículos antes de listar
                    archivo = abrirArchivo(rutaVehiculos, "r")
                    if archivo is not None:
                        vehiculos = json.load(archivo)
                        cerrarArchivo(archivo)
                    else:
                        vehiculos = {}
                    listarVehiculos(vehiculos)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")
        
        elif opcionMenuPrincipal == "3":   # Opción 3 del menú principal
            while True:
                while True:
                    opciones = 1
                    print()
                    print("------------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE RUTAS")
                    print("------------------------------")
                    print("[1] Registro de rutas")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú

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

                        # Si el número ingresado es 0, se sale del bucle
                        if legajo == "0":
                            print("Saliendo de la modificación de choferes.\n")
                        elif not legajo.isdigit() or legajo not in choferes or not choferes[legajo]["activo"]:
                            print("Legajo inválido. Intente nuevamente.")
                        else:
                            break

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

                        # Convertir fechas al formato YYYY.MM.DD HH.MM
                        # Para la hora de salida
                        partes_salida = fechaSalida.split()
                        fecha_salida = partes_salida[0]  # Ya está en formato YYYY.MM.DD
                        hora_salida = ".".join(partes_salida[1].split(".")[:2])  # Solo tomamos hora y minutos
                        horaSalida = f"{fecha_salida} {hora_salida}"

                        # Para la hora de llegada
                        partes_llegada = fechaLlegada.split()
                        fecha_llegada = partes_llegada[0]  # Ya está en formato YYYY.MM.DD
                        hora_llegada = ".".join(partes_llegada[1].split(".")[:2])  # Solo tomamos hora y minutos
                        horaLlegada = f"{fecha_llegada} {hora_llegada}"

                        # Guardar ruta
                        rutas[fechaHora] = {
                            "idLegajo": legajo,
                            "idPatente": patente,
                            "totalKm": totalKm,
                            "costoRuta": costoRuta,
                            "horaSalida": horaSalida,
                            "horaLlegada": horaLlegada
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

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")
        
        elif opcionMenuPrincipal == "4":   # Opción 4 del menú principal
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

            while True:
                while True:
                    opciones = 5
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE INFORMES")
                    print("---------------------------")
                    print("[1] Informe viajes del mes")
                    print("[2] Resumen mensual de rutas por vehículo")
                    print("[3] Resumen mensual de rutas por vehículos")
                    print("[4] Ranking choferes")
                    print("[5] Ranking vehículos")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    informeViajesDelMes(rutas, vehiculos)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    patenteBuscar = input("Ingrese la patente del vehículo: ").upper()
                    informeResumenMensualKmVehiculo(patenteBuscar, rutas, vehiculos)

                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    informeResumenMensualCostosVehiculos(rutas, vehiculos)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    informeRankingChoferes(choferes, rutas)

                elif opcionSubmenu == "5":   # Opción 4 del submenú
                    informeRankingVehiculos(vehiculos, rutas)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")

# Punto de entrada al programa
main()