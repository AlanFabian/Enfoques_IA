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

# Definimos la matriz de observaciones
observaciones = np.array([[1, 0, 0, 0, 0],
                          [0, 1, 0, 0, 0],
                          [0, 0, 1, 0, 0],
                          [0, 0, 0, 1, 0],
                          [0, 0, 0, 0, 1]])

# Definimos la función de creencia
def creencia(recompensas, transiciones, observaciones, gamma, creencias, politicas):
    estados = len(recompensas)
    creencias_actualizadas = np.zeros(estados)
    
    for estado in range(estados):
        creencia_actualizada = np.sum(transiciones[:, estado] * creencias)
        creencias_actualizadas[estado] = observaciones[estado, politicas[estado]] * creencia_actualizada
    
    creencias_actualizadas /= np.sum(creencias_actualizadas)
    
    return creencias_actualizadas

# Definimos la función de búsqueda de políticas óptimas
def buscar_politicas_pomdp(recompensas, transiciones, observaciones, gamma, creencias_iniciales):
    estados = len(recompensas)
    politicas = np.zeros(estados, dtype=int)
    creencias = creencias_iniciales
    
    while True:
        nuevas_politicas = politicas.copy()
        for estado in range(estados):
            creencias_actualizadas = creencia(recompensas, transiciones, observaciones, gamma, creencias, politicas)
            utilidad_acciones = []
            for accion in range(estados):
                utilidad_accion = np.sum(transiciones[estado, :] * creencias_actualizadas)
                nueva_utilidad = recompensas[estado, accion] + gamma * utilidad_accion
                utilidad_acciones.append(nueva_utilidad)
            mejor_accion = np.argmax(utilidad_acciones)
            nuevas_politicas[estado] = mejor_accion
        if np.array_equal(nuevas_politicas, politicas):
            break
        politicas = nuevas_politicas
    
    return politicas

# Definimos las creencias iniciales
creencias_iniciales = np.array([0.2, 0.3, 0.1, 0.1, 0.3])

# Aplicamos el proceso de decisión de Markov parcialmente observable (POMDP)
gamma = 0.9
politicas_optimas = buscar_politicas_pomdp(recompensas, transiciones, observaciones, gamma, creencias_iniciales)

# Mostramos las creencias iniciales
print("Creencias iniciales:")
for estado, creencia_inicial in enumerate(creencias_iniciales):
    print(f"Creencia para el estado {estado}: {creencia_inicial}")

# Mostramos las políticas óptimas
print("\nPolíticas óptimas:")
for estado, politica in enumerate(politicas_optimas):
    print(f"Política óptima para el estado {estado}: Acción {politica}")
