"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código (Parte III)
Alumno: Luz María Robles Barradas
"""

import math  # El novato solo importó math esta vez

# =====================================================================
# RETO 1: Inicializador de Tablero de Juego (Matrices)
# Sentido: Crear una cuadrícula vacía de 4x4 (como el juego 2048 o un tablero)
#          inicializada con ceros antes de colocar las piezas de la IA.
# Problema: Uso erróneo y peligroso de multiplicación de referencias,
#           o bucles anidados manuales sumamente redundantes.
# =====================================================================
def inicializar_tablero_vacio():
    fila_base = [0, 0, 0, 0]
    tablero = [fila_base, fila_base, fila_base, fila_base]

    for i in range(4):
        for j in range(4):
            tablero[i][j] = 0

    return tablero


def inicializar_tablero_vacio_refactorizado():
    # Se utiliza una comprensión de listas para crear filas independientes.
    # Así se evita que todas las filas compartan la misma referencia en memoria.
    return [[0] * 4 for _ in range(4)]


# =====================================================================
# RETO 2: Recortador de Valores Atípicos (Clamping de Datos)
# Sentido: Limitar las señales de los sensores del robot a un rango seguro.
#          Si la señal baja de un mínimo o pasa de un máximo, se "recorta".
# Problema: Lógica condicional repetitiva y tosca que ignora funciones nativas.
# =====================================================================
def limitar_senal_sensor(valor_lectura, minimo, maximo):
    if valor_lectura < minimo:
        resultado = minimo
    else:
        if valor_lectura > maximo:
            resultado = maximo
        else:
            resultado = valor_lectura

    return resultado


def limitar_senal_sensor_refactorizado(valor_lectura, minimo, maximo):
    # max() garantiza que el valor no sea menor que el mínimo.
    # min() garantiza que el resultado no supere el máximo.
    # Se reemplaza toda la estructura condicional por una sola línea.
    return min(max(valor_lectura, minimo), maximo)


# =====================================================================
# RETO 3: Buscador del Valor Más Cercano a Cero (Error Mínimo)
# Sentido: Encontrar el menor error absoluto (loss) en una lista de pruebas.
# Problema: Inicialización incorrecta o manual de infinitos y cálculo
#           tosco del valor absoluto usando multiplicaciones por -1.
# =====================================================================
def buscar_error_minimo(lista_errores):
    menor_error = 999999.99

    for i in range(len(lista_errores)):
        valor_actual = lista_errores[i]

        if valor_actual < 0:
            absoluto = valor_actual * -1
        else:
            absoluto = valor_actual

        if absoluto < menor_error:
            menor_error = absoluto

    return menor_error


def buscar_error_minimo_refactorizado(lista_errores):
    # math.fabs() obtiene el valor absoluto utilizando la librería math.
    # min() encuentra directamente el menor valor absoluto de la lista.
    # Se elimina la variable auxiliar y las comparaciones manuales.
    return min(math.fabs(error) for error in lista_errores)


# =====================================================================
# RETO 4: Filtro de Valores Únicos (Eliminador de Duplicados)
# Sentido: Limpiar las IDs de los usuarios del servidor de Discord para
#          que no se procesen comandos repetidos en el mismo ciclo.
# Problema: Algoritmo de búsqueda lineal doblemente anidado sumamente lento.
# =====================================================================
def depurar_usuarios_repetidos(lista_ids):
    lista_limpia = []

    for i in range(len(lista_ids)):
        id_actual = lista_ids[i]
        ya_existe = False

        for j in range(len(lista_limpia)):
            if lista_limpia[j] == id_actual:
                ya_existe = True
                break

        if not ya_existe:
            lista_limpia.append(id_actual)

    return lista_limpia


def depurar_usuarios_repetidos_refactorizado(lista_ids):
    # set() elimina automáticamente los elementos duplicados.
    # Después se convierte nuevamente a lista.
    # Esta solución es mucho más eficiente que recorrer la lista
    # comparando cada elemento contra todos los anteriores.
    return list(set(lista_ids))


# === PROGRAMA PRINCIPAL (Punto de entrada para probar) ===
if __name__ == "__main__":
    print("--- Probando Código Inicial (Parte III) ---")

    tablero_ia = inicializar_tablero_vacio()

    print("Tablero inicializado de 4x4:")
    for fila in tablero_ia:
        print(fila)

    tablero_ia_ref = inicializar_tablero_vacio_refactorizado()

    print("\nTablero inicializado de 4x4 refactorizado:")
    for fila in tablero_ia_ref:
        print(fila)

    print(
        "\nLectura recortada (125.4 en rango 0-100):",
        limitar_senal_sensor(125.4, 0.0, 100.0)
    )

    print(
        "Lectura recortada refactorizada (125.4 en rango 0-100):",
        limitar_senal_sensor_refactorizado(125.4, 0.0, 100.0)
    )

    errores_entrenamiento = [0.45, -0.12, 0.89, -0.03, 0.22]

    print(
        "\nEl error más cercano a cero es:",
        buscar_error_minimo(errores_entrenamiento)
    )

    print(
        "El error más cercano a cero refactorizado es:",
        buscar_error_minimo_refactorizado(errores_entrenamiento)
    )

    ids_discord = [4521, 8892, 4521, 1022, 8892, 9931]

    print(
        "\nLista de IDs únicas filtradas:",
        depurar_usuarios_repetidos(ids_discord)
    )

    print(
        "Lista de IDs únicas filtradas refactorizada:",
        depurar_usuarios_repetidos_refactorizado(ids_discord)
    )

    