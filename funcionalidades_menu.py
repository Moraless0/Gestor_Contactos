from gestion_contactos import agregar_contacto, eliminar_contacto, listar_contactos, buscar_contacto
from utilidades import pedir_texto
import os

def mostrar_separador():
    print("==="*11)

def mostrar_menu():
    mostrar_separador()
    print("""BIENVENIDO AL GESTOR DE CONTACTOS
          
    # 1- Agregar contacto nuevo
    # 2- Eliminar contacto
    # 3- Buscar un contacto
    # 4- Mostrar contactos 
    # 5- Salir del programa
    """)
    mostrar_separador()

def seleccionar_opción():
    while True:
        try:
            os.system("clear")
            mostrar_menu()
            n = int(input("Ingrese el numero del 1-5: "))
            if n == 1:
                os.system("clear")
                mostrar_separador()
                print("Opción #1 - Agregar contacto nuevo")
                print("Agregar un contacto nuevo")
                mostrar_separador()
                agregar_contacto()
            elif n == 2:
                os.system("clear")
                mostrar_separador()
                print("Opción #2 - Eliminar contacto")
                eliminar_contacto()
            elif n == 3:
                os.system("clear")
                mostrar_separador()
                print("Opción #3 - Buscar contacto")
                nombre = input("Ingrese el nombre a buscar: ").capitalize()
                buscar_contacto(nombre)
            elif n == 4:
                os.system("clear")
                mostrar_separador()
                print("Opción #4 - Mostrar todos los contactos")
                listar_contactos()
            elif n == 5:
                os.system("clear")
                print("Saliendo del programa...")
                break
            else:
                os.system("clear")
                print("Opcion no valida!")
                print("Ingrese un valor del 1-5 ")
                pedir_texto("Pulse ENTER para intentar nuevamente.", permitir_vacio=True)

                with open("error.txt", "a") as archivo:
                 archivo.write(f"ERROR: Opción inválida = {n}\n\n")

                    
        except ValueError:
            os.system("clear")
            print("ERROR - INCORRECTO")
            with open("error.txt", "a") as archivo:
                archivo.write(f"Usuario ingresa valor incorrecto \n\n")
            pedir_texto("Pulse ENTER para continuar...", permitir_vacio=True)
            
       
            
    