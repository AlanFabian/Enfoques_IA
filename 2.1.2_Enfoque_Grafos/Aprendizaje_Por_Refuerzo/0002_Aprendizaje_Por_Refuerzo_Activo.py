#Alan de Jesus Fabian Garcia 
import numpy as np

# Definir el entorno (ejemplo: un problema de 3 acciones)
num_acciones = 3
recompensas_medias = [0.1, 0.5, 1.0]  # Recompensas promedio para cada acción

# Inicializar los valores de acción y contador de visitas
valores_acciones = np.zeros(num_acciones)
num_ejecuciones = np.zeros(num_acciones)

# Parámetros del aprendizaje por refuerzo activo
epsilon = 0.1  # Probabilidad de exploración (ε)
num_episodios = 1000
num_pasos = 100

# Realizar el aprendizaje por refuerzo activo
for episodio in range(num_episodios):
    for paso in range(num_pasos):
        # Selección de una acción
        if np.random.uniform() < epsilon:
            # Acción aleatoria para exploración
            accion = np.random.randint(num_acciones)
        else:
            # Acción óptima basada en los valores actuales
            accion = np.argmax(valores_acciones)
        
        # Obtener la recompensa para la acción seleccionada
        recompensa = np.random.normal(recompensas_medias[accion])
        
        # Actualizar la estimación de valor de la acción seleccionada
        num_ejecuciones[accion] += 1
        valores_acciones[accion] += (recompensa - valores_acciones[accion]) / num_ejecuciones[accion]
        
# Imprimir los resultados
print("Valores de acción finales:")
for accion, valor in enumerate(valores_acciones):
    print(f"Acción {accion}: {valor}")
