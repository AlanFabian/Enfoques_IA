#Alan de Jesus Fabian Garcia 
import numpy as np

# Definimos las estrategias de los jugadores
jugador1 = np.array([1, 2, 3])
jugador2 = np.array([4, 5, 6])

# Definimos la matriz de pagos
matriz_pagos = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])

# Encontramos el equilibrio de Nash utilizando la función argmax de NumPy
equilibrio_jugador1 = np.argmax(matriz_pagos, axis=1)
equilibrio_jugador2 = np.argmax(matriz_pagos, axis=0)

# Imprimimos los resultados
print("Equilibrio de Nash:")
print("Jugador 1:", jugador1[equilibrio_jugador1])
print("Jugador 2:", jugador2[equilibrio_jugador2])

# Calculamos el pago total del equilibrio de Nash
pago_total = matriz_pagos[equilibrio_jugador1, equilibrio_jugador2].sum()
print("Pago total del equilibrio de Nash:", pago_total)
