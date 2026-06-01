# ==========================================
# IMPORTACIÓN DE BIBLIOTECAS (Biblioteca Estándar)
# ==========================================

import sys


# ==========================================
# FUNCIONES
# ==========================================

def limpiar_lecturas(lista_datos):
    """
    Recibe una lista de números flotantes que representan
    distancias detectadas por el sensor LIDAR.

    Elimina los valores atípicos menores a 0.0 y mayores
    a 100.0, retornando una nueva lista con datos válidos.
    """
    lista_filtrada = []

    for dato in lista_datos:
        if dato >= 0.0 and dato <= 100.0:
            lista_filtrada.append(dato)

    return lista_filtrada


def calcular_alertas(lista_filtrada, umbral_critico):
    """
    Recibe una lista de lecturas válidas y un umbral crítico.

    Cuenta cuántas lecturas están por debajo del umbral
    especificado y retorna el total de alertas.
    """
    total_alertas = 0

    for lectura in lista_filtrada:
        if lectura < umbral_critico:
            total_alertas += 1

    return total_alertas


def generar_log_sistema(total_alertas):
    """
    Recibe el total de alertas detectadas.

    Utiliza sys.platform para identificar la plataforma
    donde se ejecuta el programa y genera un mensaje
    de registro del sistema.

    Si las alertas son mayores a 3, la acción será
    ABORTAR. En caso contrario será PERMITIDA.
    """
    sistema = sys.platform

    if total_alertas > 3:
        accion = "ABORTAR"
    else:
        accion = "PERMITIDA"

    log = "[SISTEMA {}] Alertas críticas encontradas: {}. Acción: {}".format(
        sistema,
        total_alertas,
        accion
    )

    return log


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def main():

    # 1. Datos simulados de telemetría (con algunos errores de sensor)
    lecturas_raw = [12.5, -5.0, 88.2, 120.1, 1.2, 0.0, 45.6, 2.5]

    UMBRAL = 3.0

    print("=== SISTEMA DE TELEMETRÍA DE AGENTE AUTÓNOMO ===\n")

    # Invocar las funciones en el orden correcto
    lecturas_limpias = limpiar_lecturas(lecturas_raw)

    total_alertas = calcular_alertas(
        lecturas_limpias,
        UMBRAL
    )

    log_final = generar_log_sistema(total_alertas)

    print(log_final)


if __name__ == "__main__":
    main()

"""
EVIDENCIAS DE CONTROL DE CALIDAD

1. PROMPT UTILIZADO

Actúa como un programador experto en Python Estructurado.
Escribe el código de una función llamada limpiar_lecturas.
Recibe como parámetro una lista de números flotantes que
representan distancias a obstáculos detectados por el
LIDAR de un robot y debe retornar una nueva lista con los
valores válidos.

Restricciones estrictas:
1. No utilices programación orientada a objetos (POO).
2. No utilices manejo de excepciones (try-except).
3. Gestiona los errores usando condicionales if/else.
4. Incluye la documentación mediante un Docstring
descriptivo.

¿El codigo cumple con lo solicitado?

Da el codigo considerando lo pedido y las restricciones.

2. TABLA DE PRUEBA DE ESCRITORIO MANUAL

Caso de prueba:

lecturas_raw = [-10.5, 150.0, -2.0, 120.3]
UMBRAL = 3.0

Paso 1: limpiar_lecturas()

Dato = -10.5  -> descartado
Dato = 150.0  -> descartado
Dato = -2.0   -> descartado
Dato = 120.3  -> descartado

Resultado:
lecturas_limpias = []

Paso 2: calcular_alertas([], 3.0)

La lista está vacía.
No se cuentan alertas.

Resultado:
total_alertas = 0

Paso 3: generar_log_sistema(0)

Como 0 no es mayor que 3:

accion = "PERMITIDA"

Resultado final:

[SISTEMA plataforma] Alertas críticas encontradas: 0.
Acción: PERMITIDA


3. AUDITORÍA DE CÓDIGO

la ia propuso inicialmente utilizar una comprensión de
listas para filtrar los datos:

[dato for dato in lista_datos if 0.0 <= dato <= 100.0]

aunque esta sintaxis es válida en python, se decidió
reemplazarla por una estructura for tradicional con if
para mantener un enfoque básico y completamente
estructurado.

no se utilizaron bibliotecas externas, programación
orientada a objetos ni bloques try-except, por lo que
el código cumple con las restricciones establecidas
en la actividad.
"""
