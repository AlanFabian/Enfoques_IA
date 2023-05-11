#Alan de Jesus Fabian Garcia 
import numpy as np

# Definimos la matriz de recompensas
recompensas = np.array([[0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1]])

# Definimos la matriz de transiciones
transiciones = np.array([[0, 1, 0, 0, 0],
                         [0, 0, 1, 0, 0],
                         [0, 0, 0, 1, 0],
                         [0, 0, 0, 0, 1],
                         [0, 0, 0, 0, 0]])

# Definimos la función de utilidad
def utilidad(recompensas, transiciones, gamma, politicas):
    estados = len(recompensas)
    utilidades = np.zeros(estados)
    
    while True:
        nuevas_utilidades = utilidades.copy()
        for estado in range(estados):
            politica = politicas[estado]
            utilidad = np.sum(transiciones[estado, :] * utilidades)
            nueva_utilidad = recompensas[estado, politica] + gamma * utilidad
            nuevas_utilidades[estado] = nueva_utilidad
        if np.max(np.abs(nuevas_utilidades - utilidades)) < 1e-6:
            break
        utilidades = nuevas_utilidades
    
    return utilidades

# Definimos la función de búsqueda de políticas óptimas
def buscar_politicas(recompensas, transiciones, gamma):
    estados = len(recompensas)
    politicas = np.zeros(estados, dtype=int)
    utilidades = utilidad(recompensas, transiciones, gamma, politicas)
    
    for estado in range(estados):
        mejores_utilidades = []
        for accion in range(estados):
            utilidad_accion = np.sum(transiciones[estado, :] * utilidades)
            nueva_utilidad = recompensas[estado, accion] + gamma * utilidad_accion
            mejores_utilidades.append(nueva_utilidad)
        mejor_accion = np.argmax(mejores_utilidades)
        politicas[estado] = mejor_accion
    
    return politicas

# Aplicamos el proceso de decisión de Markov
gamma = 0.9
politicas_optimas = buscar_politicas(recompensas, transiciones, gamma)

# Mostramos las políticas óptimas
for estado, politica in enumerate(politicas_optimas):
    print(f"Política óptima para el estado {estado}: Acción {politica}")
