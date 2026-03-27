import math

#demostracion del uso de funciones de math

def mostrar_funciones_math():
    #Crear una variable
    numero= 20

    sen_x = math.sin(numero)
    conse_x = math.cos(numero)

    print("El seno de", numero, "es:", sen_x)
    print("El coseno de", numero, "es:", conse_x)

    resultado = sen_x ** 2 + conse_x ** 2
    
    print("El resultado de sen^2(x) * cos^2(x) es:", resultado)

    def main():
        mostrar_funciones_math()

    if __name__ == "__main__":
        main()
