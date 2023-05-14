#Alan de Jesus Fabian Garcia 
import numpy as np

# Definición de las probabilidades
probabilidades = {'A': 0.3, 'B': 0.4, 'C': 0.2, 'D': 0.1}

# Generación de una decisión aleatoria basada en las probabilidades
decision = np.random.choice(list(probabilidades.keys()), p=list(probabilidades.values()))

# Imprimir la decisión
print("La decisión seleccionada es:", decision)
