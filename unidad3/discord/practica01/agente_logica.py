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
        "for": "El bucle for se utiliza para iterar sobre una secuencia (como una lista, tupla, o cadena) o cualquier objeto iterable. Permite ejecutar un bloque de codigo varias veces, una por cada elemento en la secuencia",
        "while": "El bucle while se utiliza para ejecutar un bloque de codigo mientras una condicion sea verdadera. Es util cuando no se sabe de antemano cuantas veces se repetira el bloque de codigo",   
        
    #Tipos de datos
        "int": "Representa numeros enteros, como 1, 2, 3, no tiene parte decimal",
        "float": "Representa numeros con parte decimal, como 3.14 o 2.0",
        "str": "Representa cadenas de texto, como 'Hola' o 'Python'",
    #Funciones y modularidad
        "def": "Es la palabra reservada para definir una funcion en python",
        "print": "Es una funcion incorporada en python que se utiliza para mostrar informacion en la consola",
        "return": "Es la forma en que la función te entrega el resultado de su trabajo.",
        
    #Conceptos de programacion estructurada
        "programacion estructurada": "Es un paradigma de programacion que se basa en la division del programa en bloques o modulos, utilizando estructuras de control como if, for, while, y funciones para organizar el codigo de manera clara y facil de entender"
        "Secuencia: Las instrucciones se ejecutan una tras otra en el orden en que aparecen"
        "Selección (Estructuras condicionales): Permite elegir entre dos o más caminos dependiendo de una condición"
        "Iteración (Bucles): Permite repetir un bloque de código mientras se cumpla una condición o para cada elemento en una colección"
        
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