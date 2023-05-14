#Alan de Jesus Fabian Garcia 
import random

# Definición de la red bayesiana
red_bayesiana = {
    'A': {'prob': 0.6, 'parents': [], 'values': [True, False]},
    'B': {'prob': 0.3, 'parents': [], 'values': [True, False]},
    'C': {'prob': 0.2, 'parents': ['A', 'B'], 'values': [(True, True), (True, False), (False, True), (False, False)]},
    'D': {'prob': 0.8, 'parents': ['C'], 'values': [True, False]}
}

# Función para realizar el muestreo ponderado de verosimilitud
def ponderacion_verosimilitud(query, evidencia, n):
    resultados = {True: 0, False: 0}

    for _ in range(n):
        peso = 1.0
        estado = {}

        # Asignamos las evidencias conocidas
        for variable, valor in evidencia.items():
            estado[variable] = valor

        # Generamos una muestra aleatoria de las variables no evidenciales
        for variable in red_bayesiana.keys():
            if variable not in evidencia:
                prob = red_bayesiana[variable]['prob']
                parents = red_bayesiana[variable]['parents']
                values = red_bayesiana[variable]['values']
                if parents:
                    parent_values = tuple(estado[parent] for parent in parents)
                    idx = values.index(parent_values)
                    estado[variable] = values[idx][random.choice([0, 1])]
                else:
                    estado[variable] = random.choice(values)

                # Actualizamos el peso de acuerdo a las probabilidades condicionales
                peso *= prob if estado[variable] else 1 - prob

        # Actualizamos el resultado de acuerdo a la consulta
        resultados[estado[query]] += peso

    # Normalizamos los resultados
    total = sum(resultados.values())
    resultados = {k: v / total for k, v in resultados.items()}

    return resultados

# Ejemplo de uso del muestreo ponderado de verosimilitud
query_variable = 'D'
evidence_variables = {'A': True, 'B': False}
num_samples = 10000

resultado = ponderacion_verosimilitud(query_variable, evidence_variables, num_samples)
print(f"Probabilidad de {query_variable} dado {evidence_variables}:")
print(f"P({query_variable} | {evidence_variables}) = {resultado[True]:.4f}")
