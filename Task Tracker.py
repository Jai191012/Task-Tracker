import json
from datetime import datetime

listado = ["Descripción", "Estado", "Creado con fecha", "Actualizado con fecha"]
tareas = []
archivo_json = "tareas.json"

def cargar_tareas():
    try:
        with open(archivo_json, "r", encoding="utf-8") as archivo:
            global tareas
            tareas = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        tareas = []

def guardar_tareas():
    with open(archivo_json, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False, default=str)

def ingresoMenu():
    cargar_tareas()
    while True:
        print("\n" + "="*40)
        print("ADMINISTRADOR DE TAREAS ; BIENVENIDO".center(40))
        print("="*40)
        print("1. Desea agregar una tarea")
        print("2. Editar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")
        print("="*40 + "\n")
        opcion = input("Ingrese su opción: ")
        if opcion.isdigit() and 1 <= int(opcion) <= 4:
            if opcion == "1":
                agregarTarea()
            elif opcion == "2":
                editarTarea()
            elif opcion == "3":
                eliminarTarea()
            elif opcion == "4":
                print("Saliendo del programa...")
                guardar_tareas()
                break
        else:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 4.")

def agregarTarea():
    tarea = {}
    tarea["Descripción"] = input("Ingrese descripción: ")

    opciones_estado = {
        "1": "Sin gestión",
        "2": "En proceso",
        "3": "Culminada"
    }

    while True:
        print("\nSeleccione el estado de la tarea:")
        for clave, valor in opciones_estado.items():
            print(f"{clave}) {valor}")
        opcion = input("Opción: ").strip()
        if opcion in opciones_estado:
            tarea["Estado"] = opciones_estado[opcion]
            break
        else:
            print("Opción inválida. Intente nuevamente.")
    
    tarea["Creado con fecha"] = datetime.now().strftime('%d/%m/%Y %H:%M')
    tarea["Actualizado con fecha"] = []

    tareas.append(tarea)
    guardar_tareas()

    print(f"\nTarea {len(tareas)}:")
    for campo in listado:
        print(f"{campo}: {tarea.get(campo, '')}")

def editarTarea():
    cargar_tareas()
    if not tareas:
        print("No hay tareas registradas.")
        return
    
    for i, tarea in enumerate(tareas, start=1):
        print(f"Tarea {i}:")
        for campo in listado:
            valor = tarea.get(campo, "")
            if campo == "Actualizado con fecha" and isinstance(valor, list):
                print(f"{campo}:")
                for fecha in valor:
                    print(f"  - {fecha}")
            else:
                print(f"{campo}: {valor}")
        print()

    try:
        indice = int(input("Ingrese el número de la tarea a editar (o 0 para cancelar): ")) - 1
        
        if indice == -1:
            print("Edición cancelada.")
            return
        
        if 0 <= indice < len(tareas):
            tarea = tareas[indice]
            print(f"\nEditando tarea: {tarea.get('Descripción', '')}")
            
            estados = {
                "1": "Sin gestión",
                "2": "En proceso",
                "3": "Culminada"
            }

            while True:
                print("\nSeleccione el nuevo estado:")
                for clave, valor in estados.items():
                    print(f"{clave}) {valor}")
                opcion = input("Opción: ").strip()

                if opcion in estados:
                    tarea["Estado"] = estados[opcion]
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")

            if "Actualizado con fecha" not in tarea or not isinstance(tarea.get("Actualizado con fecha"), list):
                tarea["Actualizado con fecha"] = []

            tarea["Actualizado con fecha"].append(datetime.now().strftime('%d/%m/%Y %H:%M'))

            guardar_tareas()
            print("Tarea editada con éxito!")
        else:
            print("Índice inválido. Por favor, ingrese un número válido.")
    except ValueError:
        print("Índice inválido. Por favor, ingrese un número.")

def eliminarTarea():
    cargar_tareas()
    if not tareas:
        print("No hay tareas registradas.")
        return
    
    for i, tarea in enumerate(tareas, start=1):
        print(f"Tarea {i}:")
        for campo in listado:
            valor = tarea.get(campo, "")
            if campo == "Actualizado con fecha" and isinstance(valor, list):
                print(f"{campo}:")
                for fecha in valor:
                    print(f"  - {fecha}")
            else:
                print(f"{campo}: {valor}")
        print()

    while True:
        try:
            indice = int(input("Ingrese el número de la tarea a eliminar (o 0 para cancelar): ")) - 1
            
            if indice == -1:
                print("Eliminación cancelada.")
                return
            
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