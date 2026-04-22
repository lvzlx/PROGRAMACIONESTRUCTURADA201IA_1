"""
Crear un asistente capaz de leer un mensaje, limpiar un texto y ser capaz de 
determinar si un usuario está dando una orden positiva o reportando un problema.
"""

def NORMALIZAR_MENSAJE():
    MENSAJE = input("Ingrese un mensaje:")
    MENSAJE = MENSAJE.lower()
    MENSAJE = MENSAJE.strip()
    print("Mensaje normalizado: ",MENSAJE)
    return MENSAJE


def DETECTAR_INTENCION(): 
    MENSAJE_NORMALIZADO = NORMALIZAR_MENSAJE()
    if "encender" in MENSAJE_NORMALIZADO or "activar" in MENSAJE_NORMALIZADO or "reproducir" in MENSAJE_NORMALIZADO:
        print("COMANDO DE ACCION")
    
    elif "ayuda" in MENSAJE_NORMALIZADO or "error" in MENSAJE_NORMALIZADO or "fallo" in MENSAJE_NORMALIZADO:
        print("REPORTE DE SOPORTE")
    else:
        print("CONSULTA GENERAL")
        
    Caracteres = len(MENSAJE_NORMALIZADO)
    print("Cantidad de caracteres: ", Caracteres)



def main():
    DETECTAR_INTENCION()


if __name__ == "__main__":
    main()