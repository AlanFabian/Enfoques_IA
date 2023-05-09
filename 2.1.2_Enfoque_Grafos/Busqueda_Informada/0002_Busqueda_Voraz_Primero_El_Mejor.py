from math import sqrt

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def best_first(map, start, goal, heuristic):
    open_set = {start}
    closed_set = set()
    f_scores = {start: heuristic(start, goal)}
    
    while open_set:
        current = min(open_set, key=lambda city: f_scores[city])
        
        if current == goal:
            path = [current]
            while current in map:
                current = min(map[current], key=lambda city: f_scores[city])
                path.append(current)
            return path[::-1]
        
        open_set.remove(current)
        closed_set.add(current)
        
        for neighbor, distance in map[current].items():
            if neighbor in closed_set:
                continue
            
            if neighbor not in open_set:
                open_set.add(neighbor)
            
            f_scores[neighbor] = heuristic(neighbor, goal)
    
    return None

# Ejemplo de uso
map = {
    (0, 0): {(1, 1): 1.414, (2, 2): 2.828},
    (1, 1): {(0, 0): 1.414, (2, 2): 1.414},
    (2, 2): {(0, 0): 2.828, (1, 1): 1.414}
}

start = (0, 0)
goal = (2, 2)

path = best_first(map, start, goal, euclidean_distance)

if path is not None:
    print(f"La ruta óptima de {start} a {goal} es: {path}")
else:
    print(f"No se encontró una ruta de {start} a {goal}")
