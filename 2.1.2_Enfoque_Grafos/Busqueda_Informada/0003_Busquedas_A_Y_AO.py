import math

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def a_star(graph, start, goal, h_func):
    # Definir valores iniciales
    queue = [(start, 0, 0, [])]
    visited = set()
    
    # Ciclo principal
    while queue:
        # Obtener nodo con menor valor de f
        node, g_score, f_score, path = queue.pop(0)
        
        # Verificar si es meta
        if node == goal:
            return path + [node]
        
        # Agregar nodo a visitados
        visited.add(node)
        
        # Expandir nodos sucesores
        for succ, succ_cost in graph[node].items():
            # Verificar si sucesor ya fue visitado
            if succ in visited:
                continue
            
            # Calcular valores de g y f
            new_g_score = g_score + succ_cost
            new_f_score = new_g_score + h_func(succ, goal)
            
            # Agregar nodo a la cola de prioridad
            new_path = path + [node]
            queue.append((succ, new_g_score, new_f_score, new_path))
            
            # Ordenar cola de prioridad
            queue.sort(key=lambda x: x[2])
    
    # Si no se encontró solución
    return None

def ao_star(graph, start, goal, h_func, weight=0.5):
    # Definir valores iniciales
    queue = [(start, 0, 0, [])]
    visited = set()
    
    # Ciclo principal
    while queue:
        # Obtener nodo con menor valor de f
        node, g_score, f_score, path = queue.pop(0)
        
        # Verificar si es meta
        if node == goal:
            return path + [node]
        
        # Agregar nodo a visitados
        visited.add(node)
        
        # Expandir nodos sucesores
        for succ, succ_cost in graph[node].items():
            # Verificar si sucesor ya fue visitado
            if succ in visited:
                continue
            
            # Calcular valores de g y f
            new_g_score = g_score + succ_cost
            new_f_score = weight * new_g_score + (1 - weight) * h_func(succ, goal)
            
            # Agregar nodo a la cola de prioridad
            new_path = path + [node]
            queue.append((succ, new_g_score, new_f_score, new_path))
            
            # Ordenar cola de prioridad
            queue.sort(key=lambda x: x[2])
    
    # Si no se encontró solución
    return None

# Definir mapa
map = {
    'A': {'B': 5, 'D': 2},
    'B': {'C': 4, 'E': 1},
    'C': {'F': 8},
    'D': {'E': 9},
    'E': {'F': 7},
    'F': {}
}

# Definir puntos de inicio y meta
start = 'A'
goal = 'F'

# Buscar ruta con A*
print("A* search:")
path = a_star(map, start, goal)
