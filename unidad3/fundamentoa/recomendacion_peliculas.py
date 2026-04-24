"""
implementación en python de un sistema de recomendación de peliculas
 basado en perfiles de distintos usuarios.
"""

peliculas_accion = ["Mad Max", "John Wick", "Inception"]
peliculas_comedia = ["Toy Story", "Minions", "Free Guy"]
peliculas_terror = ["It", "The Conjuring", "Saw"]

print("¡Hola, bienvenido, el agente de recomendación está en funcionamiento!")    
edad_usuario = int(input("¿Cual es tu edad? "))
genero_elegido = input("¿Qué género de película prefieres? (acción, comedia, terror) ")

def Obtener_recomendacion(genero_elegido, edad_usuario):
    if genero_elegido == "comedia" and edad_usuario < 13: 
        print("¡ La mejor recomendacion para el usuario es!: " + peliculas_comedia[0])
    
    elif genero_elegido == "acción" and edad_usuario < 13:
        print("Nota: Debido a tu edad, hemos ajustado la recomendación a contenido apto para todo público, nuestra recomendacion adecuada es: "+ peliculas_comedia[0])
    
    elif genero_elegido == "terror" and edad_usuario < 13:
        print("Nota: Debido a tu edad, hemos ajustado la recomendación a contenido apto para todo público, nuestra recomendacion adecuada es: "+ peliculas_comedia[0])
    
    elif genero_elegido == "comedia" and edad_usuario >= 13:
        print("¡ La mejor recomendacion para el usuario es!: " + peliculas_comedia[0])
    
    elif genero_elegido == "acción" and edad_usuario >= 13:
        print("¡ La mejor recomendacion para el usuario es!: " + peliculas_accion[0])
    
    elif genero_elegido == "terror" and edad_usuario >= 13:
        print("¡ La mejor recomendacion para el usuario es!: " + peliculas_terror[0])       


def main():
    Obtener_recomendacion(genero_elegido, edad_usuario)
    

if __name__ == "__main__":
    
    main()