#Alan de Jesus Fabian Garcia 
import numpy as np

# Parámetros del modelo oculto de Markov
transiciones = np.array([[0.7, 0.3], [0.4, 0.6]])  # Matriz de transición
emisiones = np.array([[0.1, 0.4, 0.5], [0.7, 0.2, 0.1]])  # Matriz de emisión
pi = np.array([0.6, 0.4])  # Distribución inicial

observaciones = [0, 1, 2]  # Secuencia de observaciones

# Función para realizar el algoritmo hacia delante-atrás
def forward_backward(transiciones, emisiones, pi, observaciones):
    # Paso hacia delante
    alpha = []
    alpha_t = pi * emisiones[:, observaciones[0]]
    alpha.append(alpha_t)

    for t in range(1, len(observaciones)):
        alpha_t = np.dot(alpha_t, transiciones) * emisiones[:, observaciones[t]]
        alpha.append(alpha_t)

    # Paso hacia atrás
    beta = []
    beta_t = np.ones_like(pi)
    beta.append(beta_t)

    for t in range(len(observaciones) - 2, -1, -1):
        beta_t = np.dot(transiciones, emisiones[:, observaciones[t+1]] * beta_t)
        beta.insert(0, beta_t)

    # Cálculo de las distribuciones de probabilidad
    distribuciones = []
    for t in range(len(observaciones)):
        distribucion_t = alpha[t] * beta[t] / np.sum(alpha[t] * beta[t])
        distribuciones.append(distribucion_t)

    return distribuciones

# Ejemplo de uso del algoritmo hacia delante-atrás
distribuciones_probabilidad = forward_backward(transiciones, emisiones, pi, observaciones)

# Imprimir las distribuciones de probabilidad estimadas
for t, distribucion in enumerate(distribuciones_probabilidad):
    print(f"Distribución de probabilidad en el tiempo {t}:")
    print(distribucion)
