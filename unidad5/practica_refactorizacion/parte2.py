"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código (Parte II)
Alumno: Luz María Robles Barradas
"""
import random  # Única librería importada por el novato
import statistics  # Se agrega para utilizar la función median(), evitando ordenar y calcular la mediana manualmente.

# =====================================================================
# RETO 1: Formateador de Nombres de Usuario para Discord
# Sentido: Asegurar que los nombres en la base de datos no tengan espacios
#          extras y que inicien con mayúscula (Formato Limpio).
# Problema: Limpieza manual carácter por carácter usando bucles.
# =====================================================================
def limpiar_nombre_usuario(nombre_sucio):
    # El novato intenta quitar los espacios del inicio y final manualmente
    nombre_sin_espacios = ""
    inicio = 0
    fin = len(nombre_sucio) - 1
    
    while inicio <= fin and nombre_sucio[inicio] == " ":
        inicio += 1
    while fin >= inicio and nombre_sucio[fin] == " ":
        fin -= 1
        
    for i in range(inicio, fin + 1):
        nombre_sin_espacios += nombre_sucio[i]
        
    # Intento manual de poner la primera letra en mayúscula y el resto en minúscula
    if len(nombre_sin_espacios) > 0:
        primera_letra = nombre_sin_espacios[0]
        # Código ASCII para convertir a mayúscula si es minúscula
        if 'a' <= primera_letra <= 'z':
            primera_letra = chr(ord(primera_letra) - 32)
            
        resto_cadena = ""
        for i in range(1, len(nombre_sin_espacios)):
            caracter = nombre_sin_espacios[i]
            if 'A' <= caracter <= 'Z':
                caracter = chr(ord(caracter) + 32)
            resto_cadena += caracter
            
        return primera_letra + resto_cadena
    return ""

def limpiar_nombre_usuario_refactorizado(nombre_sucio):
    # strip() elimina automáticamente los espacios al inicio y final.
    # capitalize() convierte la primera letra en mayúscula y el resto
    # en minúsculas, reemplazando todo el proceso manual.
    return nombre_sucio.strip().capitalize()


# =====================================================================
# RETO 2: Buscador de Palabras Prohibidas (Filtro contra Groserías)
# Sentido: Banear o censurar mensajes inapropiados en el chat del servidor.
# Problema: Uso innecesario de un ciclo indexado para buscar subcadenas.
# =====================================================================
def contiene_palabra_bloqueada(mensaje_chat, palabra_prohibida):
    largo_mensaje = len(mensaje_chat)
    largo_palabra = len(palabra_prohibida)
    
    # Recorre el mensaje buscando coincidencia exacta letra por letra
    for i in range(largo_mensaje - largo_palabra + 1):
        coincidencia = True
        for j in range(largo_palabra):
            if mensaje_chat[i + j] != palabra_prohibida[j]:
                coincidencia = False
                break
        if coincidencia:
            return True
            
    return False

def contiene_palabra_bloqueada_refactorizado(mensaje_chat, palabra_prohibida):
    # El operador "in" ya realiza la búsqueda de una subcadena dentro
    # de otra cadena, evitando recorrer carácter por carácter.
    return palabra_prohibida in mensaje_chat

# =====================================================================
# RETO 3: Generador de Contraseñas Temporales para Nuevos Usuarios
# Sentido: Asignar una clave alfanumérica segura al registrar un agente.
# Problema: Algoritmo ineficiente para concatenar elementos aleatorios.
# =====================================================================
def generar_clave_temporal():
    caracteres_validos = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789"
    clave_generada = ""
    
    # El novato genera 8 caracteres uno por uno usando un ciclo e índices aleatorios
    for i in range(8):
        indice_aleatorio = random.randint(0, len(caracteres_validos) - 1)
        caracter_elegido = caracteres_validos[indice_aleatorio]
        clave_generada = clave_generada + caracter_elegido # Concatenación repetitiva
        
    return clave_generada

def generar_clave_temporal_refactorizado():
    
    # random.choices() selecciona varios caracteres aleatorios en una sola
    # instrucción.
    # join() une todos los caracteres de manera más eficiente que realizar
    # concatenaciones repetidas dentro de un ciclo.

    caracteres_validos = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789"
    return ''.join(random.choice(caracteres_validos) for _ in range(8))

# =====================================================================
# RETO 4: Buscador del Valor Central (Mediana de Latencia de Red)
# Sentido: Encontrar el punto medio de ping (ms) para evaluar lag.
# Problema: Implementación manual de un ordenamiento complejo (Burbuja) 
#           y cálculo manual de la mediana.
# =====================================================================
def calcular_mediana_latencia(lista_pings):
    # Clonamos la lista para no alterar la original
    pings_ordenados = list(lista_pings)
    n = len(pings_ordenados)
    
    # Método de la burbuja manual para ordenar los pings de menor a mayor
    for i in range(n):
        for j in range(0, n - i - 1):
            if pings_ordenados[j] > pings_ordenados[j + 1]:
                # Intercambio manual de variables
                temporal = pings_ordenados[j]
                pings_ordenados[j] = pings_ordenados[j + 1]
                pings_ordenados[j + 1] = temporal
                
    # Cálculo manual del elemento central (Mediana)
    if n % 2 == 1:
        return pings_ordenados[n // 2]
    else:
        mitad1 = pings_ordenados[(n // 2) - 1]
        mitad2 = pings_ordenados[n // 2]
        return (mitad1 + mitad2) / 2.0

def calcular_mediana_latencia_refactorizado(lista_pings):
    # statistics.median() ya contiene la lógica necesaria para calcular
    # la mediana, eliminando la necesidad de ordenar manualmente la lista
    # mediante el método burbuja y calcular el valor central.
    return statistics.median(lista_pings)


# === PROGRAMA PRINCIPAL (Punto de entrada para probar) ===
if __name__ == "__main__":
    print("--- Probando Código Inicial (Parte II) ---")

    print("Usuario limpio:",
          limpiar_nombre_usuario("   luNA_eDUaRDo  "))

    print("Usuario limpio refactorizado:",
          limpiar_nombre_usuario_refactorizado("   luNA_eDUaRDo  "))

    msg = "No digas malas palabras en este servidor"

    print("¿Tiene groserías?:",
          contiene_palabra_bloqueada(msg, "malas"))

    print("¿Tiene groserías? refactorizado:",
          contiene_palabra_bloqueada_refactorizado(msg, "malas"))

    print("Clave generada por el sistema:",
          generar_clave_temporal())

    print("Clave generada refactorizada:",
          generar_clave_temporal_refactorizado())

    pings_servidor = [120, 45, 80, 23, 150, 62]

    print("Mediana de latencia encontrada:",
          calcular_mediana_latencia(pings_servidor))

    print("Mediana de latencia refactorizada:",
          calcular_mediana_latencia_refactorizado(pings_servidor))