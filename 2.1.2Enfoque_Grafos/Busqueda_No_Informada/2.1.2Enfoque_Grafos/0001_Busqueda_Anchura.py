#Alan de Jesus Fabian Garcia  20/04/2023
#Anchura 
from collections import deque 

#Defino la funcion para que se aplique la busqueda por anchura 
def bfs(grafo,inicio,meta):
    #Conjunto de nodos visitados para evitar que se repitan 
    visitados = set()
    #Cola para los nodos a explorar
    queue = deque([(inicio,[])])
    
    #Hacemos iteraciones hasta que encuentre el nodo que es nuestro objetivo o hasta que se agoten los nodos que quedan por explorar
    while queue:
        node,path = queue.popleft()
        if node == meta:
            return path + [node]
        visitados.add(node)
        for vecino in grafo[node]:
            if vecino not in visitados:
                queue.append((vecino,path+[node]))
                
    return None
#Ejemplo para el uso
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
    
}
#El grafo lo represento como un diccionario de python donde las claves son nodos y los valores son las listas de los vecinos 
#La funcion bfs realiza una busqueda de anchura,tomando de entrada el grafo,el nodo de inicio y nodo objetivo.Devuelve el camino desde el nodo de inicio hasta el nodo objetivo de una forma de una lista de nodos.si no hay un camino entre nodos devuelve el estado None 

start_node = 'A'
goal_node  = 'F'
path = bfs(grafo,start_node,goal_node)
print(path)
