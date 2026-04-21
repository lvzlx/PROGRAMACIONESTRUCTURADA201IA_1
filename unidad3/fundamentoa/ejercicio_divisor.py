def calcular_division(dividendo, divisor):
    cociente = 0
    residuo = dividendo

    #representa el rombo
    while residuo >= divisor:
        residuo = residuo - divisor
        cociente = cociente + 1

    return cociente, residuo


def ejecutar_proceso():
    dividendo = int(input("Leer dividendo: "))
    divisor = int(input("Leer divisor: "))

    if divisor == 0:
        print("Error: división inválida")
    else:
        cociente, residuo = calcular_division(dividendo, divisor)

        print("Cociente:", cociente)
        print("Residuo:", residuo)


def main():
    ejecutar_proceso()


if __name__ == "__main__":
    main()