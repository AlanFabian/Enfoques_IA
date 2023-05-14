#Alan de Jesus Fabian Garcia 
import random

# Definición de la matriz de transición de la cadena de Markov
matriz_transicion = [
    [0.2, 0.8],
    [0.6, 0.4]
]

# Función para generar una cadena de Markov utilizando el algoritmo Monte Carlo
def monte_carlo_cadenas_markov(estado_inicial, num_pasos):
    cadena = [estado_inicial]

    for _ in range(num_pasos - 1):
        estado_actual = cadena[-1]
        proximo_estado = None

        # Generar una muestra aleatoria para elegir el próximo estado
        muestra = random.uniform(0, 1)

        # Determinar el próximo estado de acuerdo a la matriz de transición
        if estado_actual == 0:
            if muestra <= matriz_transicion[estado_actual][0]:
                proximo_estado = 0
            else:
                proximo_estado = 1
        elif estado_actual == 1:
            if muestra <= matriz_transicion[estado_actual][0]:
                proximo_estado = 0
            else:
                proximo_estado = 1

        # Agregar el próximo estado a la cadena
        cadena.append(proximo_estado)

    return cadena

# Ejemplo de uso del algoritmo Monte Carlo para Cadenas de Markov
estado_inicial = 0
num_pasos = 10

cadena_markov = monte_carlo_cadenas_markov(estado_inicial, num_pasos)
print("Cadena de Markov generada:")
print(cadena_markov)
