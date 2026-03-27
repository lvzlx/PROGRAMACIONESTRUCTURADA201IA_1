import math

# Demostracion del uso de math

def mostrar_funciones_math(numero):
    #crear variable

    sen_x = math.sin(numero)
    conse_x = math.cos(numero)
    tan_x= math.tan(numero)

    print("la tangente de", numero, "es =", tan_x)
    print("el seno de", numero, "es =", sen_x)
    print("el coseno de", numero, "es =", conse_x)

    resultado = sen_x ** 2 + conse_x ** 2 

    print("el resultado de sen^2(x) + cos^2(x) es =", resultado)

def main():
    numero = float(input("ingrese un numero: "))
    mostrar_funciones_math(numero)

if __name__ == "__main__":
    main()