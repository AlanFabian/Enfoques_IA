import math
import random

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def get_neighbors(path):
    neighbors = []
    for i in range(len(path) - 1):
        for j in range(i + 1, len(path)):
            neighbor = path[:i] + path[i:j][::-1] + path[j:]
            neighbors.append(neighbor)
    return neighbors

def simulated_annealing(graph, start, goal, h_func, initial_temp=100, temp_decay=0.99, max_iter=100):
    # Definir valores iniciales
    current = start
    current_cost = sum(graph[current][neighbor] for neighbor in graph[current])
    best_path = [current]
    best_cost = float('inf')
    temp = initial_temp
    
    # Ciclo principal
    for i in range(max_iter):
        # Obtener vecino aleatorio
        neighbors = list(graph[current].keys())
        neighbor = random.choice(neighbors)
        
        # Evaluar vecino y actualizar mejor solución
        cost = graph[current][neighbor]
        if cost < current_cost or random.random() < math.exp(-(cost - current_cost) / temp):
            current_cost = cost
            current = neighbor
            if current_cost < best_cost:
                best_path = [start, current]
                best_cost = current_cost
        
        # Reducir temperatura
        temp *= temp_decay
        
        # Si la temperatura llega a cero, salir del ciclo
        if temp == 0:
            break
    
    # Retornar mejor solución encontrada
    return best_path if current == goal else None

# Definir mapa
map = {
    'A': {'B': 1, 'C': 2},
    'B': {'D': 5, 'E': 6},
    'C': {'E': 3, 'F': 4},
    'D': {'G': 7},
    'E': {'G': 8},
    'F': {'G': 9},
    'G': {}
}

# Definir puntos de inicio y meta
start = 'A'
goal = 'G'

# Definir función heurística
h_func = euclidean_distance

# Buscar ruta con Temple Simulado
print("Temple Simulado:")
path = simulated_annealing(map, start, goal, h_func, initial_temp=100, temp_decay=0.99, max_iter=100)
print(path)
