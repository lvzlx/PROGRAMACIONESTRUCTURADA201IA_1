"""
Funcion que recibe un texto y decide que responder.
implementa programacion esrtucturada pura.
"""

def procesar_pregunta(mensaje_usuario):
    #1.- Normaliazcion (paso fundamental en IA)
    mensaje = mensaje_usuario.lower().strip()
    #2.- Base de conocimientos (diccionario)
    conocimientos = {
    #conceptos de estructura de control
        "if": "La sentencia if es un condicional. permite que el programa tome decisiones basandose en una condicion boolenana",
    
    #Tipos de datos
        "int": "Representa numeros enteros, como 1, 2, 3, no tiene parte decimal",
    #Funciones y modularidad
        "def": "Es la palabra reservada para definir una funcion en python",
    #operadores y sintaxis
        "print": "Es una funcion incorporada en python que se utiliza para mostrar informacion en la consola",
    }
    #3.- Logica de busqueda
    for clave in conocimientos:
            if clave in mensaje:
                return conocimientos[clave]

    #3.- Busqueda en la base de conocimientos
    if mensaje in conocimientos:
        return conocimientos[mensaje]
    else:
        return "Lo siento, no entiendo esa pregunta."

def main():
    print("Bienvenido al agente de logica. Preguntame sobre conceptos de programacion.")
    while True:
        pregunta = input("Tu pregunta: ")
        if pregunta.lower() == "salir":
            print("Adios!")
            break
        respuesta = procesar_pregunta(pregunta)
        print("Respuesta:", respuesta)
    
    
#prueba locar (offline)
if __name__ == "__main__":
    main()