def convertir(numero):
    valores = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    simbolos = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

    resultado = ""
    i = 0

    while i < len(valores):
        if numero >= valores[i]:
            resultado += simbolos[i]
            numero -= valores[i]
        else:
            i += 1

    return resultado


def proceso():
    numero = input("Introducir número decimal: ")

     
    if not numero.isdigit():
        print("Error: no es entero")
        proceso()
        return

    numero = int(numero)


    if numero <= 0:
        print("Error: no es positivo")
        proceso()
        return

    
    if numero > 3000:
        print("Error: mayor a 3000")
        proceso()
        return

    
    resultado = convertir(numero)
    print("Número romano:", resultado)


def main():
    proceso()


if __name__ == "__main__":
    main()