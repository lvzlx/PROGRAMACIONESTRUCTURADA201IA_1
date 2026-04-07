'''
Algoritmo de acumulacion generica
'''

def acumulacion ():
    suma=0
    while True:
        numero=int(input("ingrese numero: "))
        if numero>=10 and numero<=50:
            suma+=numero
        else:
            break
    return suma

def main():
    resultado= acumulacion()
    print("la suma acumulada es:", resultado)

if __name__ == "__main__":
    main()
    