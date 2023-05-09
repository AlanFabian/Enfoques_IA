#Alan de Jesus Fabian Garcia
import math

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

def tabu_search(graph, start, goal, h_func, tabu_list_len=10, max_iter=100):
    # Definir valores iniciales
    current = start
    tabu_list = []
    best_path = [current]
    best_cost = float('inf')
    
    # Ciclo principal
    for i in range(max_iter):
        # Obtener vecinos
        neighbors = get_neighbors(best_path)
        
        # Evaluar vecinos y actualizar mejor solución
        for neighbor in neighbors:
            if neighbor in tabu_list:
                continue
            cost = sum(graph[neighbor[i]][neighbor[i+1]] for i in range(len(neighbor) - 1))
            cost += h_func(neighbor[-1], goal)
            if cost < best_cost:
                best_path = neighbor
                best_cost = cost
        
        # Agregar mejor solución a lista tabú
        tabu_list.append(best_path)
        if len(tabu_list) > tabu_list_len:
            tabu_list.pop(0)
        
        # Moverse a siguiente nodo
        current = best_path[-1]
        
        # Si se alcanza la meta, salir del ciclo
        if current == goal:
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
h_func = lambda node: 0

# Buscar ruta con Tabú Search
print("Tabú Search:")
path = tabu_search(map, start, goal, h_func, tabu_list_len=3, max_iter=100)
print(path)
