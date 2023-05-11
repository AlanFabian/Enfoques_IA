#Alan de Jesus Fabian Garcia 
import numpy as np

# Definimos las variables y sus estados
variables = ['T', 'X', 'Y']
estados = {'T': 2, 'X': 2, 'Y': 2}

# Definimos las conexiones temporales entre variables
conexiones = [('T', 'X'), ('T', 'Y'), ('X', 'Y')]

# Definimos las Tablas de Probabilidad Condicional (CPDs)
cpds = {
    'T': np.array([0.5, 0.5]),
    'X': np.array([[0.7, 0.3], [0.3, 0.7]]),
    'Y': np.array([[0.8, 0.2], [0.4, 0.6]])
}

# Realizamos inferencia en el modelo
evidence = {'T': 0}
target = 'Y'
query = {}

# Propagación hacia adelante
for variable in variables:
    if variable in evidence:
        query[variable] = np.zeros(estados[variable])
        query[variable][evidence[variable]] = 1.0
    else:
        parents = [p for p, v in conexiones if v == variable]
        cpd = cpds[variable]
        for parent in parents:
            cpd = np.dot(np.diag(cpds[parent]), cpd)
        query[variable] = np.sum(cpd, axis=0)

# Propagación hacia atrás
order = variables[::-1]
for variable in order:
    if variable != target:
        parents = [p for v, p in conexiones if v == variable]
        cpd = cpds[variable]
        for parent in parents:
            cpd = np.dot(cpd, np.diag(cpds[parent]))
        query[variable] = np.dot(cpd, query[variable])

# Normalización
query[target] /= np.sum(query[target])

# Imprimimos la distribución de probabilidad condicional
print(f"P({target} | T = {evidence['T']}) =")
print(query[target])

# Generamos muestras del modelo
n_samples = 5
samples = np.zeros((n_samples, len(variables)), dtype=int)

# Generamos el estado inicial de T
samples[:, 0] = np.random.choice(estados['T'], size=n_samples, p=cpds['T'])

# Generamos los estados sucesivos de X e Y
for i in range(1, len(variables)):
    variable = variables[i]
    parents = [p for p, v in conexiones if v == variable]
    cpd = cpds[variable]
    for parent in parents:
        cpd = np.dot(np.diag(cpds[parent]), cpd)
    cpd = np.reshape(cpd, (estados[variable],))  # Convertir la matriz a un vector 1D
    samples[:, i] = np.random.choice(estados[variable], size=n_samples, p=cpd)

# Imprimimos las muestras generadas
print("Muestras generadas:")
print(samples)
