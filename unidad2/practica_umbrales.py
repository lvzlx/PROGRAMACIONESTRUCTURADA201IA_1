"""
modelo de ia que entrega un vslor de confianza entre 0 y 1 o 0 y 100 
"""

def UMBRAL():
    UMBRAL_ALTO = 80.0
    UMBRAL_MINIMO = 40.0

    Instruccion = input("Ingrese una instrucción: ")
    print("¡instrucción recibida con exito!")

    Nivel_Confianza = float(input("Ingrese el nivel de confianza: "))

    if Nivel_Confianza >= UMBRAL_ALTO and Nivel_Confianza <95.0:
        print(Instruccion,"¡Instrucción Exitosa!")
    
    elif Nivel_Confianza > UMBRAL_MINIMO and Nivel_Confianza < UMBRAL_ALTO:
        print("Confianza insuficiente. ¿se refiere a?", Instruccion, ",Por favor confirme.")

    elif Nivel_Confianza >= 95.0:
        print(Instruccion,"¡Instrucción Exitosa!","Aviso: El modelo ha sido reforzado con éxito debido a la alta precisión.")   
    
    else:
        print("¡Error 404: No pude entender la instrucción. Intente hablar más claro!")
    
    print("Sesión de procesamiento finalizada")
    
    return Instruccion

def main():
    UMBRAL()

if __name__ == "__main__":
    main()