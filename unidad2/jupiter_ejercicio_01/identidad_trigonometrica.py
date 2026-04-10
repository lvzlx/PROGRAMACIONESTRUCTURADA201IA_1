# calculo de identidad trigonometrica
import math

def identidad_trigonometrica(x):
    numero_radianes = math.radians(x)
    seno_x = math.pow(math.sin(numero_radianes), 2)
    coseno_x = math.pow(math.cos(numero_radianes), 2)
    identidad = seno_x + coseno_x
    print(f"Para x = {x} grados, sin^2(x) + cos^2(x) = {identidad}")

def identidad_trigonometrica_2(x):
    numero_radianes = math.radians(x)
    seno_x = math.pow(math.sin(numero_radianes), 2)
    coseno_x = math.pow(math.cos(numero_radianes), 2)
    identidad = seno_x - coseno_x
    print(f"Para x = {x} grados, sin^2(x) - cos^2(x) = {identidad}")

def main():
    x = int(input("Ingrese el valor de x en grados: "))
    identidad_trigonometrica(x)
    identidad_trigonometrica_2(x)

if __name__ == "__main__":
    main()