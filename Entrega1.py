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
import random


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
                "turno1": "Lunes - Mañana",
                "turno2": "Miércoles - Mañana",
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
                    print("------------------------------------")
                    print("MENÚ DE CHOFERES > Ingresar choferes")
                    print("------------------------------------\n")

                    while True:
                        # Crear legajo
                        while True:
                            legajo = random.randint(10000, 99999)
                            if legajo not in choferes:
                                break
                        
                        # Solicitar nombre
                        nombre = ""
                        while not nombre:
                            nombre = input("Ingrese el primer nombre del chofer: ")

                            if nombre.strip() == "":
                                print("El nombre no puede estar vacío. Intente nuevamente.")
                                nombre = ""
                            else:
                                for char in nombre:
                                    if not char.isalpha():
                                        print("El nombre solo puede contener letras. Intente nuevamente.")
                                        nombre = ""

                        # Solicitar apellido
                        apellido = ""
                        while not apellido:
                            apellido = input("Ingrese el primer apellido del chofer: ")

                            if nombre.strip() == "":
                                print("El apellido no puede estar vacío. Intente nuevamente.")
                                apellido = ""
                            else:
                                for char in nombre:
                                    if not char.isalpha() and char != " ":
                                        print("El apellido solo puede contener letras y espacios. Intente nuevamente.")
                                        apellido = ""

                        # Solicitar teléfono
                        telefono = ""
                        while not telefono:
                            telefono = input("Ingrese el teléfono del chofer: +54 11 ")

                            if len(telefono) != 8:
                                print("El teléfono debe tener 8 dígitos. Intente nuevamente.")
                                telefono = ""
                            elif not telefono.isdigit():
                                print("El teléfono solo puede contener números. Intente nuevamente.")
                                telefono = ""

                        # Solicitar cantidad de km recorridos
                        while True:
                            cantidadKm = input("Ingrese la cantidad de km recorridos por el chofer (Presione Enter para 0): ")

                            if cantidadKm == "":
                                cantidadKm = 0
                                break
                            elif not cantidadKm.isdigit() or int(cantidadKm) < 0:
                                print("La cantidad de km solo puede contener números. Intente nuevamente.")
                            else:
                                break

                        # Agregar turnos
                        turnos = {}
                        for i in range(3):
                            # Ingresar nuevo día
                            diaTurno = input("Ingrese el nuevo día (Lunes, Martes, etc.): ")
                            while diaTurno not in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
                                print("Día inválido. Intente nuevamente.")
                                diaTurno = input("Ingrese el nuevo día (Lunes, Martes, etc.): ")

                            # Ingresar nuevo horario
                            horarioTurno = input("Ingrese el nuevo horario (Mañana, Tarde o Noche): ")
                            while horarioTurno not in ["Mañana", "Tarde", "Noche"]:
                                print("Horario inválido. Intente nuevamente.")
                                horarioTurno = input("Ingrese el nuevo horario (Mañana, Tarde o Noche): ")

                            nuevoTurno = f"{horarioTurno} - {diaTurno}"

                            # Confirmar turno
                            confirmarTurno = input(f"¿Confirma el turno {nuevoTurno}? (s/n): ").lower()
                            if confirmarTurno == "s" or confirmarTurno == "si":
                                turnos[f"turno{i+1}"] = nuevoTurno
                            else:
                                print("Turno no confirmado. Intente nuevamente.")
                                i -= 1  # Se resta 1 al índice para repetir el mismo turno

                        # Guardar chofer
                        choferes[legajo] = {
                            "activo": True,
                            "nombre": nombre,
                            "apellido": apellido,
                            "telefono": telefono,
                            "cantidadKm": int(cantidadKm),
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

                        # Seleccionar dato a modificar
                        print("\nDatos actuales del chofer:")
                        print(f"1. Nombre: {choferes[int(legajo)]['nombre']}")
                        print(f"2. Apellido: {choferes[int(legajo)]['apellido']}")
                        print(f"3. Teléfono: +54 11 {choferes[int(legajo)]['telefono']}")
                        print(f"4. Cantidad de km: {choferes[int(legajo)]['cantidadKm']}")
                        print(f"5. Ver turnos")
                        print(f"6. Estado activo: {'Sí' if choferes[int(legajo)]['activo'] else 'No'}")
                        print("\n¿Qué dato desea modificar?")
                        
                        opcion = input("Ingrese el número de la opción (1-6): ")
                        
                        if opcion == "1":
                            # Ingresar nuevo nombre
                            nombre = ""
                            while not nombre:
                                nombre = input("Ingrese el primer nombre del chofer: ")

                                if nombre.strip() == "":
                                    print("El nombre no puede estar vacío. Intente nuevamente.")
                                    nombre = ""
                                else:
                                    for char in nombre:
                                        if not char.isalpha():
                                            print("El nombre solo puede contener letras. Intente nuevamente.")
                                            nombre = ""

                            # Guardar nuevo nombre
                            choferes[int(legajo)]['nombre'] = nombre

                            print("\nDato modificado exitosamente.")
                            
                        elif opcion == "2":
                            # Ingresar nuevo apellido
                            apellido = ""
                            while not apellido:
                                apellido = input("Ingrese el primer apellido del chofer: ")

                                if nombre.strip() == "":
                                    print("El apellido no puede estar vacío. Intente nuevamente.")
                                    apellido = ""
                                else:
                                    for char in nombre:
                                        if not char.isalpha() and char != " ":
                                            print("El apellido solo puede contener letras y espacios. Intente nuevamente.")
                                            apellido = ""

                            # Guardar nuevo apellido
                            choferes[int(legajo)]['apellido'] = apellido

                            print("\nDato modificado exitosamente.")

                        elif opcion == "3":
                            # Solicitar teléfono
                            telefono = ""
                            while not telefono:
                                telefono = input("Ingrese el teléfono del chofer: +54 11 ")

                                if len(telefono) != 8:
                                    print("El teléfono debe tener 8 dígitos. Intente nuevamente.")
                                    telefono = ""
                                elif not telefono.isdigit():
                                    print("El teléfono solo puede contener números. Intente nuevamente.")
                                    telefono = ""

                            # Guardar nuevo teléfono
                            choferes[int(legajo)]['telefono'] = telefono

                            print("\nDato modificado exitosamente.")

                        elif opcion == "4":
                            # Ingresar nueva cantidad de km recorridos
                            while True:
                                cantidadKm = input("Ingrese la cantidad de km recorridos por el chofer (Presione Enter para 0): ")

                                if cantidadKm == "":
                                    cantidadKm = 0
                                    break
                                elif not cantidadKm.isdigit() or int(cantidadKm) < 0:
                                    print("La cantidad de km solo puede contener números. Intente nuevamente.")
                                else:
                                    break

                            # Guardar nueva cantidad de km
                            choferes[int(legajo)]['cantidadKm'] = int(cantidadKm)

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
                                # Ingresar nuevo día
                                diaNuevoTurno = input("Ingrese el nuevo día (Lunes, Martes, etc.) o '-' para dejar vacío: ")
                                if diaNuevoTurno == "-":
                                    # Si se ingresa "-", eliminar el turno
                                    del choferes[int(legajo)]['turnos'][f"turno{turnoModificar}"]
                                    print("\nTurno eliminado exitosamente.")
                                else:
                                    while diaNuevoTurno not in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
                                        print("Día inválido. Intente nuevamente.")
                                        diaNuevoTurno = input("Ingrese el nuevo día (Lunes, Martes, etc.) o '-' para dejar vacío: ")
                                        if diaNuevoTurno == "-":
                                            break

                                    if diaNuevoTurno != "-":
                                        # Ingresar nuevo horario
                                        horarioNuevoTurno = input("Ingrese el nuevo horario (Mañana, Tarde o Noche): ")
                                        while horarioNuevoTurno not in ["Mañana", "Tarde", "Noche"]:
                                            print("Horario inválido. Intente nuevamente.")
                                            horarioNuevoTurno = input("Ingrese el nuevo horario (Mañana, Tarde o Noche): ")

                                        nuevoTurno = f"{horarioNuevoTurno} - {diaNuevoTurno}"
                                        choferes[int(legajo)]['turnos'][f"turno{turnoModificar}"] = nuevoTurno
                                        print("\nDato modificado exitosamente.")
                            
                        elif opcion == "6":
                            # Modificar estado
                            estado = input("¿Desea que el chofer esté activo? (s/n): ").lower()
                            if estado == "s" or estado == "si":
                                choferes[int(legajo)]['activo'] = True
                            elif estado == "n" or estado == "no":
                                choferes[int(legajo)]['activo'] = False

                            print("\nDato modificado exitosamente.")
                            
                        else:
                            print("Opción inválida.")
                            break
                            
                        # Preguntar si desea modificar otro chofer
                        modificarOtro = input("¿Desea modificar otro chofer? (s/n): ").lower()
                        if modificarOtro != "s" and modificarOtro != "si":
                            break
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    print("------------------------------------")
                    print("MENÚ DE CHOFERES > Eliminar choferes")
                    print("------------------------------------\n")

                    while True:
                        # Se pide el número de legajo a eliminar
                        legajo = input("Ingrese el legajo del chofer a eliminar (o '0' para salir): ")

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
                            confirmar = input(f"¿Está seguro que desea eliminar al chofer {chofer['nombre']} {chofer['apellido']} (LU{legajo})? (s/n): ").lower()
                            
                            # Si el usuario confirma la acción, se elimina el chofer. Sino, se cancela la operación
                            if confirmar == "s" or confirmar == "si":
                                del choferes[legajo]
                                print(f"Chofer LU{legajo} eliminado exitosamente.\n")
                            else:
                                print("Eliminación cancelada.\n")
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    print("--------------------------------------")
                    print("MENÚ DE CHOFERES > Listado de choferes")
                    print("--------------------------------------\n")

                    # Imprimir los títulos de la tabla
                    print("-" * 135)
                    print(f"|{'Legajo':^8}|{'Nombre':^25}|{'Teléfono':^17}|{'Km Recorridos':^15}|{'Activo':^8}|{'Turnos':^55}|")
                    print("-" * 135)

                    # Imprimir filas de datos
                    for legajo, datos in choferes.items():
                        nombre_completo = datos['nombre'] + " " + datos['apellido']
                        
                        # Procesar celda de turnos
                        celdaTurnos = ""
                        if len(datos['turnos']) == 0:
                            celdaTurnos = "Sin turnos"
                        else:
                            for turno in datos['turnos'].values():
                                if celdaTurnos == "":
                                    celdaTurnos = turno
                                else:
                                    celdaTurnos += ", " + turno

                        # Procesar celda de activo
                        if datos['activo']:
                            activo_str = "Sí"
                        else:
                            activo_str = "No"
                        
                        # Imprimir fila
                        print("|" +
                            str(legajo).center(8) + "| " +                              # Celda legajo
                            nombre_completo.ljust(24) + "| " +                          # Celda nombre completo
                            str("+54 11 " + str(datos['telefono'])).ljust(8) + " | " +  # Celda teléfono
                            str(datos['cantidadKm']).ljust(14) + "| " +                 # Celda km recorridos
                            activo_str.ljust(7) + "| " +                                # Celda activo
                            (celdaTurnos).ljust(54) + "|")                              # Celda turnos
                    
                    # Cerrar tabla
                    print("-" * 135)

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