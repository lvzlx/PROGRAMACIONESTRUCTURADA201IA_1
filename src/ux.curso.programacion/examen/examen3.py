#Ejercicio 3
#Entrada de datos: Aquí se solicitan la frecuencia de ambos agentes

frecuencia_A = int(input("Ingrese la frecuencia del Agente A (Hz): "))
frecuencia_B = int(input("Ingrese la frecuencia del Agente B (Hz): "))

#Se verifica si una frecuencia es divisible por la otra

if frecuencia_A % frecuencia_B == 0 or frecuencia_B % frecuencia_A == 0:
    
#Posibles salidas
    
    print("Existe sincronización perfecta de ciclos")
    
else:
    
    print("No hay sincronización")