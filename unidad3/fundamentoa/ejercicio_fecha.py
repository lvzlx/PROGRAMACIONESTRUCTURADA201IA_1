def leer_fecha():
    return input("Introduzca la fecha (DD/MM/AAAA): ")


def es_formato_valido(f):
    return len(f) == 10 and f[2] == '/' and f[5] == '/'


def validar_fecha():
    fecha = leer_fecha()

    # Validar formato
    if not es_formato_valido(fecha):
        print("Formato incorrecto")
        validar_fecha()
        return

    # Extraer datos
    dia = int(fecha[0] + fecha[1])
    mes = int(fecha[3] + fecha[4])
    anio = int(fecha[6] + fecha[7] + fecha[8] + fecha[9])

    # Validaciones (como en el diagrama)
    if dia < 1 or dia > 31:
        print("Día inválido")
        validar_fecha()

    elif mes < 1 or mes > 12:
        print("Mes inválido")
        validar_fecha()

    elif anio < 0 or anio > 2026:
        print("Año inválido")
        validar_fecha()

    else:
        print("Fecha válida")


def main():
    validar_fecha()


if __name__ == "__main__":
    main()