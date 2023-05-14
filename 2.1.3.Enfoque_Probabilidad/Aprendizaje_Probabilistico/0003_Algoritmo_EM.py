#Alan de Jesus Fabian Garcia 
import numpy as np

# Datos observados
datos = np.array([[1, 2, np.nan, 4],
                  [5, np.nan, 7, 8],
                  [9, 10, 11, np.nan]])

# Número de iteraciones
num_iteraciones = 10

# Inicialización de parámetros
media_inicial = np.nanmean(datos)
varianza_inicial = np.nanvar(datos)
p_inicial = np.nanmean(~np.isnan(datos))

media_estimada = media_inicial
varianza_estimada = varianza_inicial
p_estimada = p_inicial

for i in range(num_iteraciones):
    # E-step: Calcular las probabilidades posteriores
    likelihood = np.exp(-0.5 * ((datos - media_estimada) ** 2) / varianza_estimada)
    prior = p_estimada
    posterior = likelihood * prior
    normalizacion = np.sum(posterior, axis=1, keepdims=True)
    posterior /= normalizacion

    # M-step: Actualizar los parámetros
    media_estimada = np.nansum(posterior * datos) / np.sum(posterior)
    varianza_estimada = np.nansum(posterior * ((datos - media_estimada) ** 2)) / np.sum(posterior)
    p_estimada = np.mean(posterior)

# Imprimir los resultados
print("Media estimada:", media_estimada)
print("Varianza estimada:", varianza_estimada)
print("Probabilidad estimada:", p_estimada)
