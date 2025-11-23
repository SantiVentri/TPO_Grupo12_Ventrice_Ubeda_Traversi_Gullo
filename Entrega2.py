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

                    registrarChofer()

                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    print("----------------------------------------")
                    print("MENÚ DE CHOFERES > Modificar de choferes")
                    print("----------------------------------------\n")

                    modificarChofer()
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    print("------------------------------------")
                    print("MENÚ DE CHOFERES > Desactivar choferes")
                    print("------------------------------------\n")

                    desactivarChofer()
                            
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    print("--------------------------------------")
                    print("MENÚ DE CHOFERES > Listado de choferes")
                    print("--------------------------------------\n")

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
                    print("MENÚ DE VEHÍCULOS > Ingresar vehículos")
                    print("--------------------------------------\n")

                    ingresarVehiculo()
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    print("--------------------------------------")
                    print("MENÚ DE VEHÍCULOS > Modificar vehículos")
                    print("--------------------------------------\n")

                    modificarVehiculo()
                                        
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    print("--------------------------------------")
                    print("MENÚ DE VEHÍCULOS > Desactivar vehículos")
                    print("--------------------------------------\n")

                    desactivarVehiculo()

                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    print("--------------------------------------")
                    print("MENÚ DE VEHÍCULOS > Listar vehículos")
                    print("--------------------------------------\n")

                    listarVehiculos()

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
                    print("--------------------------------")
                    print("MENÚ DE RUTAS > Registro de rutas")
                    print("--------------------------------\n")
                    
                    registrarRuta()

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")
        
        elif opcionMenuPrincipal == "4":   # Opción 4 del menú principal
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
                    print("-----------------------------------")
                    print("MENÚ DE INFORMES > Informe viajes del mes")
                    print("-----------------------------------\n")

                    informeViajesDelMes()
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    print("-----------------------------------")
                    print("MENÚ DE INFORMES > Informe resumen mensual de rutas por vehículo")
                    print("-----------------------------------\n")

                    informeResumenMensualKmVehiculo()

                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    print("-----------------------------------")
                    print("MENÚ DE INFORMES > Informe resumen mensual de costos por vehículo")
                    print("-----------------------------------\n")

                    informeResumenMensualCostosVehiculos()
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    print("-----------------------------------")
                    print("MENÚ DE INFORMES > Informe ranking de choferes")
                    print("-----------------------------------\n")

                    informeRankingChoferes()

                elif opcionSubmenu == "5":   # Opción 4 del submenú
                    print("-----------------------------------")
                    print("MENÚ DE INFORMES > Informe ranking de vehículos")
                    print("-----------------------------------\n")

                    informeRankingVehiculos()

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")

# Punto de entrada al programa
main()