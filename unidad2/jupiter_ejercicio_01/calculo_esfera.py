# calculo del radio de una esfera
import math

def define_esfera():
    radio = float(input("Ingrese el radio de la esfera en cm: "))
    volumen = (4/3) * math.pi * math.pow(radio, 3)
    print(f"El volumen de la esfera es {volumen} en cm cubicos")

def main():
    define_esfera()     

if __name__ == "__main__":
    main()