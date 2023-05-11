#Alan de Jesus Fabian Garcia 
import numpy as np

# Definir el entorno (ejemplo: un problema de 5 brazos)
num_brazos = 5
recompensas_medias = [1.0, 0.5, 0.2, 0.8, 0.3]  # Recompensas promedio para cada brazo

# Parámetros de la exploración vs explotación
epsilon = 0.2  # Probabilidad de exploración (ε)
num_ejecuciones = np.zeros(num_brazos)  # Contador de ejecuciones
valores_brazos = np.zeros(num_brazos)  # Valor estimado de cada brazo

# Simulación de las interacciones con el entorno
num_interacciones = 1000
recompensas_totales = 0
recompensas_registradas = []

for i in range(num_interacciones):
    # Selección de una acción
    if np.random.uniform() < epsilon:
        # Acción aleatoria para exploración
        accion = np.random.randint(num_brazos)
    else:
        # Acción óptima basada en los valores actuales
        accion = np.argmax(valores_brazos)
    
    # Obtener la recompensa para la acción seleccionada
    recompensa = np.random.normal(recompensas_medias[accion])
    
    # Actualizar la estimación de valor del brazo seleccionado
    num_ejecuciones[accion] += 1
    valores_brazos[accion] += (recompensa - valores_brazos[accion]) / num_ejecuciones[accion]
    
    # Registrar la recompensa obtenida
    recompensas_totales += recompensa
    recompensas_registradas.append(recompensa)

# Imprimir los resultados
promedio_recompensas = recompensas_totales / num_interacciones
print("Recompensa promedio obtenida:", promedio_recompensas)
