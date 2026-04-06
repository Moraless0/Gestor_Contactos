from utilidades import pedir_texto
import json, os

def agregar_contacto ():
    nombre = input("Ingrese el nombre del contacto ").capitalize()
    apellido = input("Ingrese el apellido ").capitalize()
    correo_electrónico = input("Ingrese el correo electrónico ")
    numero = input("Ingrese el numero de teléfono ")
    numero_2 = input("Ingrese segundo numero ")

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
        with open("error.txt", "a") as archivo:
            archivo.write("Usuario intenta eliminar contacto no existe\n\n")
        pedir_texto("Pulse ENTER para continuar...", permitir_vacio=True)
    else:
        print("Contacto eliminado correctamente")
        pedir_texto("Pulse ENTER para continuar...", permitir_vacio=True)
    
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
Nombre: {contacto['nombre']}                           
Apellido: {contacto['apellido']}                        
Correo: {contacto['correo']}                           
Numero: {contacto['numero']}                            
Numero 2: {contacto['numero_2']}""")
                print("=="*15)
                encontrado = True
                pedir_texto("Pulse ENTER para continuar...", permitir_vacio=True)

        if not encontrado:
            print("No se encontró el contacto")
            with open("error.txt", "a") as archivo:
                archivo.write("Usuario intenta buscar contacto inexistente \n\n")
            pedir_texto("Pulse ENTER para continuar...", permitir_vacio=True)

    except:
        print("Error al leer el archivo")
        with open("error.txt", "a") as archivo:
            archivo.write(f"Error al leer el archivo\n\n" )
        pedir_texto("Pulse ENTER para continuar...", permitir_vacio=True)

def listar_contactos():
    os.system("clear")
    try:
        with open("contactos.json", "r") as archivo:
            contactos = json.load(archivo)
        for contactos in contactos:
            print("Nombre:", contactos["nombre"], contactos["apellido"])
            print("Numero de teléfono:", contactos["numero"], "-" , contactos["numero_2"])
            print("Correo electrónico:", contactos["correo"])
            print("=="*18)
    except:
        print("No hay contactos")
        with open("error.txt", "a") as archivo:
            archivo.write("No existen contactos\n\n")
        pedir_texto("Pulse ENTER para continuar...", permitir_vacio=True)

    pedir_texto("Pulse ENTER para continuar...", permitir_vacio=True)