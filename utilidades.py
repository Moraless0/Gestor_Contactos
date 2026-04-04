def pedir_texto(mensaje):
    try:
        opc = input(mensaje).strip()
        if opc == "":
            print("Se debe ingresar un valor!")
        else:
            return opc
    except Exception:
        print("Error al pedir texto!")