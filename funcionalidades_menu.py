from gestion_contactos import agregar_contacto, eliminar_contacto, listar_contactos
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

def seleccionar_opcion():
    while True:
        mostrar_menu()
        n = int(input("Ingrese un numero del 1-5: "))
        if n == 1:
            mostrar_separador()
            print("Opcion #1")
            print("Agregar un contacto nuevo")
            mostrar_separador()
            agregar_contacto()
        elif n == 2:
            print("Opcion #2")
            eliminar_contacto()
        elif n == 3:
            print("Opcion #3")
            listar_contactos()
        elif n == 4:
            print("Opcion #4")

        elif n == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Valor incorrecto!")
            pedir_texto("Pulse ENTER para intentar nuevamente.")

