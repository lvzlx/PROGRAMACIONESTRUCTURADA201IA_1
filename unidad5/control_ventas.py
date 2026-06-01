# Declaración de estructuras

productos = ["Laptop", "Smartphone", "Tablet"]

ventas = [[0] * 3 for _ in range(3)]

 

# Lectura de datos

for i in range(3):

    print(f"--- Registro para {productos[i]} ---")

    for j in range(3):

        ventas[i][j] = int(input(f"Ventas del día {j+1}: "))

 

# Escritura y Reporte

print("\nRESUMEN DE VENTAS")

total_general = 0
total_por_producto = []
 

def lector_ventas():

    total_general=0
    
    for i in range(3):

        suma_producto = sum(ventas[i])
        total_por_producto.append(suma_producto)
        total_general += suma_producto

        print(f"{productos[i]}: {ventas[i]} | Total: {suma_producto}")

 

    print(f"\nEl total de ventas de la semana es: {total_general}")

    print(f"El promedio de ventas es: {total_general / 9:.2f}")

    #Producto mas vendido 
    index_max = total_por_producto.index(max(total_por_producto))
    print(f"El producto mas vendido es: {productos[index_max]} con {total_por_producto[index_max]} ventas.")



def main():
    lector_ventas()

if __name__ == "__main__":
    main()