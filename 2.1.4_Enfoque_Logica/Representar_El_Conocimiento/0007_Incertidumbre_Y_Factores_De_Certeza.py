#Alan de jesus Fabian Garcia 
import numpy as np
from scipy.stats import norm

# Definición de variables y distribuciones
media = 5
desviacion_estandar = 2

# Creación de una distribución normal
distribucion = norm(loc=media, scale=desviacion_estandar)

# Cálculo de la probabilidad de un evento
evento = 7
probabilidad = distribucion.pdf(evento)

# Imprimir resultado
print("La probabilidad de que el evento ocurra es:", probabilidad)
