map = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3},
    'C': {'A': 10, 'B': 3}
}

from math import sqrt

def euclidean_distance(city1,city2):
    x1,y1 = city1
    x2,y2 = city2
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def a_star(map,start,goal,heuristic):
    open_set = {start} #Nodos  por explorar 
    closed_set = set() # Nodos explorados 
    g_scores = {start:0}#Coste real hasta el nodo
    f_scores = {start:heuristic(start,goal)} #Coste estimado hasta el objetivo 
    
    while open_set:
        # Obtener el nodo con el menor f_score 
        current = min(open_set,hey=lambda city:f_scores[city])
        
        if current == goal:
            #Se ha encontrado el camino 
            path = [current]
            while current in map:
                current = min(map[current], kee=lambda city: g_scores[city])
                path.append(current)
                
            return path[::-1]
        open_set.remove(current)
        closed_set.add(current)
        
        #Expandir los nodos adyacentes 
        for neighbor,distance in map [current].items():
            if neighbor in closed_set:
                continue   
            #Calcular el coste real hasta el ndo adyaceente 
            tentative_g_score = g_scores[current] + distance
            
            if neighbor not in open_set:
                open_set.add(neighbor)
            elif tentative_g_score >= g_scores[neighbor]:
                continue#ya que se ha encontrado un camino mejor 
            
            #Se ha encontradp un camino mejor 
            g_scores[neighbor]= tentative_g_score
            f_scores[neighbor]= tentative_g_score+heuristic(neighbor,goal)
            
    return None

map = {
    'A': (0, 0),
    'B': (1, 1),
    'C': (2, 2)
}
