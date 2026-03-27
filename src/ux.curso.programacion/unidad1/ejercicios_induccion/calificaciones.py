#Una variable guardará la calificacion obtenida

#Definicion de la funcion main (Controla el flujo del programa)
def main():
    while True:
        n= float(input("Ingrese una calificacion de 0 a 100:\n "))
        if n >= 0 and n <= 100:
            break
    else:
        print("Numero fuera del rango. Intenta nuevamente.")

    if n >= 90:
            grado= "A"
    elif n >= 80:
            grado= "B"
    elif n >= 70:
            grado= "C"
    elif n >= 69:
            grado= "D"
    else:
            grado = "F"
    print("El grado es:", grado)

#LLamada de la funcion main para iniciar el programa
if __name__ == "__main__":
    main()