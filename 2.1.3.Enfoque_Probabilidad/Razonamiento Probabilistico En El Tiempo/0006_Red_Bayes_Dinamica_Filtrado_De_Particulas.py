#Alan de Jesus Fabian Garcia 
import numpy as np
import random

# Parámetros del modelo de la red bayesiana dinámica
transiciones = np.array([[0.7, 0.3], [0.4, 0.6]])  # Matriz de transición
emisiones = np.array([[0.1, 0.4, 0.5], [0.7, 0.2, 0.1]])  # Matriz de emisión

# Función para generar una muestra del estado oculto inicial
def generar_estado_inicial():
    estado_inicial = random.choices([0, 1], [0.6, 0.4])[0]
    return estado_inicial

# Función para generar una muestra del estado oculto dado el estado anterior
def generar_estado_actual(estado_anterior):
    estado_actual = random.choices([0, 1], transiciones[estado_anterior])[0]
    return estado_actual

# Función para generar una muestra de la observación dada el estado actual
def generar_observacion(estado_actual):
    observacion = random.choices([0, 1, 2], emisiones[estado_actual])[0]
    return observacion

# Función para inicializar la población de partículas
def inicializar_particulas(n):
    particulas = []
    for _ in range(n):
        estado = generar_estado_inicial()
        particulas.append(estado)
    return particulas

# Función para realizar el filtrado de partículas
def filtrado_particulas(observaciones, n_particulas):
    particulas = inicializar_particulas(n_particulas)
    pesos = np.ones(n_particulas) / n_particulas  # Pesos uniformes inicialmente

    for obs in observaciones:
        for i in range(n_particulas):
            estado_actual = generar_estado_actual(particulas[i])
            particulas[i] = estado_actual

            prob_emision = emisiones[estado_actual][obs]
            pesos[i] *= prob_emision

        pesos = pesos / np.sum(pesos)  # Normalizar los pesos

    estado_estimado = np.random.choice(particulas, p=pesos)

    return estado_estimado

# Ejemplo de uso del filtrado de partículas en una red bayesiana dinámica
observaciones = [0, 1, 2]  # Secuencia de observaciones
n_particulas = 100  # Número de partículas

estado_estimado = filtrado_particulas(observaciones, n_particulas)

# Imprimir el estado estimado
print("Estado estimado:", estado_estimado)
