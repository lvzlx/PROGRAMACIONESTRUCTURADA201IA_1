"""
programa para procesar datos recogidos por los sensores del automovil y decidir la acción segura para el coche.
"""

# Función para simular la recolección de datos de los sensores del vehículo.
def datos_sensores ():
    distancia_metros = float(input("Ingrese la distancia al objeto más cercano en metros: "))
    color_semaforo = input("Ingrese el color del semáforo (rojo, amarillo, verde): ").lower()
    peaton = input("¿Hay un peatón cruzando? (sí/no): ")
    return distancia_metros, color_semaforo, peaton

# Función para decidir la acción del vehículo basada en los datos de los sensores.
def decidir_accion(distancia, semaforo, peatón):
    if distancia <= 5 or peatón == "sí": 
        return print ("¡FRENO DE EMERGENCIA ACTIVADO! Deteniendo el vehículo inmediatamente.")
    elif semaforo == "rojo":
        return print ("Estado: Detenido. Esperando luz verde.")
    elif semaforo == "amarillo":
        return print ("Estado: Precaución. Reduciendo velocidad para detenerse.")
    elif semaforo == "verde" and distancia >= 5:
        return print ("Estado: En movimiento. Todo despejado para avanzar.")
    else:
        return print ("Error de lectura en sensores: Color de semáforo no reconocido.")

def main():
    distancia, semaforo, peatón = datos_sensores()
    decidir_accion(distancia, semaforo, peatón)
    print ("Monitoreo de sensores constante... Sistema activo.")


if __name__ == "__main__":
    main()