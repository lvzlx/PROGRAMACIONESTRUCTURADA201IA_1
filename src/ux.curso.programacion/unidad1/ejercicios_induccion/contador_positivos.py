#Desarrollo de algoritmo contador de positivos


"""
Esta función se encarga de que el código pueda finalizar o 
realizar el conteo de positivos, para 
finalizar se le solicita al usuario colocar un -1
"""
def contador_positivos():
    contador=0
    while True:
        #el int lo recibe como un entero y es la base para poder terminar el conteo
        numero = int(input("ingrese un numero (-1 para terminar):"))
        if numero <0:
            break;
        contador += 1

    print("cantidad de numeros positivos ingresados: ", contador)


"""
Esta funcion se encarga de que el usuario comicen a ingresar 
números, puesto que inicia dando a entender que es un contador
de positivos además de que "contador_positivos()" recibe los números
pafa que la otra función lo realice
"""
#Definicion de la funcion main (Controla el flujo del programa)
def main():
    print("Bienvenido al contador de positivos")
    contador_positivos()

"""
Ejecuta la función para que realice lo que se tiene programado
"""    
#LLamada de la funcion main para iniciar el programa
if __name__ == "__main__":
    main()