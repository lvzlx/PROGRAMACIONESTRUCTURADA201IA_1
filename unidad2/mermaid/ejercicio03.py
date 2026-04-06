N = int(input("Ingresa la cantidad de números impares: "))

contador = 0
numero = 1

# este ciclo se repite mientras el contador sea menor que N
# se ejecuta hasta imprimir la cantidad de números que pidio el usuario
while contador < N:
    print(numero)
    numero = numero + 2
    contador = contador + 1
