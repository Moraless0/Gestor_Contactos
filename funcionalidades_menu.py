from gestion_contactos import agregar_contacto, eliminar_contacto, listar_contactos, buscar_contacto
from utilidades import pedir_texto

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
    try:
        while True:
            mostrar_menu()
            n = int(input("Ingrese el numero del 1-5: "))
            if n == 1:
                mostrar_separador()
                print("Opción #1")
                print("Agregar un contacto nuevo")
                mostrar_separador()
                agregar_contacto()
            elif n == 2:
                print("Opcion #2")
                eliminar_contacto()
            elif n == 3:
                print("Opción #3 - Buscar contacto")
                nombre = input("Ingrese el nombre a buscar: ").capitalize()
                buscar_contacto(nombre)
            elif n == 4:
                print("opción #4")
                listar_contactos()
            elif n == 5:
                print("Saliendo del programa...")
                break
            else:
                print("Valor incorrecto!")
                print("Ingrese un valor del 1-5 ")
                pedir_texto("Pulse ENTER para intentar nuevamente.")

                with open("error.txt", "a") as archivo:
                    archivo.write(f"Usuario ingresa valor incorrecto = {n}\n*")
    except:
        print("ERROR - INCORRECTO")
            
    