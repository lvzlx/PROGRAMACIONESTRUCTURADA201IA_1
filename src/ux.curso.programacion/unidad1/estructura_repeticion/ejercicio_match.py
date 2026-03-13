#Implementacion de Match en Python

def demostracion():
    print("-- Ejemplo de match --")
    opcion = input("Ingrese una opcion (1-3): ")

    match opcion:
        case "1":
            print("Opcion 1 seleccionada")
            nombre = input("Ingrese su nombre: ")
            print(f"Hola, {nombre}!")
        case "2":
            print("Opcion 2 seleccionada")
            matricula = input("Ingrese su (matricula)")
            print(f"Su matricula es: {matricula}")
        case "3":
            print("Opcion 3 seleccionada")
            semestre=input("Ingrese su semestre:")
            print("Usted está en el semestre: {semestre}")
        case _:
            print("Opcion no valida")

def main():
    demostracion()

if __name__ == "__main__":
    main()