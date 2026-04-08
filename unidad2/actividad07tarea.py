"""
implementación en python un algoritmo de cálculo
de tiempo laboral acumulado siguiendo un diagrama 
de flujo.
"""

def acumulacion_semanas():
    total_acumulado = 0
    semanas = 0 
    meta = 2500

    while total_acumulado <= meta:
        salario_semanal = int(input("ingrese su salario semanal: "))
        total_acumulado = total_acumulado + salario_semanal
        semanas = semanas + 1
        
    
    print("Semanas trabajadas:", semanas)
    print("Su salario acumulado es:", total_acumulado)

    
def main():
    acumulacion_semanas()

if __name__ == "__main__":
    main()