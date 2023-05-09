#Alan de Jesus Fabian Garcia 
import math

def euclidean_distance(city1,city2):
    x1,y1 = city1
    x2,y2 = city2
    return math.sqrt((x1-x2)**2 +(y1-y2)**2)

def hill_climbing(graph,start,goal,h_func):
    #Definir los valores iniciales 
    node = start
    path =[node]
    
    #Ciclo principal
    while node != goal:
        #Obtener sucesores y sus valores de heuristica 
        succs = graph[node]
        h_scores = {succ: h_func(succ,goal)for succ in succs}
        
        #Obtener sucesor con menor valor de heuristica 
        best_succ = min(h_scores,key=h_scores.get)
        
        #Si el sucesor es peor que el nodo actual,sale del ciclo 
        if h_scores[best_succ] >= h_func(node,goal):
            break
        
        #Moverse al sucesor 
        node = best_succ
        path.append(node)
        
    #Retornar camino encontrado 
    return path if node == goal else None
#Defino el mapa 
map = {
    'A': {'B': 5, 'D': 2},
    'B': {'C': 4, 'E': 1},
    'C': {'F': 8},
    'D': {'E': 9},
    'E': {'F': 7},
    'F': {}
    
}

#Definir puntos de inicio y de meta 
start = 'A'
goal  = 'F'

#Buscar ruta con hill climbing 
print ("Hill Climbing:")
path = hill_climbing(map,start,goal,euclidean_distance)
print(path)
