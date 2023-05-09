#Alan de jesus Fabian Garcia 24 de abril 2023
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': []
}
from collections import deque

def bfs (graph,start):
    visited = set()#Nodos visitados 
    queue = deque([start])#Cola de nodos a visitar 
    
    while queue: #Mientras la cola no este vacia 
        node = queue.popleft()#Sacar el primer nodo de la cola 
        
        if node not in visited:
            visited.add(node)#marcar el nodo como visitado 
            
            #Agregar los nodos adyacentes no visitados a la cola 
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    
    
    return list(visited)

graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': []
}

print(bfs(graph, 'A')) # ['A', 'B', 'C', 'D']
