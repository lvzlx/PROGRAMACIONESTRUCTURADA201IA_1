"""
implementación en python de un inicio de sesión siguiendo una logica de iteración y desición 
anidada definida.
"""

def seguridad():

    intentos= 0
    clave_correcta= "1234"

    while intentos <= 3:

        clave = input("ingrese la contraseña por favor: ")
        if clave == clave_correcta:
            print("¡Acceso concedido!")

            break

        elif clave:
            intentos = intentos + 1
            print("¡Error!, contraseña incorrecta")

            if intentos > 3:
                print("¡Acceso denegado!, cuenta bloqueada")    
    

def main():
    seguridad()

if __name__ == "__main__":
    main()