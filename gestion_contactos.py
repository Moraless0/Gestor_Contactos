from utilidades import pedir_texto
import json, os

def agregar_contacto ():
    nombre = input("Ingrese el nombre del contacto :").capitalize()
    apellido = input("Ingrese el apellido :").capitalize()
    correo_electrónico = input("Ingrese el correo electrónico :")
    numero = input("Ingrese el numero de teléfono :")
    numero_2 = input("Ingrese segundo numero :")

    contacto = {
        "nombre" : nombre, "apellido" : apellido, "correo" : correo_electrónico, "numero" : numero, "numero_2" : numero_2  }

    try:
        with open("contactos.json", "r") as archivo:
            datos = json.load(archivo)
    
    except:
        datos = []
        
    datos.append(contacto)

    with open("contactos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)
        
def eliminar_contacto ():
    nombre = input("Ingrese el nombre del contacto a eliminar: ").capitalize()

    with open("contactos.json", "r") as archivo:
        datos = json.load(archivo)

    nueva_lista = [c for c in datos if c["nombre"]!= nombre]

    if len (datos) == len(nueva_lista):
        print("No se encontró el contacto")
        pedir_texto("Presione ENTER para continuar...")
    else:
        print("Contacto eliminado correctamente")
        pedir_texto("Presione ENTER para continuar...")
    
    with open("contactos.json", "w") as archivo:
        json.dump(nueva_lista, archivo, indent=4)

def buscar_contacto(nombre_buscar):
    try:
        with open("contactos.json", "r") as archivo:
            contactos = json.load(archivo)
        
        encontrado = False

        for contacto in contactos:
            if contacto["nombre"] == nombre_buscar:
                print(f"""
Nombre: {contacto['nombre']}                           | 
Apellido: {contacto['apellido']}                       | 
Correo: {contacto['correo']}                           |
Numero: {contacto['numero']}                           | 
Numero 2: {contacto['numero_2']}""")
                print("=="*15)
                encontrado = True

        if not encontrado:
            print("No se encontró el contacto")

    except:
        print("Error al leer el archivo")

def listar_contactos():
    try:
        with open("contactos.json", "r") as archivo:
            contactos = json.load(archivo)
        for contactos in contactos:
            print("Nombre:", contactos["nombre"], contactos["apellido"])
            print("Numero de teléfono:", contactos["numero"], "-" , contactos["numero_2"])
            print("Correo electrónico:", contactos["correo"])
            print("=="*15)
    except:
        print("No hay contactos")
