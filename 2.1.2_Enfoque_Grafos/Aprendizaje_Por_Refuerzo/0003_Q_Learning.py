#Alan de Jesus Fabian Garcia 
import numpy as np

# Definir el entorno (ejemplo: un problema de 3 acciones)
num_estados = 3
num_acciones = 3
recompensas = np.array([
    [-1, 0, 0],  # Matriz de recompensas
    [0, -1, 1],
    [0, 0, -1]
])

# Parámetros de aprendizaje
factor_aprendizaje = 0.8  # Tasa de aprendizaje (α)
factor_descuento = 0.95  # Factor de descuento (γ)
num_episodios = 1000

# Inicializar la matriz Q con ceros
Q = np.zeros((num_estados, num_acciones))

# Función para seleccionar una acción basada en la política ε-greedy
def seleccionar_accion(estado, epsilon):
    if np.random.uniform() < epsilon:
        return np.random.randint(num_acciones)
    else:
        return np.argmax(Q[estado, :])

# Algoritmo Q-learning
for episodio in range(num_episodios):
    estado_actual = np.random.randint(num_estados)
    epsilon = 1.0 / (episodio + 1)  # Decrementar epsilon con cada episodio
    
    while estado_actual != num_estados - 1:
        accion = seleccionar_accion(estado_actual, epsilon)
        estado_siguiente = np.random.choice(range(num_estados), p=[0.2, 0.6, 0.2])  # Transiciones de estado aleatorias
        
        # Actualizar el valor Q para el par (estado_actual, accion)
        max_valor_siguiente = np.max(Q[estado_siguiente, :])
        Q[estado_actual, accion] += factor_aprendizaje * (recompensas[estado_actual, accion] + factor_descuento * max_valor_siguiente - Q[estado_actual, accion])
        
        estado_actual = estado_siguiente

# Imprimir los valores finales de la matriz Q
print("Valores finales de la matriz Q:")
print(Q)
