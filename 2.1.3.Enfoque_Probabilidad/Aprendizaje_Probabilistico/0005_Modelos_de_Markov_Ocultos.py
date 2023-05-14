#Alan de Jesus Fabian Garcia 
from hmmlearn import hmm
import numpy as np

# Definir los parámetros del modelo HMM
n_states = 2  # Número de estados ocultos
n_symbols = 3  # Número de símbolos observables

# Crear un objeto HMM
model = hmm.MultinomialHMM(n_components=n_states, n_iter=100)

# Definir la matriz de transición de estados
trans_matrix = np.array([[0.7, 0.3], [0.4, 0.6]])
model.transmat_ = trans_matrix

# Definir la matriz de emisión de símbolos observables
emission_matrix = np.array([[0.2, 0.3, 0.5], [0.6, 0.2, 0.2]])
model.emissionprob_ = emission_matrix

# Definir la distribución inicial de estados
initial_dist = np.array([0.8, 0.2])
model.startprob_ = initial_dist

# Generar una secuencia de observaciones
sequence_length = 10
obs_sequence, hidden_states = model.sample(sequence_length)

# Imprimir la secuencia de observaciones generada
print("Secuencia de observaciones generada:")
print(obs_sequence)

# Imprimir los estados ocultos correspondientes
print("Estados ocultos correspondientes:")
print(hidden_states)
