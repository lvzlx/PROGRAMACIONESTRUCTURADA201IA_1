# Limpieza de datos, normalización

umbral_bajo = 0.3
umbral_alto = 0.7
    
def clasificar_pixel (): 
    #Solicitar al usuario
    intensidad = float(input("Ingrese la intensidad del pixel (entre 0 y 0.1): "))
    
    #Si la intensidad es menor a 0.0 o mayor a 1.0, es un valor inválido
    if intensidad < 0.0 or intensidad > 1.0:
        print("Error: Valor de pixel invalido")
        return
    
    if 0.0 <= intensidad < umbral_bajo:
        print("Clasificacion (Fondo Oscuro)")
        return 
    
    if umbral_bajo < intensidad < umbral_alto:
        print("Clasificacion (Fondo GRIS)")
        return 
    
    if intensidad >= umbral_alto:
        print("Clasificacion (Objeto brillante)")
        return 

    print("Analisis de imagen finalizado")

def main():
    clasificar_pixel()

if __name__ == "__main__":
    main()