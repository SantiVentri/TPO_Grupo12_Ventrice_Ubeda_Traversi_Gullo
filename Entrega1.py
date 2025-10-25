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
from funciones.def_choferes import *
from funciones.def_vehiculos import *
from funciones.def_rutas import *
from funciones.def_informes import *

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
        "AD654TU": {
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

    rutas = {
        "2025.10.21 06.45.00": {
            "idLegajo": "12507",      # Carlos Pérez
            "idPatente": "AA345NO",   # Peugeot Boxer
            "totalKm": 180,
            "costoRuta": 16794.0,
            "horaSalida": "2025-10-21 06:45",
            "horaLlegada": "2025-10-21 09:15"
        },
        "2025.10.22 14.00.00": {
            "idLegajo": "33051",      # María Gómez
            "idPatente": "AC456FG",   # Renault Master
            "totalKm": 220,
            "costoRuta": 20020.0,
            "horaSalida": "2025-10-22 14:00",
            "horaLlegada": "2025-10-22 18:30"
        },
        "2025.10.21 22.30.00": {
            "idLegajo": "27713",      # Jorge López
            "idPatente": "AE101JK",   # Iveco Daily
            "totalKm": 310,
            "costoRuta": 32705.0,
            "horaSalida": "2025-10-21 22:30",
            "horaLlegada": "2025-10-22 03:45"  # Cruce de medianoche
        },
        "2025.10.22 08.00.00": {
            "idLegajo": "81306",      # Elena Silva
            "idPatente": "AE456GH",   # Mercedes-Benz Sprinter
            "totalKm": 160,
            "costoRuta": 13680.0,
            "horaSalida": "2025-10-22 08:00",
            "horaLlegada": "2025-10-22 10:40"
        },
        "2025.10.24 19.00.00": {
            "idLegajo": "61895",      # Sofía Fernández
            "idPatente": "AB678PQ",   # Hyundai H100
            "totalKm": 195,
            "costoRuta": 16185.0,
            "horaSalida": "2025-10-24 19:00",
            "horaLlegada": "2025-10-24 23:10"
        },
        "2025.10.21 07.15.00": {
            "idLegajo": "56982",      # Luis Rodríguez
            "idPatente": "AA345NO",   # Peugeot Boxer
            "totalKm": 240,
            "costoRuta": 22392.0,
            "horaSalida": "2025-10-21 07:15",
            "horaLlegada": "2025-10-21 11:45"
        },
        "2025.10.23 22.30.00": {
            "idLegajo": "27713",      # Jorge López
            "idPatente": "AE101JK",   # Iveco Daily
            "totalKm": 275,
            "costoRuta": 29012.5,
            "horaSalida": "2025-10-23 22:30",
            "horaLlegada": "2025-10-24 02:20"  # Cruce de medianoche
        },
        "2025.10.24 14.00.00": {
            "idLegajo": "33051",      # María Gómez
            "idPatente": "AC456FG",   # Renault Master
            "totalKm": 190,
            "costoRuta": 17290.0,
            "horaSalida": "2025-10-24 14:00",
            "horaLlegada": "2025-10-24 18:00"
        },
        "2025.10.24 08.30.00": {
            "idLegajo": "81306",      # Elena Silva
            "idPatente": "D654TU",    # Vehículo: Volkswagen Crafter
            "totalKm": 250,
            "costoRuta": 26375.0,
            "horaSalida": "2025-10-24 08:30",
            "horaLlegada": "2025-10-24 13:15"
        },
        "2025.10.21 06.45.00": {
            "idLegajo": "96767",      # Harry Farias
            "idPatente": "AE432VX",   # Vehículo: Fiat Ducato
            "totalKm": 145,
            "costoRuta": 13528.5,
            "horaSalida": "2025-10-21 06:45",
            "horaLlegada": "2025-10-21 10:00"
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
                        # Crear legajo
                        legajo = crearLegajo(choferes)
                        
                        # Solicitar nombre
                        nombreValido = False
                        while not nombreValido:
                            nombre = input("Ingrese el primer nombre del chofer: ")
                            nombreValido = validarNombreApellido("nombre", nombre)

                        # Solicitar apellido
                        apellidoValido = False
                        while not apellidoValido:
                            apellido = input("Ingrese el apellido del chofer: ")
                            apellidoValido = validarNombreApellido("apellido", apellido)

                        # Solicitar teléfono
                        telValido = False
                        while not telValido:
                            telefono = input("Ingrese el teléfono del chofer: +54 11 ")
                            telValido = validarTelefono(telefono)

                        # Solicitar cantidad de km recorridos
                        kmValidos = False
                        while not kmValidos:
                            cantidadKm = input("Ingrese la cantidad de km recorridos por el chofer (Presione Enter para 0): ")
                            if cantidadKm.strip() == "":
                                cantidadKm = "0"
                            kmValidos = validarKm(cantidadKm)

                        # Agregar turnos
                        turnos = {}
                        for i in range(3):
                            turnoValido = False
                            while not turnoValido:
                                # Ingresar nuevo día
                                diaTurno = input(f"Ingrese el día para el turno {i+1} (Lunes, Martes, etc.) o '-' para dejarlo vacío: ")
                                
                                if diaTurno == "-":
                                    print(f"Turno {i+1} quedará vacío.")
                                    turnoValido = True
                                else:
                                    # Ingresar nuevo horario
                                    horarioTurno = input("Ingrese el horario (Mañana, Tarde o Noche): ")
                                    
                                    # Crear y validar el turno
                                    nuevoTurno = f"{diaTurno.title()} - {horarioTurno.title()}"
                                    turnoValido = validarTurno(turnos, nuevoTurno)
                                    
                                    if turnoValido:
                                        # Guardar turno válido
                                        turnos[f"turno{i+1}"] = nuevoTurno
                                        print(f"Turno {nuevoTurno} agregado exitosamente.")

                        # Guardar chofer
                        choferes[legajo] = {
                            "activo": True,
                            "nombre": nombre,
                            "apellido": apellido,
                            "telefono": telefono,
                            "cantidadKm": float(cantidadKm),
                            "turnos": turnos
                        }

                        print(f"\nSe agregó al chofer {nombre} {apellido}, LU{legajo} exitosamente.\n")

                        # Preguntar si desea agregar otro chofer
                        agregarOtro = input("¿Desea agregar otro chofer? (s/n): ").lower()
                        if agregarOtro != "s" and agregarOtro != "si":
                            break
                        
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    print("----------------------------------------")
                    print("MENÚ DE CHOFERES > Modificar de choferes")
                    print("----------------------------------------\n")

                    while True:
                        # Preguntar legajo de chofer a modificar
                        legajo = input("Ingrese el legajo del chofer a modificar (o '0' para salir): ")

                        # Si el número ingresado es 0, se sale del bucle
                        if legajo == "0":
                            print("Saliendo de la modificación de choferes.\n")
                            break
                        elif not legajo.isdigit() or int(legajo) not in choferes:
                            print("Legajo inválido. Intente nuevamente.")
                            break

                        # Formatear celda de teléfono
                        telefonoFormateado = str(choferes[int(legajo)]['telefono'])[4:] + "-" + str(choferes[int(legajo)]['telefono'])[:4]

                        # Seleccionar dato a modificar
                        print("\nDatos actuales del chofer:")
                        print(f"1. Nombre: {choferes[int(legajo)]['nombre']}")
                        print(f"2. Apellido: {choferes[int(legajo)]['apellido']}")
                        print(f"3. Teléfono: +54 11 {telefonoFormateado}")
                        print(f"4. Cantidad de km: {choferes[int(legajo)]['cantidadKm']}")
                        print(f"5. Ver turnos")
                        print("\n¿Qué dato desea modificar?")
                        
                        opcion = input("Ingrese el número de la opción (1-5): ")
                        
                        if opcion == "1":
                            # Ingresar nuevo nombre
                            nombreValido = False
                            while not nombreValido:
                                nombre = input("Ingrese el primer nombre del chofer: ")

                                # Formatear nombre (primera letra mayúscula, resto minúsculas)
                                nombre = formatearNombreApellido(nombre)

                                # Validar nombre
                                nombreValido = validarNombreApellido("nombre", nombre)

                            # Guardar nuevo nombre
                            choferes[int(legajo)]['nombre'] = nombre

                            print("\nDato modificado exitosamente.")
                            
                        elif opcion == "2":
                            # Ingresar nuevo apellido
                            apellidoValido = False
                            while not apellidoValido:
                                apellido = input("Ingrese el apellido del chofer: ")

                                # Formatear apellido (primera letra mayúscula, resto minúsculas)
                                apellido = formatearNombreApellido(apellido)
                                
                                # Validar apellido
                                apellidoValido = validarNombreApellido("apellido", apellido)

                            # Guardar nuevo apellido
                            choferes[int(legajo)]['apellido'] = apellido

                            print("\nDato modificado exitosamente.")

                        elif opcion == "3":
                            # Solicitar teléfono
                            telValido = False
                            while not telValido:
                                telefono = input("Ingrese el teléfono del chofer: +54 11 ")
                                telValido = validarTelefono(telefono)

                            # Guardar nuevo teléfono
                            choferes[int(legajo)]['telefono'] = telefono

                            print("\nDato modificado exitosamente.")

                        elif opcion == "4":
                            # Ingresar nueva cantidad de km recorridos
                            kmValidos = False
                            while not kmValidos:
                                cantidadKm = input("Ingrese el cantidad de km recorridos del chofer: ")
                                kmValidos = validarKm(cantidadKm)

                            # Guardar nueva cantidad de km
                            choferes[int(legajo)]['cantidadKm'] = float(cantidadKm)

                            print("\nDato modificado exitosamente.")
                                    
                        elif opcion == "5":
                            # Ver turnos
                            print("\nTurnos actuales del chofer:")
                            for i in range(1, 4):
                                if f"turno{i}" in choferes[int(legajo)]['turnos']:
                                    print(f"{i}. {choferes[int(legajo)]['turnos'][f'turno{i}']}")
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
                                turnoValido = False
                                while not turnoValido:
                                    # Ingresar nuevo día
                                    nuevoDia = input("Ingrese el nuevo día del turno (Lunes a Viernes) o '-' para dejar vacío: ")

                                    if nuevoDia == "-":
                                        # Eliminar el turno
                                        if f'turno{turnoModificar}' in choferes[int(legajo)]['turnos']:
                                            del choferes[int(legajo)]['turnos'][f'turno{turnoModificar}']
                                        print("Turno eliminado exitosamente.")
                                        turnoValido = True
                                    else:
                                        # Ingresar nuevo horario
                                        nuevoHorario = input("Ingrese el nuevo horario del turno (Mañana, Tarde o Noche): ")

                                        # Validar turno
                                        nuevoTurno = f"{nuevoDia} - {nuevoHorario}"
                                        turnoValido = validarTurno(choferes[int(legajo)]["turnos"].values(), nuevoTurno)

                                        if turnoValido:
                                            # Guardar nuevo turno
                                            choferes[int(legajo)]['turnos'][f'turno{turnoModificar}'] = nuevoTurno

                                            # Mensaje de éxito
                                            print(f"Turno del {nuevoDia} a la {nuevoHorario} modificado exitosamente.")

                        else:
                            print("Opción inválida.")
                            break
                            
                        # Preguntar si desea modificar otro chofer
                        modificarOtro = input("¿Desea modificar otro chofer? (s/n): ").lower()
                        if modificarOtro != "s" and modificarOtro != "si":
                            break
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    print("------------------------------------")
                    print("MENÚ DE CHOFERES > Desactivar choferes")
                    print("------------------------------------\n")

                    while True:
                        # Se pide el número de legajo a eliminar
                        legajo = input("Ingrese el legajo del chofer a desactivar (o '0' para salir): ")

                        # Si el número ingresado es 0, se sale del bucle
                        if legajo == "0":
                            break
                        # Validar legajo
                        elif not legajo.isdigit() or int(legajo) not in choferes:
                            print("Legajo inválido. Intente nuevamente.")
                        else:
                            legajo = int(legajo) # Convertir a entero
                            chofer = choferes[legajo] # Obtener datos del chofer

                            # Mensaje de confirmación
                            confirmar = input(f"¿Está seguro que desea desactivar al chofer {chofer['nombre']} {chofer['apellido']} (LU{legajo})? (s/n): ").lower()
                            
                            # Si el usuario confirma la acción, se desactiva el chofer. Sino, se cancela la operación
                            if confirmar == "s" or confirmar == "si":
                                choferes[legajo]["activo"] = False
                                print(f"Chofer LU{legajo} desactivado exitosamente.\n")
                            else:
                                print("Desactivación cancelada.\n")
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    listarChoferes(choferes)

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
                        patenteValida=False
                      
                        while not patenteValida:
                            patente = input("Ingrese la patente del vehículo (ej. AE456GH): ").upper()
                            patenteValida = validarPatente(patente, vehiculos)
                       
                        #modelo del vehiculo 
                        modelo = input("Ingrese el modelo del vehiculo: ")
                        
                        #Agregar y validar año de compra 
                       
                        añoValido = False
                        while not añoValido:
                            añoCompra = input("Ingrese el año de compra del vehículo: ")
                            añoValido = validarAñoCompra(añoCompra)

                        añoCompra = int(añoCompra)

                        #Agregar y validar cantidad de Km
                        kmValido = False
                        while not kmValido:
                            cantidadKm = input("Ingrese la cantidad de Km actuales: ")
                            kmValido = validarCantKm(cantidadKm)

                        cantidadKm = float(cantidadKm)
                         #Agregar y modificar costo de Km
                        costoValido = False
                        while not costoValido:
                            costoKm = input("Ingrese el costo por Km: ")
                            costoValido = validarCostoKm(costoKm)

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
                    print("--------------------------------------")
                    print("MENÚ DE VEHÍCULOS > Modificar vehículos")
                    print("--------------------------------------\n")
                    
                    patente = input("Ingrese la patente del vehiculo a modificar: ").upper()

                    if patente not in vehiculos:
                        print("Error la patente no se encuentra registrada") 
                    else: 
                        vehiculo = vehiculos[patente]

                        print("Datos actuales del vehiculo: ")
                        for campo, valor in vehiculo.items():
                         if campo != "infracciones":
                            print(f"  {campo}: {valor}")

                        print()
                        print("¿Que datos deseas modificar?")
                        print("1.Patente")
                        print("2. Modelo")
                        print("3. Año de compra")
                        print("4. Kilometro")
                        print("5. Costo por Km")
                        print("6. Infracciones")
                        opcionMod = input("Seleccione una opcion: ")

                        if opcionMod == "1":
                            nuevaPatenteValida = False
                            while not nuevaPatenteValida:
                                nuevaPatente= input("Ingrese la nueva patente: ").upper()
                                nuevaPatenteValida= validarPatente(nuevaPatente, vehiculos)
                            
                            vehiculos[nuevaPatente] = vehiculo
                            del vehiculos[patente]
                            print("Patente modificada corretamente")
                               

                        elif opcionMod == "2":
                            nuevoModelo = input("Ingrese el nuevo modelo: ")
                            vehiculo["modelo"] = nuevoModelo
                            print("Modelo modificado correctamente.")
                        
                        elif opcionMod == "3":
                            añoValido = False 
                            while not añoValido:
                                nuevoAño = input("Ingrese el nuevo año de compra: ")
                                añoValido = validarAñoCompra(nuevoAño)
                            vehiculo["añoCompra"] = int(nuevoAño)
                            print("Año de compra modificado correctamente")

                        elif opcionMod == "4":
                             kmValido = False 
                             while not kmValido:
                                 nuevoKm = input("Ingrese l nueva cantidad de Km actuales: ")
                                 kmValido = validarCantKm(nuevoKm)
                             vehiculo["cantidadKm"] = float(nuevoKm)
                             print("cantidad de Km modifcado correctamente")
                            
                        elif opcionMod == "5": 
                            costoValido = False 
                            while not costoValido:
                                nuevoCosto = input("Ingrese el nuevo costo del Km: ")
                                costoValido= validarCostoKm(nuevoCosto)
                            vehiculo["costoKm"] = float(nuevoCosto)
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

                            elif opcionInf == "2":
                                mostrarInfracciones(vehiculo)
                                claveEliminar = input("Ingrese el nombre exacto de la infracción a eliminar (ej: infraccion1): ")
                                eliminarInfraccion(vehiculo, claveEliminar)

                            elif opcionInf == "3":
                                mostrarInfracciones(vehiculo)

                            else:
                                print("Opción inválida en el menú de infracciones.")
                                                        
                        else:
                             print("Opcion invalida.")
                        
                                        
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    print("--------------------------------------")
                    print("MENÚ DE VEHÍCULOS > Desactivar vehículos")
                    print("--------------------------------------\n")

                    patente = input("Ingrese la pantente del vehiculo a desactivar: ").upper()
                    if patente not in vehiculos:
                         print("No existe un vehículo con esa patente.")
                    else:
                        if not vehiculos[patente]["activo"]:
                         print("Ese vehículo ya está inactivo.")
                        else:
                            confirm = input(f"¿Deseas desactivar el vehículo {patente}? (si/no): ").upper()
                        if confirm == "SI":
                            vehiculos[patente]["activo"] = False
                            print("Vehículo desactivado con éxito.")
                        else:
                            print("Operación cancelada.")

                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    print("--------------------------------------")
                    print("MENÚ DE VEHÍCULOS > Listar vehículos")
                    print("--------------------------------------\n")

                    if len(vehiculos) == 0:
                        print("No hay vehiculos cargados.")
                    
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
                        def fila_texto(fila):
                            print(" | " + " | ".join(str(fila[i]).ljust(anchos[i]) for i in range(len(fila))) + " |")
                        
                        #Imprimir la tabla completa

                        linea()
                        fila_texto(encabezado)
                        linea()
                        for f in tabla:
                            fila_texto(f)
                        linea()
                    print("\n")

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
                    # Ingresar legajo
                    while True:
                        legajo = input("Ingrese el legajo del chofer (o '0' para salir): ")

                        # Si el número ingresado es 0, se sale del bucle
                        if legajo == "0":
                            print("Saliendo de la modificación de choferes.\n")
                        elif not legajo.isdigit() or int(legajo) not in choferes or not choferes[int(legajo)]["activo"]:
                            print("Legajo inválido. Intente nuevamente.")
                        else:
                            break
                        
                    # Ingresar patente
                    patenteValida = False
                    while not patenteValida:
                        patente = input("Ingrese la patente del vehículo (ej. AE456GH): ").upper()
                        patenteValida = validarPatenteExistente(patente, vehiculos)

                    # Ingresar kms
                    kmValidos = False
                    while not kmValidos:
                        totalKm = input("Ingrese la cantidad de km recorridos en la ruta: ")
                        kmValidos = validarCantKm(totalKm)

                    # Ingresar salida
                    fechaSalidaValida = False
                    while not fechaSalidaValida:
                        fechaSalida = input("Ingrese la fecha y hora de salida (AAAA.MM.DD HH.MM.SS): ")
                        fechaSalidaValida = validarFechaHora(fechaSalida)

                    # Ingresar llegada
                    fechaLlegadaValida = False
                    while not fechaLlegadaValida:
                        fechaLlegada = input("Ingrese la fecha y hora de llegada (AAAA.MM.DD HH.MM.SS): ")
                        fechaLlegadaValida = validarFechaHora(fechaLlegada)

                    # Confirmación
                    print("\nResumen de la ruta a registrar:")
                    print(f"Chofer: LU{legajo} - {choferes[int(legajo)]['nombre']} {choferes[int(legajo)]['apellido']}")
                    print(f"Vehículo: {patente} - {vehiculos[patente]['modelo']}")
                    print(f"Km recorridos: {totalKm} km")
                    print(f"Fecha y hora de salida: {fechaSalida}")
                    print(f"Fecha y hora de llegada: {fechaLlegada}")
                    confirmar = input("¿Desea registrar esta ruta? (s/n): ").lower()

                    if confirmar == "s" or confirmar == "si":
                        # Obtener la fecha y hora actual para la clave
                        fechaHora = obtenerFechaHora()

                        # Guardar ruta
                        rutas[fechaHora] = {
                            "legajo": int(legajo),
                            "patente": patente,
                            "totalKm": float(totalKm),
                            "fechaSalida": fechaSalida,
                            "fechaLlegada": fechaLlegada
                        }

                        # Actualizar km del chofer y vehículo
                        choferes[int(legajo)]['cantidadKm'] += float(totalKm)
                        vehiculos[patente]['cantidadKm'] += float(totalKm)

                        print(f"\nRuta registrada exitosamente.\n")

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
                    informeResumenMensualRutasVehiculos(rutas, vehiculos)
                
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