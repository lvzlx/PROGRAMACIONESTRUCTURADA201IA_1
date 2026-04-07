"""
implementar en python una simulacion de un fondo de ahorro. 
El usuario realiza depositos mensuales de forma sucesiva hasta que la suma total iguala 
o supera una meta economica preestablecida de $1,000.
"""

def fondo_ahorro():
    
    saldo = 0
    meta = 1000
    while saldo < meta:
        deposito = float(input("Ingrese el monto del depósito mensual: "))
        saldo += deposito
    return saldo

def main():
    resultado = fondo_ahorro()
    print("Has alcanzado tu meta de ahorro con un saldo de:", resultado)

if __name__ == "__main__":
    main()