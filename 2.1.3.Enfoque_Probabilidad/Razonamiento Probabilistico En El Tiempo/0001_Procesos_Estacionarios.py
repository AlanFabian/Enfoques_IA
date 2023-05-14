#Alan de Jesus Fabian Garcia 
import random

# Definición de parámetros del proceso estacionario
estado_inicial = 0
num_pasos = 10

# Función de transición del proceso estacionario
def transicion(estado_actual):
    if estado_actual == 0:
        return random.choices([0, 1], weights=[0.7, 0.3])[0]
    elif estado_actual == 1:
        return random.choices([0, 1], weights=[0.4, 0.6])[0]

# Función para generar la secuencia del proceso estacionario
def generar_proceso_estacionario(estado_inicial, num_pasos):
    proceso = [estado_inicial]

    for _ in range(num_pasos - 1):
        estado_actual = proceso[-1]
        proximo_estado = transicion(estado_actual)
        proceso.append(proximo_estado)

    return proceso

# Ejemplo de uso de la razón probabilística en el tiempo para procesos estacionarios
proceso_estacionario = generar_proceso_estacionario(estado_inicial, num_pasos)
print("Proceso estacionario generado:")
print(proceso_estacionario)
