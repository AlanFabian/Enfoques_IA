#Alan de Jesus Fabian Garcia 
import numpy as np

# Parámetros del modelo oculto de Markov
transiciones = np.array([[0.7, 0.3], [0.4, 0.6]])  # Matriz de transición
emisiones = np.array([[0.1, 0.4, 0.5], [0.7, 0.2, 0.1]])  # Matriz de emisión
pi = np.array([0.6, 0.4])  # Distribución inicial

observaciones = [0, 1, 2]  # Secuencia de observaciones

# Función para realizar la decodificación del estado oculto más probable utilizando el algoritmo de Viterbi
def viterbi(transiciones, emisiones, pi, observaciones):
    T = len(observaciones)
    N = transiciones.shape[0]

    # Paso inicial
    delta = np.zeros((T, N))
    psi = np.zeros((T, N), dtype=int)
    delta[0] = pi * emisiones[:, observaciones[0]]

    # Paso recursivo
    for t in range(1, T):
        for j in range(N):
            delta[t, j] = np.max(delta[t-1] * transiciones[:, j]) * emisiones[j, observaciones[t]]
            psi[t, j] = np.argmax(delta[t-1] * transiciones[:, j])

    # Decodificación del estado oculto más probable
    estados_ocultos = np.zeros(T, dtype=int)
    estados_ocultos[T-1] = np.argmax(delta[T-1])

    for t in range(T-2, -1, -1):
        estados_ocultos[t] = psi[t+1, estados_ocultos[t+1]]

    return estados_ocultos

# Ejemplo de uso del modelo oculto de Markov con el algoritmo de Viterbi
estados_ocultos_probables = viterbi(transiciones, emisiones, pi, observaciones)

# Imprimir los estados ocultos más probables
print("Estados ocultos más probables:")
print(estados_ocultos_probables)
