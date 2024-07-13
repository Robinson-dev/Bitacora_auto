"""
Crear un programa que permita unir la mayoría de los conocimientos adquiridos durante el
semestre. Este programa permitirá guardar los eventos o acciones que se realizan en
auto, será una bitácora de todas las acciones que el auto realiza, ejemplo: Se registra
como un texto las acciones encender auto, colocar alarma, auto encendido, auto
estacionado, auto con nivel de aceite bajo, etc . Se debe utilizar sentencia While, For,
listas, Try Except, validaciones, archivo CSV y funciones. Se debe generar un menú de
opciones para poder agregar acciones a la bitácora, debe ser un texto, la segunda opción
es para ver la bitácora de las acciones hechas en el auto, una tercera opción que guarda
la bitácora en un archivo CSV y una cuarta opción para salir.
"""

import csv
from datetime import datetime

bitacora = []

def agregar_evento(evento):
    fecha_hora_actual = datetime.now().strftime("%d-%m-%y-%H-%M-%S")
    fecha_evento = f"{fecha_hora_actual} - {evento}"
    bitacora.append(fecha_evento)
    print(f"Evento '{evento}' registrado en la bitácora del auto.")

def historico():
    if not bitacora:
        print("La bitácora está vacía.")
    else:
        print("Bitácora histórica:")
        for evento in bitacora:
            print(evento)

def guardar_registro_csv(nombre_archivo):
    try:
        with open(nombre_archivo, "w", newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow(["Bitácora del auto"]) 
            for evento in bitacora:
                writer.writerow([evento])
        print(f"Registro guardado en '{nombre_archivo}' con éxito.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}. Por favor, coloque un nombre y extensión de archivo válidos.")

def menu():
    while True:
        print("\nMenú de registro histórico de acciones en el Auto")
        print("1. Agregar acción")
        print("2. Verificar histórico")
        print("3. Guardar en archivo CSV")
        print("4. Salir")
        try:
            opcion = int(input("Ingrese una opción del menú: "))

            if opcion == 1:
                print("Escriba la acción (Ej. encender el auto, viaje de Santiago a Puerto Montt, apagar auto, colocar alarma)")
                evento = input("Escriba la acción: ")
                agregar_evento(evento)
            elif opcion == 2:
                historico()
            elif opcion == 3:
                nombre_archivo = input("Ingrese el nombre del archivo CSV para guardar el registro. Ej: bitacoraAuto.csv: ")
                guardar_registro_csv(nombre_archivo)
            elif opcion == 4:
                print("Saliendo de la bitácora.")
                break
            else:
                print("Opción no válida. Por favor, ingrese una opción válida.")
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese un valor numérico válido.")

if __name__ == "__main__":
    menu()














