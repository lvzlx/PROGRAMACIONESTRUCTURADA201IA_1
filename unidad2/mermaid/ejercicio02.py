"""
Implementar en Python el algoritmo para calcular el Factorial de un número 
siguiendo estrictamente la lógica definida en el Diagrama de Flujo proporcionado.
"""

def factorial(n):
    input_num = n
    factorial = 1
    i = 1
    while i <= input_num:
        factorial = factorial * i
        i += 1
    return factorial

    
def main():
    n = int(input("Ingrese un número para calcular su factorial: "))
    resultado = factorial(n)
    print(resultado)

if __name__ == "__main__":
    main()
    