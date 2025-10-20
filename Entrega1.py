"""
-----------------------------------------------------------------------------------------------
Título:
Fecha: 8/10/2025
Autores: Santino Ventrice, Valentina Ubeda, Santino Traversi y Rocco Gullo

Descripción: Empresa de transporte que realiza viajes con sus vehículos y choferes.
Cada vehículo tiene como dato su costo por kilómetro. El único usuario del sistema será el que
gestiona los viajes en la empresa.

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
...


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    choferes = {
        12507: {
            "activo": True,
            "nombre": "Carlos",
            "apellido": "Pérez",
            "telefono": 34567890,
            "cantidadKm": 25400,
            "turnos": {
                "turno1": "Mañana - Lunes",
                "turno2": "Mañana - Miércoles",
                "turno3": "Mañana - Viernes"
            }
        },
        33051: {
            "activo": True,
            "nombre": "María",
            "apellido": "Gómez",
            "telefono": 23456789,
            "cantidadKm": 18750,
            "turnos": {
                "turno1": "Tarde - Martes",
                "turno2": "Tarde - Jueves",
                "turno3": "Tarde - Sábado"
            }
        },
        27713: {
            "activo": True,
            "nombre": "Jorge",
            "apellido": "López",
            "telefono": 45678901,
            "cantidadKm": 31000,
            "turnos": {
                "turno1": "Noche - Lunes",
                "turno2": "Noche - Miércoles",
                "turno3": "Noche - Viernes"
            }
        },
        44128: {
            "activo": False,
            "nombre": "Ana",
            "apellido": "Martínez",
            "telefono": 67890123,
            "cantidadKm": 9800,
            "turnos": {
                "turno1": "Tarde - Martes",
                "turno2": "Tarde - Jueves",
                "turno3": "Tarde - Sábado"
            }
        },
        56982: {
            "activo": True,
            "nombre": "Luis",
            "apellido": "Rodríguez",
            "telefono": 78901234,
            "cantidadKm": 42000,
            "turnos": {
                "turno1": "Mañana - Lunes",
                "turno2": "Mañana - Martes",
                "turno3": "Mañana - Jueves"
            }
        },
        61895: {
            "activo": True,
            "nombre": "Sofía",
            "apellido": "Fernández",
            "telefono": 89012345,
            "cantidadKm": 22100,
            "turnos": {
                "turno1": "Noche - Martes",
                "turno2": "Noche - Jueves",
                "turno3": "Noche - Sábado"
            }
        },
        78136: {
            "activo": False,
            "nombre": "Diego",
            "apellido": "Ruiz",
            "telefono": 90123456,
            "cantidadKm": 15000,
            "turnos": {
                "turno1": "Tarde - Lunes",
                "turno2": "Tarde - Miércoles",
                "turno3": "Tarde - Viernes"
            }
        },
        81306: {
            "activo": True,
            "nombre": "Elena",
            "apellido": "Silva",
            "telefono": 31234567,
            "cantidadKm": 30500,
            "turnos": {
                "turno1": "Mañana - Martes",
                "turno2": "Mañana - Jueves",
                "turno3": "Mañana - Sábado"
            }
        }
    }

    vehiculos = {
        "AE456GH": {
            "activo": True,
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
        }
    }

    rutas = {
        "RN001": {
            "idLegajo": "12507",      # Carlos Pérez
            "idPatente": "AA345NO",   # Peugeot Boxer
            "totalKm": 180,
            "costoRuta": 16794.0,
            "horaSalida": "2025-10-14 06:45",
            "horaLlegada": "2025-10-14 09:15"
        },
        "RN002": {
            "idLegajo": "33051",      # María Gómez
            "idPatente": "AC456FG",   # Renault Master
            "totalKm": 220,
            "costoRuta": 20020.0,
            "horaSalida": "2025-10-14 14:00",
            "horaLlegada": "2025-10-14 18:30"
        },
        "RN003": {
            "idLegajo": "27713",      # Jorge López
            "idPatente": "AE101JK",   # Iveco Daily
            "totalKm": 310,
            "costoRuta": 32705.0,
            "horaSalida": "2025-10-13 22:30",
            "horaLlegada": "2025-10-14 03:45"  # Cruce de medianoche
        },
        "RN004": {
            "idLegajo": "81306",      # Elena Silva
            "idPatente": "AE456GH",   # Mercedes-Benz Sprinter
            "totalKm": 160,
            "costoRuta": 13680.0,
            "horaSalida": "2025-10-12 08:00",
            "horaLlegada": "2025-10-12 10:40"
        },
        "RN005": {
            "idLegajo": "61895",      # Sofía Fernández
            "idPatente": "AB678PQ",   # Hyundai H100
            "totalKm": 195,
            "costoRuta": 16185.0,
            "horaSalida": "2025-10-12 19:00",
            "horaLlegada": "2025-10-12 23:10"
        },
        "RN006": {
            "idLegajo": "56982",      # Luis Rodríguez
            "idPatente": "AA345NO",   # Peugeot Boxer
            "totalKm": 240,
            "costoRuta": 22392.0,
            "horaSalida": "2025-10-11 07:15",
            "horaLlegada": "2025-10-11 11:45"
        },
        "RN007": {
            "idLegajo": "27713",      # Jorge López
            "idPatente": "AE101JK",   # Iveco Daily
            "totalKm": 275,
            "costoRuta": 29012.5,
            "horaSalida": "2025-10-10 21:30",
            "horaLlegada": "2025-10-11 02:20"  # Cruce de medianoche
        },
        "RN008": {
            "idLegajo": "33051",      # María Gómez
            "idPatente": "AC456FG",   # Renault Master
            "totalKm": 190,
            "costoRuta": 17290.0,
            "horaSalida": "2025-10-09 15:00",
            "horaLlegada": "2025-10-09 19:00"
        }
    }

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
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE CHOFERES")
                    print("---------------------------")
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
                    ...
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    ...
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    ...
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    ...

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
                    print("[3] Eliminar vehículos")
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
                        print("---------AGREGAR VEHICULO----------")
                        patente = input("Ingrese la patente del vehículo (ej. AE456GH): ").upper()
                        if patente in vehiculos:
                            print("Ya existe un vehículo con esa patente.")
                        else: 
                            modelo = input("Ingrese el modelo del vehiculo: ")
                        
                        añoCompra = input("Ingrese año de compra: ")
                        while not añoCompra.isdigit():#Validar año de compra 
                            print("Error: el año debe ser numérico.")
                            añoCompra = input("Ingrese año de compra: ")
                        añoCompra = int(añoCompra)

                        cantidadKm = input("Ingrese cantidad de km actuales: ")
                        while not cantidadKm.replace(".", "", 1).isdigit(): #validar cantidad de Km
                            print("Error: el valor debe ser numérico.")
                            cantidadKm = input("Ingrese cantidad de km actuales: ")
                        cantidadKm = float(cantidadKm)

                        costoKm = input("Ingrese costo por km: ")
                        while not costoKm.replace(".", "", 1).isdigit(): #validamos el costo por kilometro 
                            print("Error: el valor debe ser numérico.")
                            costoKm = input("Ingrese costo por km: ")
                        costoKm = float(costoKm)

                        vehiculos[patente] = {
                            "activo": True,  # SIEMPRE TRUE al cargar
                            "modelo": modelo,
                            "añoCompra": añoCompra,
                            "cantidadKm": cantidadKm,
                            "costoKm": costoKm,
                            "infracciones": {}  # VACÍO AL INICIO
                        }

                        print("Se ingreso el vehiculo correctamente! ")

                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    print("----------MODIFICAR VEHICULOS----------")
                    patente = input("Ingrese la patente del vehiculo a modificar: ").upper()

                    if patente not in vehiculos:
                        print("Error la patente no se encuentra registrada") 
                    else: 
                        vehiculo = vehiculos[patente]
                        print("Datos actuales del vehiculo: ")
                        for campo, valor in vehiculo.items():
                         if campo != "infracciones":
                            print(f"  {campo}: {valor}")
                        
                        print("¿Que datos deseas modificar?")
                        print("1.Modelo")
                        print("2. Año de compra")
                        print("3. Kilometraje")
                        print("4. Costo por Km")
                        opcionMod = input("Seleccione una opcion: ")
                        if opcionMod == "1":
                            vehiculo["modelo"] = input("Nuevo modelo: ")
                        elif opcionMod == "2":
                            vehiculo["añoCompra"]= int(input("Nuevo año de compra: "))
                        elif opcionMod == "3":
                            vehiculo[cantidadKm]= float(input("Nueva cantidad de Km: "))
                        elif opcionMod == "4": 
                            vehiculo[costoKm]= float(input("Nuevo costo de Km: "))
                        else:
                            print("Opcion invalida.")
                        print("Vehiculo modificado correctamente!") 

                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    print("----------ELIMINAR VEHICULO---------")
                    patente = input("Ingrese la pantente del vehiculo a eliminar: ").upper()

                    if patente not in vehiculos:
                        print("No existe un vehiculo con esa patente.")
                    else: 
                        confirm = input(f"¿Estas seguro que deseas eliminar el vehiculo {patente} (si/no): ?").upper()
                        if confirm == "SI":
                            del vehiculos[patente]
                            print("Vehiculo eliminado con exito!")
                        else:        
                            print("Operacion cancelada.")

                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    print("----------LISTA DE VEHICULOS----------")
                    if len(vehiculos) == 0:
                        print("No hay vehiculos cargados.")
                    else: 
                        for patente, datos in vehiculos.items():
                             print(f"\nPatente: {patente}")
                             print(f"  Activo     : {datos['activo']}")
                             print(f"  Modelo     : {datos['modelo']}")
                             print(f"  Año compra : {datos['añoCompra']}")
                             print(f"  Km totales : {datos['cantidadKm']}")
                             print(f"  Costo x Km : {datos['costoKm']}")
                             print(f"  Infracciones: {len(datos['infracciones'])} registradas")

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")
        
        elif opcionMenuPrincipal == "3":   # Opción 3 del menú principal
            while True:
                while True:
                    opciones = 1
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE RUTAS")
                    print("---------------------------")
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
                    ...

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
                    ...
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    ...
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    ...
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    ...

                elif opcionSubmenu == "5":   # Opción 4 del submenú
                    ...

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")


# Punto de entrada al programa
main()