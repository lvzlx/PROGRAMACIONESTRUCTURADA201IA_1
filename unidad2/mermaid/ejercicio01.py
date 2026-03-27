"""
Diseñar un algoritmo que calcule la suma de 
todos los números enteros del 1 al 100 que son
divisbles por 3 y, además, impares.
"""

def es_divisible():
    suma = 0
    i = 1
    while i <= 100:
        if i % 3 == 0 and i % 2 != 0:
            suma += i
        i += 1
    return suma

def main():
    suma = es_divisible()
    print(suma)
    
if __name__ == "__main__":
    main()
    