#es para obtener la hora real del sistema
from datetime import datetime

#configuracion de variables, primero se crea la variable y se le asigna un nombre.
nombre_asistente = "quikin"

"""
en esta funcion se llevan a cabo todas las estructuras condicionales 
con el proposito de identificar la intencion del usuario.
"""

def ejecutar_asistente():
    #mensaje de bienvenida
    print(f"te doy la bienvenida, soy {nombre_asistente}, tu asistente y estoy listo para ayudarte.")

    #entrada de datos
    frase = input("¿en que te puedo ayudar hoy?: ").lower()

    #clasificacion de intencion
    if "hola" in frase or "buenos días" in frase:
        print("¡Hola! Soy tu asistente, es un gusto saludarte.")

    elif "clima" in frase or "temperatura" in frase:
        print("consultando el servicio meteorologico... hoy en Xalapa tendremos un día nublado.")

    elif "hora" in frase or "tiempo" in frase:
        hora_actual = datetime.now().strftime("%I:%M %p")
        print(f"la hora actual del sistema es: {hora_actual}")

    else:
        print("lo siento, todavía no entiendo ese comando, ¿podrías intentar con otra palabra?")

    #despedida
    print(f"proceso finalizado, gracias tiline por usar {nombre_asistente}.")



def main():
    ejecutar_asistente()

if __name__ == "__main__":
    main()
