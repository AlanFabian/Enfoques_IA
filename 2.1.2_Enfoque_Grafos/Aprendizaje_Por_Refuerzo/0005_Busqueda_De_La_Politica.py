#Alan de Jesus Fabian Garcia 
import numpy as np

# Definir el entorno (ejemplo: un problema de 3 acciones)
num_estados = 3
num_acciones = 3

# Matriz de recompensas y matriz de transiciones de estado
recompensas = np.array([
    [-1, 0, 0],
    [0, -1, 1],
    [0, 0, -1]
])
transiciones_estado = np.array([
    [0.2, 0.6, 0.2],
    [0.3, 0.4, 0.3],
    [0.1, 0.2, 0.7]
])

# Parámetros del algoritmo de búsqueda de política
num_iteraciones = 1000
factor_descuento = 0.8

# Inicializar valores de los estados
valores_estados = np.zeros(num_estados)

# Algoritmo de búsqueda de política
for _ in range(num_iteraciones):
    valores_estados_actualizados = np.zeros(num_estados)
    
    # Actualizar los valores de los estados
    for estado in range(num_estados):
        accion_valores = np.zeros(num_acciones)
        
        # Calcular el valor de cada acción en el estado actual
        for accion in range(num_acciones):
            accion_valores[accion] = recompensas[estado, accion] + factor_descuento * np.sum(transiciones_estado[estado, accion] * valores_estados)
        
        # Asignar el valor máximo al estado actual
        valores_estados_actualizados[estado] = np.max(accion_valores)
    
    # Comprobar si los valores de los estados se han estabilizado
    if np.array_equal(valores_estados, valores_estados_actualizados):
        break
    
    valores_estados = valores_estados_actualizados

# Obtener la política óptima
politica_optima = np.argmax(recompensas + factor_descuento * np.matmul(transiciones_estado, valores_estados), axis=1)

# Imprimir la política óptima
print("Política óptima:")
print(politica_optima)
