import json

import pyfiglet
from colorama import Fore, Style
banner= pyfiglet.figlet_format("ToDo List / Gestor de Tareas en Consola")
print(Fore.RED + banner + Style.RESET_ALL)
while True:
    print(Fore.YELLOW + "Elige una opción colocando el numero (Ej: 1): )")
    print(Fore.YELLOW + "1.- Registrar tareas \n2.- Listar tareas\n3.- Marcar tareas como hechas\n4.- Eliminar tareas \n5.- Cerrar gestor")
    opcion = input(Fore.YELLOW + "Elige una opción: ")

    if opcion == "5":
        despedida= pyfiglet.figlet_format("Hasta la proximaaaaaaaaaaaaaaaaaaaa.....")
        print(Fore.RED + despedida + Style.RESET_ALL)
        break
    if opcion not in ["1","2","3","4","5"]:
        print("El gestor no tiene esa opción")
        continue
    if opcion == "1":
        registros = []
        while True:
            tarea = input(Fore.YELLOW + "Hola, escribe tu tarea: ")
            fecha = input("Coloca la fecha: ")
            registro = {
                "tarea" : tarea,
                "fecha" : fecha
            }

            registros.append(registro)
            continuar = input("¿Desea agregar una tarea más? (s/n):").lower()
            if continuar != "s":
                 break
        with open("datos.json", "w", encoding="utf-8") as archivos:
            json.dump(registros, archivos, ensure_ascii=False, indent=4)
    if opcion == "2":
        with open('datos.json', 'r') as archivos:
            obj = json.load(archivos)
        print(f"estas son todas tus tareas pendientes: {obj}")

    if opcion == "4":
         print("¿Qué tarea deseas eliminar?")
         with open('datos.json', 'r') as archivos:
             datos = json.load(archivos)
             print(f"{datos}\n Escribe todos el nombre de la tarea que deseas borrar")




    


