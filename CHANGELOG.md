# Changelog - TP Grupal Equipo N°12
En este archivo se documentan los cambios más importantes de la segunda versión de la entrega.

---

## [2.0] - 24-11-2025

### Nuevo
- **Gestión de archivos JSON:** Lectura y escritura de archivos JSON para Choferes, Vehículos y Rutas.
- **Expresiones regulares:** - Incorporación de campo `email` en Choferes y validación con módulo `re`.
- **Manejo de Errores:** Se incorporó `try-except` para gestionar entrada de datos y errores de archivos.

### Cambios
- **Modularización del CRUD:** Se movió toda la lógica de Ingreso, Desactivación y Modificación (incluyendo la apertura y cierre de archivos) desde el programa principal hacia sus respectivos módulos (`funciones/*.py`).
- **Diccionarios precargados:** Se comentaron con triples comillas los diccionarios de la versión 1.0.

### Arreglos
- **Informes Matriciales:** Se corrigieron los informes [2] y [3].
- **Limpieza del Main:** El archivo `Entrega2.py` ahora funciona exclusivamente como menú de navegación, y delega todas las operaciones a las funciones importadas.