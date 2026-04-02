import json

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

def seleccionar_opcion(n):
    if n == 1:
        print("opción #1")
        agregar_contacto()
    elif n == 2:
        print("opción #2")
    elif n == 3:
        print("opción #3")

def agregar_contacto ():
    nombre = input("Ingrese el nombre del contacto")
    correo_electronico = input("Ingrese el correo electronico")

    contacto = {
        "nombre" : nombre, "correo" : correo_electronico
    }

    try:
        with open("contactos.json", "r") as archivo:
            datos = json.load(archivo)
    
    except:
        datos = []
        
    datos.append(contacto)

    with open("contactos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)
        

       





    