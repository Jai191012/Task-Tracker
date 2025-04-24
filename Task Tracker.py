import json
from datetime import datetime

listado = ["Descripción", "Estado", "Creado con fecha", "Actualizado con fecha"]
tareas = []
archivo_json = "tareas.json"

def cargar_tareas():
    try:
        with open(archivo_json, "r") as archivo:
            global tareas
            tareas = json.load(archivo)
    except FileNotFoundError:
        tareas = []

def guardar_tareas():
    with open(archivo_json, "w") as archivo:
        json.dump(tareas, archivo, default=str, indent=4)

def ingresoMenu():
    cargar_tareas()
    while True:
        print("\n" + "="*40)
        print("ADMINISTRADOR DE TAREAS ; BIENVENIDO".center(40))
        print("="*40)
        print("1. Desea agregar una tarea")
        print("2. Mostrar tareas")
        print("3. Editar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        print("="*40 + "\n")
        opcion = input("Ingrese su opción: ")
        if opcion.isdigit() and 1 <= int(opcion) <= 5:
            if opcion == "1":
                agregarTarea()
            elif opcion == "2":
                mostrarTareas()
            elif opcion == "3":
                editarTarea()
            elif opcion == "4":
                eliminarTarea()
            elif opcion == "5":
                print("Saliendo del programa...")
                guardar_tareas()
                break
        else:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 5.")

def obtenerFecha(prompt):
    while True:
        try:
            fecha = input(prompt)
            return datetime.strptime(fecha, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Fecha inválida. Por favor, ingrese una fecha en formato YYYY-MM-DD HH:MM")

def agregarTarea():
    tarea = {}
    tarea["Descripción"] = input("Ingrese descripción: ")
    tarea["Estado"] = input("Ingrese estado: ")
    tarea["Creado con fecha"] = str(obtenerFecha("Ingrese fecha de creación (YYYY-MM-DD HH:MM): "))
    tarea["Actualizado con fecha"] = str(obtenerFecha("Ingrese fecha de actualización (YYYY-MM-DD HH:MM): "))
    tareas.append(tarea)
    guardar_tareas()
    print("Tarea agregada con éxito!")

def mostrarTareas():
    cargar_tareas()
    if not tareas:
        print("No hay tareas registradas.")
    else:
        for i, tarea in enumerate(tareas, start=1):
            print(f"Tarea {i}:")
            for campo, valor in tarea.items():
                print(f"{campo}: {valor}")
            print()

def editarTarea():
    cargar_tareas()
    if not tareas:
        print("No hay tareas registradas.")
    else:
        mostrarTareas()
        while True:
            try:
                indice = int(input("Ingrese el número de la tarea a editar: ")) - 1
                if 0 <= indice < len(tareas):
                    tarea = tareas[indice]
                    tarea["Descripción"] = input("Ingrese nueva descripción: ")
                    tarea["Estado"] = input("Ingrese nuevo estado: ")
                    tarea["Creado con fecha"] = str(obtenerFecha("Ingrese nueva fecha de creación (YYYY-MM-DD HH:MM): "))
                    tarea["Actualizado con fecha"] = str(obtenerFecha("Ingrese fecha de actualización (YYYY-MM-DD HH:MM): "))
                    guardar_tareas()
                    print("Tarea editada con éxito!")
                    break
                else:
                    print("Índice inválido. Por favor, ingrese un número válido.")
            except ValueError:
                print("Índice inválido. Por favor, ingrese un número.")

def eliminarTarea():
    cargar_tareas()
    if not tareas:
        print("No hay tareas registradas.")
    else:
        mostrarTareas()
        while True:
            try:
                indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
                if 0 <= indice < len(tareas):
                    del tareas[indice]
                    guardar_tareas()
                    print("Tarea eliminada con éxito!")
                    break
                else:
                    print("Índice inválido. Por favor, ingrese un número válido.")
            except ValueError:
                print("Índice inválido. Por favor, ingrese un número.")

ingresoMenu()