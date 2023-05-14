#Alan de Jesus Fabian Garcia 
import pymc3 as pm
import numpy as np

# Datos observados
datos = np.array([0, 1, 0, 0, 1, 1, 1, 0, 1, 1])

# Definir el modelo
with pm.Model() as modelo:
    # Prior para la probabilidad
    p = pm.Beta('p', alpha=1, beta=1)

    # Likelihood (modelo generativo)
    y = pm.Bernoulli('y', p=p, observed=datos)

    # Muestreo de la distribución posterior
    traza = pm.sample(2000, tune=1000)

# Obtener los resultados
resultados = traza['p']

# Imprimir la estimación de la probabilidad
print("Probabilidad estimada:", resultados.mean())
